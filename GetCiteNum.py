import requests
import re
from time import sleep

def getCiteNumbyTitle(paper_title, session):
    headers = {
        'authority': 'scholar.lanfanshu.cn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,zh-Hans;q=0.8',
        'cache-control': 'max-age=0',
        'referer': 'https://scholar.lanfanshu.cn/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    params = {
        'hl': 'zh-CN',
        'as_sdt': '0,5',
        'q': paper_title,
        'btnG': '',
    }

    response = session.get('https://0-scholar-google-com.brum.beds.ac.uk/scholar', params=params, headers=headers)
    num_cite = re.findall(r'被引用次数：(.*?)</a>', response.text)
    # print(paper_title)
    # print(num_cite)
    num_cite = num_cite[0] if len(num_cite) != 0 else -1
    return num_cite


session = requests.session()

with open('README.md', 'r') as f:
    text = f.readlines()
    start_idx = text.index('#### Full Version\n') + 3
    end_idx = text.index('### Datasets\n')

    for relate_row, item in enumerate(text[start_idx:end_idx]):
        paper_title = re.findall(r'\[(.*?)\]', item)
        old_cite_num = re.findall(r'Cited by(?:\s*?)(\d+?)(?:\s*?)\|', item)
        if len(paper_title) != 0 and len(old_cite_num) != 0:
            paper_title = paper_title[0]
            old_cite_num = old_cite_num[0]
            # print(paper_title, old_cite_num)
            now_cite_num = getCiteNumbyTitle(paper_title, session)
            # print(now_cite_num)
            if now_cite_num != -1 and old_cite_num != now_cite_num:
                text[start_idx+relate_row] = re.sub(r'Cited by(?:\s*?)(\d+?)(?:\s*?)\|', f'Cited by {now_cite_num} |', text[start_idx+relate_row])

with open('README.md', 'w') as f:
    f.writelines(text)
