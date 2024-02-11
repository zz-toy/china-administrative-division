# govstat
- [scrapy github](https://github.com/scrapy/scrapy)
- [tuna anaconda 源](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
- [python downloads](https://www.python.org/downloads/)
- [conda install](https://anaconda.org/conda-forge/pymysql)

## 介绍
爬虫项目，用来爬取省市区乡镇村庄数据

一共5个爬虫，分别爬取各自数据并入库：
- python launch_province.py
- python launch_city.py
- python launch_county.py
- python launch_town.py
- python launch_village.py

## 开发环境
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

## 使用
```shell
pip install -r requirements.txt
```