from AppKit import NSWorkspace
import numpy as np
import pandas as pd
import psutil
import pyaudio
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
    )
from Quartz.CoreGraphics import (
    CGEventSourceSecondsSinceLastEventType,
    kCGEventSourceStateHIDSystemState,
    kCGAnyInputEventType
    )


class FocusComponent:
    """プロセスリスト，アクティブウィンドウ，AKF,音量を取得．"""

    def _create_cpu_df(self):
        """
        プロセスリストからプロセスデータフレームを作成．
        Returns
        ----------
        df: DataFrame
            プロセスのプロセス名，割合をデータフレームに格納．
        """
        # プロセスリストを取得．
        proc_list = self._get_cpu()
        n = len(proc_list)
        df = pd.DataFrame(np.arange(n*3).reshape(n, 3))
        for i in range(n):
            name = proc_list[i]['name']
            percent = proc_list[i]['cpu_percent']
            df.iloc[i, 0] = name
            df.iloc[i, 1] = percent
        # データを加工．
        # pythonで始まるものを削除    
        df = df[~df[0].str.match(r"python(?i)")]            
        # vcxpcで始まるものを削除
        df = df[~df[0].str.match(r"vcxpc(?i)")]            
        # system idle processを削除
        df = df[~df[0].str.match(r"system idle process(?i)")]            
        # 似ている名前を削除. (Render)などを削除
        df[0].replace(r"\s\(.+\)", "", inplace=True, regex=True) #()と(の直前の半角空白を削除
        df[0].replace(r"\sHelper", "", inplace=True, regex=True) #Helperという名前と直前の半角空白を削除
        df[0].replace(r"\.exe", "", inplace=True, regex=True)  # .exeを削除
        df = df.groupby(0).sum()[1].reset_index() 
        df = df.sort_values(1, ascending=False).reset_index(drop=True)
        return df.round(1)

    def _get_active_window(self):
        """
        アクティブウィンドウを取得．
        Returns
        ----------
        active_window: string
            アクティブウィンドウ名
        """
        # 初期値がないとスワイプアップしたときエラーになる
        active_window = "--"
        # アクティブウィンドウを取得
        curr_pid = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']
        options = kCGWindowListOptionOnScreenOnly
        window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
        for window in window_list:
            try:
                pid = window['kCGWindowOwnerPID']
                owner_name = window['kCGWindowOwnerName']
            except:
                owner_name = '--'
            if curr_pid == pid:
                    active_window = owner_name 
        return active_window

    def _get_afk(self, afk_threshold=3):
        """
        キーボードに触れていない時間．AFKかどうかを取得．
        Parameters
        ----------
        afk_threshold: int
            AFKを判定する時間閾値．
        
        Returns
        ----------
        afk_time: float
            キーボードもしくはタッチパッドに触れていない時間(秒)．
        afk: string(AFK, working)
            キーボードに触れているかどうか
        """
        # キーボードに触れていない時間を取得．
        afk_time = CGEventSourceSecondsSinceLastEventType(kCGEventSourceStateHIDSystemState, kCGAnyInputEventType)
        # 時間閾値に応じて，AFKを判定．
        if afk_time <= afk_threshold:
            afk = "Working"
        else:
            afk = "AFK"
        return afk_time, afk

    def _get_audio(self, mic_device_number=1, audio_threshold=2000):
        """
        マイクの音量．話しているかどうか
        Parameters
        ----------
        mic_device_number: int
            マイクのデバイス番号．
        audio_threshold: int
            話しているかを判定する音量閾値．
        
        Returns
        ----------
        audio_value: float
            音量を取得(単位はわからない)．
        audio_checker: string(speaking, Not speaking)
            話しているかどうか
        """
        form_1 = pyaudio.paInt16 # 16-bit resolution
        chans = 1 # 1 channel
        samp_rate = 44100 # 44.1kHz　サンプリング周波数
        chunk = 4096*3 # 一度に取得するデータ数
        mic_device_number = mic_device_number # デバイス番号
        audio = pyaudio.PyAudio() # create pyaudio instantiation
        # pyaudio streamを作成する
        stream = audio.open(format = form_1,rate = samp_rate,channels = chans, input_device_index = mic_device_number,input = True,frames_per_buffer=chunk)
        frames = []
        # loop through stream and append audio chunks to frame array
        # for i in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)
        ndarray = np.frombuffer(data, dtype='int16')
        # stop the stream, close it, and terminate the pyaudio instantiation
        stream.stop_stream()
        stream.close()
        audio.terminate()
        # 閾値処理
        audio_value = abs(ndarray.max())
        # バグが生じるのを防ぐための初期値
        audio_checker = "None"
        if audio_value >= audio_threshold:
            audio_checker = "Speaking"
        else:
            audio_checker = "Not speaking"
        return audio_value, audio_checker

    def _get_cpu(self):
        """
        プロセス名と割合をランキング順に取得．
        Returns
        ----------
        proc_list: list
            プロセス割合順にpid, プロセス名，割合を収納．
        """
        proc_list = []
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid','cpu_percent','name',])
                # cpu_percentが存在しないと降順にできないため
                if pinfo['cpu_percent'] is not None:
                        proc_list.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        proc_list = sorted(proc_list, key=lambda procObj: procObj['cpu_percent'], reverse=True)
        return proc_list
