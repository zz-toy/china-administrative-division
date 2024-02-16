# china-administrative-division
中国行政区划数据

## 描述
中华人民共和国行政区划（四级）：省级、地级、县级、乡镇级。

该项目提供最新的省市区乡镇数据，方便业务升级。

港澳台数据暂无。

## 数据来源
- [百度地图](https://lbsyun.baidu.com/faq/api?title=webapi/download)

## 数据下载
| 单级别数据 | 通用格式 | 前端格式 |
|---|---|---|
| 省级(省份, 直辖市, 自治区) | [province-flatten.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/province-flatten.json)<br>[province-flatten.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/province-flatten.csv) | [province-cascade.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/province-cascade.json)|
| 市级(城市, 市区) | [city-flatten.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/city-flatten.json)<br>[city-flatten.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/city-flatten.csv) | [city-cascade.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/city-cascade.json) |
| 区级(区县, 县城) | [county-flatten.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/county-flatten.json)<br>[county-flatten.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/county-flatten.csv) | [county-cascade.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/county-cascade.json) |
| 乡级(乡镇、街道) | [town-flatten.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/town-flatten.json)<br>[town-flatten.csv](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/town-flatten.csv) | [town-cascade.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/town-cascade.json) |


| 级联数据 | 文件 |
|---|---|
| "省,市" 二级联动数据 | [pc.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/pc.json)<br>[pc-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/pc-code.json) |
| "省,市,区" 三级联动数据 | [pcc.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/pcc.json)<br>[pcc-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/pcc-code.json) |
| "省,市,区,乡" 四级联动数据 | [pcct.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/pcct.json)<br> [pcct-code.json](https://github.com/zz-open/china-administrative-division/blob/main/dist/bdmap/pcct-code.json) |

提示：需要打包下载全部文件，请看 Releases。