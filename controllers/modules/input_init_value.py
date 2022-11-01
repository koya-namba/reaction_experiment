# import pyaudio


class InputInitValue:
    """
    名前とマイク番号を入力する
    """

    @staticmethod
    def main():
        """
        名前とマイク番号を入力する
        Returns
        ----------
        name: string
            被験者の名前
        """
        # 名前を取得
        print("-"*50)
        name = input('名前を入力してください(例：山田 >> yamada) : ')

        return name
