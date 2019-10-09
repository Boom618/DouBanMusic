# coding:utf-8
from lxml import etree
import requests
from SQL_method import SQL_Method

sql = SQL_Method()


# 抓取 豆瓣 歌曲
# 获取页面地址
def getUrl():
    sql.creatDB()
    for i in range(10):
        url = 'https://music.douban.com/top250?start={}'.format(i * 25)
        scrapyPage(url)


# 爬取每页数据
def scrapyPage(url):
    html = requests.get(url).text
    s = etree.HTML(html)
    trs = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr')

    for tr in trs:
        href = tr.xpath('./td[2]/div/a/@href')[0]
        title = tr.xpath('./td[2]/div/a/text()')[0]
        score = tr.xpath('./td[2]/div/div/span[2]/text()')[0]
        number = tr.xpath('./td[2]/div/div/span[3]/text()')[0]
        img = tr.xpath('./td[1]/a/img/@src')[0]

        print("地址是：" + href)
        print("歌名是：" + title.strip())
        print("评分是：" + score)
        number = number.strip()
        number = number.replace("(", "")
        number = number.replace(")", "")
        print("点赞是：" + number.strip())
        print("图片是：" + img)

        sql.insertDB(href, title.strip(), score, number, img)


if __name__ == '__main__':
    getUrl()
