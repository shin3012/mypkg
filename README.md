# threshold_alarm: ROS2 しきい値アラーム

数を数えるノードと，その数がある値以上になったときにアラートを出すノードからなるROS2パッケージです．

- `talker` ノード: 0,1,2,... と整数を一定間隔で Publish します．
- `threshold_alarm` ノード: 整数を Subscribe して、しきい値以上になったらログで知らせます．


[![test](https://github.com/shin3012/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/shin3012/mypkg/actions/workflows/test.yml)


## ダウンロードとビルド

ROS2のワークスペース`~/ros2_ws`を使うことを想定しています

```bash
$ cd ~/ros2_ws/src
$ git clone https://github.com/shin3012/mypkg
$ cd ~/ros2_ws
$ colcon build
```
ビルド後に環境設定を読み込みます．
```bash
$ source /opt/ros/foxy/setup.bash
$ source ~/ros2_ws/install/setup.bash
```

## ノードとトピック
### talker ノード
countという整数カウンタを0,1,2...と増やして送るノードです．

- 実行コマンド：
```bash
$ ros2 run mypkg talker
```

#### 動作
 - /count トピックにstd_msgs/msg/Int32型のメッセージをPublish します．
 - 0.5秒ごとに値が1ずつ増えていきます．
 - 送った値はログに出ます．
 ```text
 [talker-1] [INFO] [⋯] [talker]: Publish: 0
 [talker-1] [INFO] [⋯] [talker]: Publish: 1
 ...
 ```

### threshold_alarm ノード
/count を監視して，しきい値以上になったときに[ALERT]を1回だけだすノードです．

- 実行コマンド：
```bash
$ ros2 run mypkg threshold_alarm
```

#### 動作：
 - /count トピックからstd_msgs/msg/Int32を受け取ります．
 - 値がしきい値以上になったタイミングで，以下のようなログが出ます．
 ```text
 [threshold_alarm-2] [INFO] [⋯] [threshold_alarm]: ALERT: value 10 >= threshold 10
 ```

## ローンチファイル
二つのノードをまとめて起動するローンチファイルです

- ファイル：launch/talk_alarm.launch.py

- 実行例：
```bash
$ source /opt/ros/foxy/setup.bash
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
$ ros2 launch mypkg talk_alarm.launch.py
```
動作が成功している場合以下のようなログが流れます．
```text
[talker-1] [INFO] [⋯] [talker]: Publish: 0
...
[talker-1] [INFO] [⋯] [talker]: Publish: 10
[threshold_alarm-2] [INFO] [⋯] [threshold_alarm]: ALERT: value 10 >= threshold 10
```

## テスト
### 実行方法
```bash
$ cd ~/ros2_ws/src/mypkg/test
$ ./test.bash
```
## 環境
- 開発環境（ローカル）：ubuntu 20.04 / python 3.8
- 実行環境(リモート)：GitHub Actions ubuntu-latest / ROS 2 Humble


## 最後に
- このソフトウェアパッケージは，BSD 3-Clause ライセンスの下，再頒布および使用が許可されます.
- © 2025 Saito Shinnosuke
