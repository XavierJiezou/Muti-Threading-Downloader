import requests
import time
start = time.time()
url = 'https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/1250921_c7af3a2b73d03604f6421ef11134af72.mp4'
res = requests.get(url, stream=True)
with open('test.mp4', 'wb') as f:
    for chunk in res.iter_content(chunk_size=10240):
        f.write(chunk)
end = time.time()
print(end-start)
