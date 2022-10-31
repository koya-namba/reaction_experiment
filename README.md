# プロセス取得実験(11/1)

## 目次
1. 実験準備
    - 仮想環境を使わない
    - condaを使う
    - pyenv, pyenv-virtualenvを使う
    - 上記以外を使う

2. 実験

3. 参考

## 実験準備
pythonの環境に応じて，以下の4つから実験用の仮想環境構築とコードが動くか確認をお願いします．  

ちなみにコードをダウンロードする方法はgithubのページで，  

<img width="800" alt="スクリーンショット 2022-10-29 15 13 47" src="https://user-images.githubusercontent.com/82089820/198816898-a9539a68-229a-44b0-a7d7-c5631480a5c2.png">  

をクリックするとできます.

---

### 仮想環境を使わない

1. pythonがインストールされているか確認します．  
下記を実行してください．
```bash
$ python -V
```
もしくは，
```bash
$ python3 -V
```

pythonのバージョンが ~~3.8.5(2022/10/30)~~ 3.7.0以上3.10.7以下なら問題なくコードは動きます．

2. 必要なライブラリをインストールします．  
以下を実行してください．
```bash
$ pip install numpy==1.22.1
$ pip install pandas==1.3.5
$ pip install psutil==5.9.0
$ pip install PyAudio==0.2.11
$ pip install pyobjc-framework-Quartz==8.2
```

3. 次にコードをクローンもしくはzipをダウンロードしてください．  
クローンもしくはダウンロードしたらフォルダまで移動をお願いします.(vscodeで開いてもOKです．)  
<img width="300" alt="スクリーンショット 2022-10-29 10 48 46" src="https://user-images.githubusercontent.com/82089820/198760360-5270c4a6-5b18-4cf8-a0af-4a2977a7c5b1.png">

4. コードが動くか確認．  
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
フォルダを削除しないようにお願いします．

---

### conda
1. まずはコードをクローンもしくはzipをダウンロードしてください．  
クローンもしくはダウンロードしたらフォルダまで移動をお願いします.(vscodeで開いてもOKです．)  
<img width="300" alt="スクリーンショット 2022-10-29 10 48 46" src="https://user-images.githubusercontent.com/82089820/198760360-5270c4a6-5b18-4cf8-a0af-4a2977a7c5b1.png">

2. まずは仮想環境を確認します．
```bash
$ conda info -e
```

いろいろな仮想環境を作成している場合には，下記のように表示されます．  
もし過去に同じ実験に参加している場合は，reaction_envという環境が作成されています．  
その場合は，6番までとばしてOKです．
```bash
# conda environments:
#
base                  *  /Users/koya/miniforge3
drf-env                  /Users/koya/miniforge3/envs/drf-env
gtts                     /Users/koya/miniforge3/envs/gtts
workout_app_env          /Users/koya/miniforge3/envs/workout_app_env
workout_record_venv      /Users/koya/miniforge3/envs/workout_record_venv
```

3. 新しく仮想環境を作成します．以下を実行してください．
```bash
$ conda create -n reaction_env python=3.8.13
```

4. 次に仮想環境に入ります．実験用のフォルダにいることを確認して，以下を実行してくさい.
```bash
$ conda activate reaction_env
```
すると，パスの前に仮想環境名が表示されると思います．  
以下のようになっていればOKです．  
<img width="400" alt="スクリーンショット 2022-10-29 10 48 38" src="https://user-images.githubusercontent.com/82089820/198760567-48de42c9-2b34-4ca9-a32c-fd6e0501e6e9.png">

5. 必要なライブラリをインストールします．
```bash
$ conda install -c anaconda numpy
$ conda install -c anaconda pandas
$ conda install -c conda-forge/label/cf202003 psutil
$ conda install -c anaconda pyaudio
$ conda install -c conda-forge/label/cf202003 pyobjc-framework-quartz
```

6. コードが動くか確認．  
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
以下のコマンドを実行すると仮想環境から抜けられます．
```bash
conda deactivate
```
<img width="623" alt="スクリーンショット 2022-10-29 14 28 34" src="https://user-images.githubusercontent.com/82089820/198815568-08aef2e9-1fdb-4e1f-92c3-7bb58c1ce131.png">

実験本番まで，フォルダや仮想環境は削除しないでください．

---

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

---

### 上記以外を使う
下記の条件を満たすように環境構築をお願いします．  
- pythonのバージョンが ~~3.8.5(2022/10/30)~~ 3.7.0以上3.10.7
- 以下のライブラリをインストール
  - numpy==1.22.1
  - pandas==1.3.5
  - psutil==5.9.0
  - PyAudio==0.2.11
  - pyobjc-framework-Quartz==8.2

仮想環境に入って動作を確認してください．

コードが動くか確認．  
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
実験本番まで，フォルダや仮想環境などは削除しないようにお願いします．


## 実験
実験用のフォルダに移動してください．

* 仮想環境を使わない人はフォルダまで移動してください．

* condaを使っている人は，以下を実行してください．
```bash
$ conda activate reaction_env
```

* pyenv, pyenv-virtualenvを使っている人はフォルダに移動するだけでOKです．

* 上記以外の場合は仮想環境の中に入って，実験フォルダまで移動してください．

**以下，どちらも共通です！**  
パスの前に仮想環境名が表示されていればOKです！  
<img width="400" alt="スクリーンショット 2022-10-29 10 48 38" src="https://user-images.githubusercontent.com/82089820/198760567-48de42c9-2b34-4ca9-a32c-fd6e0501e6e9.png">

#### 実験開始

実験が始まったら，main.pyを実行してください．　
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
$ Please input(finish): 
```

#### 実験終了
finishを入力してください．

```bash
$ Please input(finish): finish
```

以下のように表示されれば問題ないです．
```bash
task-1: csvへの書き込みを完了しました
--------------------------------------------------
すべてのプロセスが正常に終了しました
```

#### 提出
dataフォルダをzipにして，slackもしくはgoogle driveにアップしてください．
<img width="700" alt="スクリーンショット 2022-10-29 14 57 45" src="https://user-images.githubusercontent.com/82089820/198816376-16f8b4b6-191f-4f08-b91e-38fc86d5b47a.png">

以上で実験を終了します．  
ご協力ありがとうございました．


## 参考
- [M1 Macで機械学習やPythonはMiniforgeを使う](https://qiita.com/kujirahand/items/9bf1a1e7bd34bdb87da5)
- [Mac/LinuxのPython環境構築をMiniForgeで行う理由](https://zenn.dev/karaage0703/articles/f3254b14898b4d)
- [Anacondaでbaseが自動的にactivateされるのを防ぎたい](https://ja.stackoverflow.com/questions/61630/anaconda%E3%81%A7base%E3%81%8C%E8%87%AA%E5%8B%95%E7%9A%84%E3%81%ABactivate%E3%81%95%E3%82%8C%E3%82%8B%E3%81%AE%E3%82%92%E9%98%B2%E3%81%8E%E3%81%9F%E3%81%84)
- [pyenvとpyenv-virtualenvの自分流使い方](https://qiita.com/ksato9700/items/5d9eba10fe6b8e064178)
- [pyenv 利用のまとめ](https://qiita.com/m3y/items/45c7be319e401b24fca8)
- [pyenv をinstallした後に python not foundとなる問題](https://zenn.dev/ymd/articles/68ed58e45ea275)
- [【初心者向け】Anacondaで仮想環境を作ってみる](https://qiita.com/ozaki_physics/items/985188feb92570e5b82d)
