from bs4 import BeautifulSoup
import requests
from os.path import join, abspath
requests.utils.DEFAULT_CA_BUNDLE_PATH = join(abspath('.'), 'cacert.pem')
# 定义检索的答案数
search_num = 8
# 定义baidu URL
baidu_url = "https://www.baidu.com/s?wd="
# 定义header
headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0"}
# 定义各个答案的返回
Tupu_str = "TupuAnswer"
Baike_str = "BaikeAnswer"
Zhidao_str = "ZhidaoAnswer"
Other_str = "OtherAnswer"
None_str = "NoAnswer"


def get_soup(url):
    result = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(result, "lxml")
    # 去除无关的标签
    [s.extract() for s in soup(['script', 'style', 'img'])]
    return soup
