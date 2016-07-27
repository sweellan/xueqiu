# -*- coding: utf-8 -*-

import requests
import json
# url='http://xueqiu.com/P/ZH382868'
# url='http://xueqiu.com/P/ZH233641'
url='https://xueqiu.com/P/ZH918570'  #my own

def scrape_portfolio(url):

    reqst=requests.get(url)
    theheaders={'Accept':'*/*',
             'Accept-Encoding':'gzip, deflate, sdch',
             'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
             'Cache-Control':'max-age=0',
             'Connection':'keep-alive',
             'Cookie':'s=2f9y11mae1; xq_r_token=0fd1c5ad06a1272407d710720be1d6eb2a0d6472; _sid=FsXa4M7XA1Jrc00utGff1vl4wpAFdi; xq_a_token=45b07bb0de3ada3c54f6d4f514c7d1c2dd3264a6; xq_is_login=1; bid=c58dcca58d63a9bda58851c906350d2a_ir1oxlko; snbim_minify=true; __utma=1.1945563305.1469430585.1469430585.1469430585.1; __utmb=1.3.10.1469430585; __utmc=1; __utmz=1.1469430585.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1469430165,1469430170,1469430288,1469430442; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1469431210',
             'Host':'xueqiu.com',
             'Referer':'http://xueqiu.com/P/ZH382868',
             'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
             'X-Requested-With':'XMLHttpRequest'}
    reqst=requests.get(url, headers=theheaders)
    html=reqst.text
    pos_start = html.find('SNB.cubeInfo = ') + len('SNB.cubeInfo = ')
    pos_end = html.find('SNB.cubePieData')
    data_name = html[pos_start:pos_end]
    dic_name = json.loads(data_name)
    pos_start =html.find('SNB.cubeTreeData = ') + len('SNB.cubeTreeData = ')
    # print(pos_start)
    pos_end = html.find('SNB.marketInfo')
    # print(pos_end)
    data_portfolio = html[pos_start:pos_end-2]  # -2把最后的分号去掉
    dic_portfolio = json.loads(data_portfolio)

    portfolio={}
    for i in dic_portfolio:
        portfolio[i]=dic_portfolio[i]['stocks']
        for j in portfolio[i]:
            del j['stock_id']
            del j['segment_name']
            del j['segment_id']
            del j['stock_symbol']
            del j['segment_color']
            del j['proactive']
            del j['volume']
            del j['textname']

    # print(pos_start)
    # print(data_name)
    # print(dic_name['name'])
    # print(data_portfolio)
    # print(dic_portfolio)
    print(portfolio)
    # for i in dic_portfolio:
    #     print(i)
    # print(reqst.text)




scrape_portfolio(url)