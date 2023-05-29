import requests
import re
from time import sleep

def getCiteNumbyTitle(paper_title, session):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    params = {
        'hl': 'zh-CN',
        'as_sdt': '0,5',
        'q': paper_title,
        'btnG': '',
    }

    response = session.get('https://sc.panda321.com/scholar', params=params, headers=headers)
    num_cite = re.findall(r'被引用次数：(.*?)</a>', response.text)
    # print(paper_title)
    # print(num_cite)
    num_cite = num_cite[0] if len(num_cite) != 0 else -1
    return num_cite


session = requests.session()

with open('README.md', 'r') as f:
    text = f.readlines()
    start_idx = text.index('### Papers\n') + 3
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
