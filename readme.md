# introduce
this is a Multithreading downloader based on python. 
# why multithreading
multithreading can maximize the use of the network that single threading cannot.
# install
```bash
pip3 install requests
```
# single threading
[single_threading.py](single_threading.py)
# multi threading
[muti_threading.py](muti_threading.py)
# test sample
```https
https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/1250921_c7af3a2b73d03604f6421ef11134af72.mp4
```
# comparation
| item | muti-threading |  single-threading |
|:--:|:--:|:--:|
| total-time | 93s | 560s |
| average-speed | 9.06MB/s | 1.50MB/s|
# todo
- [x] mutithreading
- [ ] breakpoint resume
- [ ] gui
# more details
```https
https://mp.weixin.qq.com/s/D92aFTd5ywMgYJv7_7h7-Q
https://blog.csdn.net/qq_42951560/article/details/108785802
```
# reference
```https
[0] https://blog.csdn.net/qq_41488943/article/details/107118377
[1] https://docs.python.org/zh-cn/3.8/library/concurrent.futures.html#threadpoolexecutor
[2] https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html#id9
```