import pyaudio


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
        mic_device_number: int
            マイクのデバイス番号
        """
        # 名前を取得
        print("-"*50)
        name = input('名前を入力してください(例：山田 >> yamada) : ')

        # マイクの番号を取得
        print("-"*50)
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            chan = p.get_device_info_by_index
            print(chan(i)["index"], chan(i)["name"])    
        mic_device_number = int(input("マイクのデバイス番号を整数で入力してください: "))

        return name, mic_device_number
