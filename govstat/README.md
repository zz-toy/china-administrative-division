# govstat
- [scrapy](https://scrapy.org/)
- [scrapy github](https://github.com/scrapy/scrapy)
- [tuna anaconda](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
- [python版本](https://www.python.org/downloads/)
- [conda install pkg](https://anaconda.org/conda-forge/pymysql)

## 介绍
爬虫项目，用来爬取省市区城镇乡村数据

一共5个爬虫，分别爬取各自数据并入库：
- province
- city
- county
- town
- village

## 搭建开发环境
```shell
# 创建虚拟环境
conda create --name china-administrative-division
```

## 安装依赖项
```shell
conda install python=3.10
conda install -c conda-forge scrapy==2.9.0
conda install -c conda-forge pymysql
conda install "PyMySQL[rsa]"
conda install scrapy-redis
pip install redis
pip install Twisted==22.10.0
conda install fake-useragent
```