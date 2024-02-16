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

## 数据库支持
目前本项目数据保存在 Mysql ，数据文件下载：[govstat.sql](https://github.com/zz-open/china-administrative-division/blob/main/dist/govstat.sql)。

可以按需将数据迁移到其他数据库管理系统中（Sqlite, Oracle, MSSQL 等）。

## 数据下载
| 单级别数据 | 通用 | 前端 |
|---|---|---|
| 省级(省份, 直辖市, 自治区) | [province.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/province.json)<br>[province-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/province-code.json)<br>[province.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/province.csv)<br>[province-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/province-code.csv) | [province-ui.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/province-ui.json)<br>[province-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/province-ui-code.json)<br>[province-zn.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/province-zn.json)  |
| 市级(城市, 市区) | [city-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/city-code.json)<br>[city-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/city-code.csv) | [city-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/city-ui-code.json) |
| 区级(区县, 县城) | [county-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/county-code.json)<br>[county-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/county-code.csv) | [county-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/county-ui-code.json) |
| 乡级(乡镇、街道) | [town-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/town-code.json)<br>[town-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/town-code.csv) | [town-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/town-ui-code.json) |
| 村级(村委会、居委会) | [village-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/village-code.json)<br>[village-code.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/village-code.csv) | [village-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/village-ui-code.json) |


| 级联数据 | 通用 |	前端 |
|---|---|---|
| "省,市" 二级联动数据 | [pc.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pc.json)<br>[pc-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pc-code.json) | [pc-ui.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pc-ui.json)<br>[pc-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pc-ui-code.json)<br>[pc-zn.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pc-zn.json) |
| "省,市,区" 三级联动数据 | [pcc.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcc.json)<br>[pcc-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcc-code.json) | [pcc-ui.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcc-ui.json)<br>[pcc-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcc-ui-code.json)<br>[pcc-zn.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcc-zn.json) |
| "省,市,区,乡" 四级联动数据 | [pcct.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcct.json)<br>[pcct-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcct-code.json) | [pcct-ui.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcct-ui.json)<br>[pcct-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcct-ui-code.json) |
| "省,市,区,乡,村" 五级联动数据 | [pcctv.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcctv.json)<br>[pcctv-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcctv-code.json) | [pcctv-ui.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcctv-ui.json)<br>[pcctv-ui-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/pcctv-ui-code.json) |

提示：需要打包下载全部文件，请看 Releases。

[清洗规则](./FAQ.md)