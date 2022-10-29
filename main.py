import controllers.main as main


########## 必要に応じて以下を書き換えてください ##########

# 作業中かを判定する時間
AFK_THRESHOLD = 5

# 話しているかを判定する音量
AUDIO_THRESHOLD = 2000

# CSVにデータを書き込む時間間隔
WRITE_CYCLE = 1


##################################################


if __name__ == "__main__":
        main.main(AFK_THRESHOLD, AUDIO_THRESHOLD, WRITE_CYCLE)
