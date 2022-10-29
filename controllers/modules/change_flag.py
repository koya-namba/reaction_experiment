import time


class ChangeFlag:
    """
    キーボード入力からフラグを変更する．
    Attributes
    ----------
    flag: string(no, finish)
        機能の処理を制御．
    """

    @staticmethod
    def main(flag):
        """
        キーボード入力からフラグを変更する．
        Parameters
        ----------
        flag: string(no, finish)
            機能の処理を制御．
        """
        time.sleep(5)
        # キーボード入力を受け取る
        while True:
            print("-"*50)
            print('終了する場合にはfinishを入力してください')
            keyboard_row_input = input('Please input(finish): ')    
            if keyboard_row_input =="finish":
                flag.value = keyboard_row_input
            else:
                print('#'*50)
                print('#### "finish"を入力してください #####')
                print('#'*50)
            
            if flag.value == 'finish':
                break
