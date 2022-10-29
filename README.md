# プロセス取得実験(11/1)

## 目次
1. 実験準備
    1. pyenv, pyenv-virtualenv
    2. conda
    3. 仮想環境を特に用いていない人

2. 実験

## 実験準備
pythonの環境に応じて，以下の3つから実験用の仮想環境構築とコードが動くか確認をお願いします．

### pyenv, pyenv-virtualenv
1. まずはコードをクローンもしくはzipをダウンロードしてください．  
クローンもしくはダウンロードしたらフォルダまで移動をお願いします.(vscodeで開いてもOKです．)  
<img width="300" alt="スクリーンショット 2022-10-29 10 48 46" src="https://user-images.githubusercontent.com/82089820/198760360-5270c4a6-5b18-4cf8-a0af-4a2977a7c5b1.png">


2. 次に利用するpythonを指定します  
以下のコマンドを実行して，3.8.13がインストールされているか確認してください．
```bash
$ pyenv versions
```

インストールされていない場合には，以下のような表示になります．
```bash
  system
* 3.9.8 (set by /Users/koya/.pyenv/version)
```

もし3.8.13がインストールされていない場合には，下記を実行します．  
(少し時間がかかると思います)
```bash
$ pyenv install 3.8.13
```

もう一度3.8.13がインストールされているか確認します．
```bash
$ pyenv versions
```

以下のように表示されればOKです．
```bash
  system
  3.8.13
* 3.9.8 (set by /Users/koya/.pyenv/version)
```

3. pyenv-virtualenvで仮想環境を作成します．  
以下を実行します．
```bash
$ pyenv virtualenv 3.8.13 reaction_env
```

もう一度下記を実行します．
```bash
$ pyenv versions
```

そして，reaction_envが加わっていればOKです．
```
  system
  3.8.13
  3.8.13/envs/reaction_env
* 3.9.8 (set by /Users/koya/.pyenv/version)
  reaction_env
```

実験用のフォルダにいることを確認して下記を実行します．
```bash
$ pyenv local reaction_env
```

すると，パスの前に仮想環境名が表示されると思います．  
以下のようになっていればOKです．  
<img width="400" alt="スクリーンショット 2022-10-29 10 48 38" src="https://user-images.githubusercontent.com/82089820/198760567-48de42c9-2b34-4ca9-a32c-fd6e0501e6e9.png">


4. 必要なライブラリをインストールします．  
以下を実行してください．
```bash
$ pip install numpy==1.22.1
$ pip install pandas==1.3.5
$ pip install psutil==5.9.0
$ pip install PyAudio==0.2.11
$ pip install pyobjc-framework-Quartz==8.2
```

5. コードが動くか確認．  
main.pyを実行します．
```bash
$ python main.py
```

次に名前を入力して，enterを押します．
```bash
$ 名前を入力してください(例：山田 >> yamada) : namba
```

次にマイクの番号を選択します．  
外部マイクを使っている場合には，外部マイクを選択してください．  
それ以外の場合は，MacBook Proのマイクを選択してください．  
```bash
0 EV2785
1 BlackHole 16ch
2 BlackHole 2ch
3 外部マイク
4 外部ヘッドフォン
5 MacBook Proのマイク
6 MacBook Proのスピーカー
7 Microsoft Teams Audio
8 ZoomAudioDevice
9 機器セット
$ マイクのデバイス番号を整数で入力してください: 3
```

下記のように表示されれば問題ないです．  
finishを入力して，実行を終了してください．
```bash
task-1: csvへの書き込みを始めます
--------------------------------------------------
終了する場合にはfinishを入力してください
$ Please input(finish): finish
```

以下のように表示されれば問題ないです．
```bash
task-1: csvへの書き込みを完了しました
--------------------------------------------------
すべてのプロセスが正常に終了しました
```

最後にreaction_experimentフォルダの中のdataフォルダにcsvファイルが保存されているか確認してください．  
<img width="300" alt="スクリーンショット 2022-10-29 10 47 33" src="https://user-images.githubusercontent.com/82089820/198760880-bc149fdf-a0d8-4b07-811c-b9236378b821.png">

これで実験準備は終了です．
特にコマンドを実行しなくても，フォルダを移動すると仮想環境から抜けるはずです．  
<img width="500" alt="スクリーンショット 2022-10-29 11 07 16" src="https://user-images.githubusercontent.com/82089820/198767798-9bc2276d-92f2-4504-afd3-75ec409e4a5f.png">

実験本番まで，フォルダなどは削除しないようにお願いします．