<!--
 * @Author: hibana2077 hibana2077@gmaill.com
 * @Date: 2023-04-29 14:51:15
 * @LastEditors: hibana2077 hibana2077@gmaill.com
 * @LastEditTime: 2023-05-01 10:19:01
 * @FilePath: /smart_hydroponic_farm/doc/jetson_nano.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# Jetson Nano 建置與部署

## 準備

- [ ] Jetson Nano 開發板
- [ ] SD card
- [ ] 電源供應器

## 安裝作業系統

[ref](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

- 下載 Image 檔案，預設版本為最新的版本。
- 使用 Etcher 將 Image 檔案 (壓縮檔即可) 燒進 microSD 卡裡，以 28 MB/s 的速度 Flash、 40 MB/s 的速度 Validate 總共大約需要 15 分鐘。

## 設定開機

- 將 microSD 卡插入 Jetson Nano 開發板。
- 跳帽設定為 5V 4A 電源供應器。(J48)
- 用HDMI連接螢幕。
- 開機

## 設定網路(有線)

*新思AIOT可考慮用新思的板子作為網路橋接器*

- 網路線插好。
- ifconfig 查看網路設定。

## 其他設定

```bash
# 顯示當前模式
$ sudo nvpmodel -q
# 預設為高效能模式(10W)，此功率需用 DC 5V 4A 供電，不然會突然關機
$ sudo nvpmodel -m 0
# 若使用 Micro-USB 供電需切換到 5W 模式
$ sudo nvpmodel -m 1
```

cuda 設定

```bash
# 使用nano編輯環境檔案
$ sudo nano ~/.bashrc
```

最後面加入以下內容：

```bash
export CUDA_HOME=/usr/local/cuda-10.2
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-10.2/bin:$PATH
```

```bash
# 完成後，使其生效：
$ source ~/.bashrc
# 測試是否有生效
$ nvcc -V
```

```bash
# 安裝 pip3 工具
$ sudo apt-get install python3-pip python3-dev build-essential 
$ sudo -H pip3 install --upgrade pip
$ sudo -H pip3 install jetson-stats
$ sudo systemctl restart jetson_stats.service
```

```bash
$ sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran qtbase5-dev python3-matplotlib
# 安裝 pycuda 是為了能用 python 將 onnx 模型轉成 trt 模型
$ pip3 install pycuda
# 安裝 onnx 前需要先安裝 protobuf-3.8.0，我們使用 bash 檔安裝
$ wget https://raw.githubusercontent.com/jkjung-avt/jetson_nano/master/install_protobuf-3.8.0.sh
$ bash install_protobuf-3.8.0.sh
# 接著安裝 onnx 1.4.1 版本
$ pip3 install onnx==1.4.1
```

