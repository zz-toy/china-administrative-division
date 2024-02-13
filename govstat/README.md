# govstat
- [scrapy github](https://github.com/scrapy/scrapy)
- [tuna anaconda 源](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
- [python downloads](https://www.python.org/downloads/)
- [conda install](https://anaconda.org/conda-forge/pymysql)

## 描述
爬虫项目，用来抓取省市区乡镇村庄数据

一共5个爬虫，分别爬取各级数据并入库:
- python launch_province.py
- python launch_city.py
- python launch_county.py
- python launch_town.py
- python launch_village.py

## 环境搭建
```shell
# 创建虚拟环境
conda create --name china-administrative-division

# 安装依赖
pip install -r requirements.txt
```

## 如何使用
### 抓取命令
```shell
python launch_province.py
python launch_city.py
python launch_county.py
python launch_town.py
python launch_village.py
```

### 导出数据
```shell
python tool/export.py
```