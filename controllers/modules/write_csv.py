from datetime import datetime as dt
import time

import pandas as pd

from controllers.modules.components.focus_component import FocusComponent


class WriteCsv(FocusComponent):
    """
    CSVにデータを書き込む．
    Attributes
    ----------
    name: string
        プログラムを用いている人の名前．
    write_cycle: int
        csvファイルに書き込む時間間隔(秒)．
    afk_threshold: int
        AFKを判定する時間閾値．
    """

    def __init__(self, name, write_cycle, afk_threshold):
        """
        Parameters
        ----------
        name: string
            プログラムを用いている人の名前．
        write_cycle: int
            csvファイルに書き込む時間間隔(秒)．
        afk_threshold: int
            AFKを判定する時間閾値．
        """
        self.name = name
        self.write_cycle = write_cycle
        self.afk_threshold = afk_threshold

    def _create_file(self):
        """
        csv保存用のファイル(ファイル名)を作成．
        Returns
        ----------
        file_name: string
            プログラムを起動している人の名前と現在時間から作成．
        """
        now = dt.now()
        now_str = now.strftime('%Y%m%d_%H%M%S')
        file_name = now_str + '_' + self.name
        f = open(f'data/{file_name}.csv', 'w')
        f.close()
        return file_name

    def main(self, flag):
        """
        csvファイルに書き込むためのDF作成．終了時にファイルに書き込み．
        Parameters
        ----------
        flag: string(yes, no, finish)
            OBSの表示の有無を制御．終了フラグ．
        """
        print("-"*50)
        print('task-1: csvへの書き込みを始めます')
        # データフレームを作成
        proc_df = self._create_cpu_df()
        proc_df = proc_df.rename(columns={1: 'cycle1'})
        active_window = self._get_active_window()
        afk_time, _ = self._get_afk(self.afk_threshold)
        now = dt.now()
        # データフレームに追加
        # AFK，アクティブウィンドウ，時間の有無を追加
        proc_df.loc[len(proc_df)] = ["AFK", afk_time]
        proc_df.loc[len(proc_df)] = ["Active Window", active_window]
        proc_df.loc[len(proc_df)] = ['DateTime', now]
        # データフレームにデータをどんどん追加
        i = 2
        while True:
            time.sleep(self.write_cycle)
            df_topn = self._create_cpu_df()
            df_topn = df_topn.rename(columns={1: f'cycle{i}'})
            active_window = self._get_active_window()
            afk_time, _ = self._get_afk(self.afk_threshold)
            now = dt.now()
            # AFK，アクティブウィンドウ，時間の有無を追加
            df_topn.loc[len(df_topn)] = ["AFK", afk_time]
            df_topn.loc[len(df_topn)] = ["Active Window", active_window]
            df_topn.loc[len(df_topn)] = ['DateTime', now]
            # pandasをマージする
            proc_df = pd.merge(proc_df, df_topn, on=0, how="outer")
            # サイクルを追加
            i += 1
            # 終了の入力
            if flag.value == 'finish':
                file_name = self._create_file()
                proc_df.T.to_csv(f'data/{file_name}.csv', header=False)
                print("-"*50)
                print('task-1: csvへの書き込みを完了しました')
                break
