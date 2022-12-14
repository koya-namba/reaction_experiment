from ctypes import c_char_p
from multiprocessing import Manager
import threading

from controllers.modules.change_flag import ChangeFlag
from controllers.modules.input_init_value import InputInitValue
from controllers.modules.write_csv import WriteCsv


def main(afk_threshold, write_cycle):
    """
    メイン実行．
    Parameters
    ----------
    afk_threshold: int
        AFK判定の時間閾値．
    write_cycle: int
        CSVファイルに書き込む時間間隔．
    Returns
    ----------
    
    """
    # インプット関数から名前とマイク番号を取得
    name = InputInitValue.main()
    
    # 終了フラグスレッド
    manager = Manager()
    flag = manager.Value(c_char_p, 'no')
    change_flag_thread = threading.Thread(
        target=ChangeFlag.main, 
        args=(flag,)
        )

    # csvファイルへの書き込み
    write_csv = WriteCsv(name, write_cycle, afk_threshold)

    # プロセス開始
    change_flag_thread.start()
    write_csv.main(flag)
    change_flag_thread.join()

    print("-"*50)
    print('すべてのプロセスが正常に終了しました')
