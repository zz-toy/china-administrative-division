# china-administrative-division
中国行政区划数据

## 描述
中华人民共和国行政区划（五级）：省级、地级、县级、乡级和村级。

该项目提供最新的省市区乡镇村庄数据，方便业务升级。

港澳台数据暂无。

## 数据来源
- 国家统计局
    - [中华人民共和国国家统计局-统计用区划和城乡划分代码](https://www.stats.gov.cn/sj/tjbz/qhdm/)
    - [中华人民共和国国家统计局-统计用区划代码和城乡划分代码编制规则](https://www.stats.gov.cn/sj/tjbz/gjtjbz/202302/t20230213_1902741.html)
- 本项目已更新至
    - [2023年统计用区划代码和城乡划分代码（截止时间：2023-06-30，发布时间：2023-09-11）](https://www.stats.gov.cn/sj/tjbz/tjyqhdmhcxhfdm/2023/index.html)
- [百度地图](https://lbsyun.baidu.com/faq/api?title=webapi/download)

## 数据库支持
目前本项目数据保存在 Mysql ，数据文件下载：[govstat.sql](https://github.com/zz-open/china-administrative-division/blob/main/dist/govstat.sql)。

可以按需将数据迁移到其他数据库管理系统中（Sqlite, Oracle, MSSQL 等）。

## 数据下载
- 单独级别数据

| 文件列表 | JSON |	CSV |
|---|---|---|
| 省级(省份, 直辖市, 自治区) | [province.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/province.json) | [province.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/province.csv) |
| 市级(城市, 市区) | [city.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/city.json) | [city.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/city.csv) |
| 区级(区县, 县城) | [county.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/county.json) | [district.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/county.csv) |
| 乡级(乡镇、街道) | [town.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/town.json) | [street.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/town.csv) |
| 村级(村委会、居委会) | [village.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/village.json) | [village.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/village.csv) |

- 级联数据

| 文件列表 | 普通 |	带编码 |
|---|---|---|
| "省,市" 二级联动数据 | [pc.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pc.json) | [pc-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/pc-code.json) |
| "省,市,区" 三级联动数据 | [pcd.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcc.json) | [pcd-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcc-code.json) |
| "省,市,区,乡" 四级联动数据 | [pcds.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcct.json) | [pcds-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcct-code.json) |
| "省,市,区,乡,村" 五级联动数据 | [pcdsv.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcctv.json) | [pcdsv-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcctv-code.json) |

提示：需要打包下载全部文件，请看 Releases。
