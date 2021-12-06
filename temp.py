import requests
from tqdm import tqdm


def single_thread(url: str):
    res = requests.get(url, stream=True)
    with open('test.mp4', 'wb') as f:
        for chunk in tqdm(res.iter_content(chunk_size=1024**2), total=int(int(res.headers['content-length'])/1024/1024)+1, unit='MB'):
            f.write(chunk)


if __name__ == '__main__':
    single_thread('https://1251316161.vod2.myqcloud.com/007a649dvodcq1251316161/2074194f5285890808508755340/Q5TVeeaCdf0A.mp4')
