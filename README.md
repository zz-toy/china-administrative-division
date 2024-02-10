# china-administrative-division
中国行政区划数据

## 描述
中华人民共和国行政区划（五级）：省级、地级、县级、乡级和村级。

该项目提供最新的省市区数据，方便业务升级。


## 数据来源
- 国家统计局
    - [中华人民共和国国家统计局-统计用区划和城乡划分代码](https://www.stats.gov.cn/sj/tjbz/qhdm/)
    - [中华人民共和国国家统计局-统计用区划代码和城乡划分代码编制规则](https://www.stats.gov.cn/sj/tjbz/gjtjbz/202302/t20230213_1902741.html)
- 本项目已更新至
    - [2023年统计用区划代码和城乡划分代码（截止时间：2023-06-30，发布时间：2023-09-11）](https://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2023/index.html)
- [参考百度地图](https://lbsyun.baidu.com/faq/api?title=webapi/download)

## 数据库支持
目前本项目数据保存在 sqlite3，数据文件下载：data.sqlite。

可以按需将数据迁移到其他数据库管理系统中（MySQL, Oracle, MSSQL 等）。

## 数据下载
- 单独级别数据

| 文件列表 | JSON |	CSV |
|---|---|---|
| 省级(省份, 直辖市, 自治区) | [province.json](province.json) | [province.csv](province.csv) |
| 市级(城市, 市区) | [city.json](city.json) | [city.csv](city.csv) |
| 区级(区县, 县城) | [district.json](district.json) | [district.csv](district.csv) |
| 乡级(乡镇、街道) | [street.json](street.json) | [street.csv](street.csv) |
| 村级(村委会、居委会) | [village.json](village.json) | [village.csv](village.csv) |

- 级联数据

| 文件列表 | 普通 |	带编码 |
|---|---|---|
| "省,市" 二级联动数据 | [pc.json](pc.json) | [pc-code.csv](pc-code.csv) |
| "省,市,区" 二级联动数据 | [pcd.json](pcd.json) | [pcd-code.csv](pcd-code.csv) |
| "省,市,区,乡" 二级联动数据 | [pcds.json](pcds.json) | [pcds-code.csv](pcds-code.csv) |
| "省,市,区,乡,村" 二级联动数据 | [pcdsv.json](pcdsv.json) | [pcdsv-code.csv](pcdsv-code.csv) |

提示：需要打包下载全部文件，请看 Releases。
