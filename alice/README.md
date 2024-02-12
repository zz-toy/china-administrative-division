# alice
- [go-zero](https://github.com/zeromicro/go-zero)

基于 go-zero 搭建的 行政区划数据 http 服务

## 说明
api只提供最原始的数据，如果有字段改名等需求，通过接口返回的数据自行处理。

## 开发环境
```shell
# 安装 goctl
go install github.com/zeromicro/go-zero/tools/goctl@latest

# 安装其他依赖
go get github.com/duke-git/lancet/v2
go get -u gorm.io/gen
go install gorm.io/gen/tools/gentool@latest


# 创建服务
goctl api new alice

# 运行服务
go run alice.go
```

## api列表
建议使用id参数，因为地方名称可能会重复

### 单级别数据
#### 省 list
GET /province/list
- [可选参数] name string 省名称
```json
{

}
```

#### 城市 list
GET /city/list
- [可选参数] name string 城市名称
- [可选参数] province_id int province表的主键id
- [可选参数] province_name string 省名称

```json
{

}
```

#### 区县 list
GET /county/list
- [可选参数] province_id int province表的主键id
- [可选参数] city_id int city表的主键id
- [可选参数] name string 区县名称
- [可选参数] province_name string 省名称
- [可选参数] city_name string 城市名称

```json
{

}
```

#### 乡镇 list
GET /town/list
- [可选参数] province_id int province表的主键id
- [可选参数] city_id int city表的主键id
- [可选参数] county_id int county表的主键id
- [可选参数] name string 乡镇名称

```json
{

}
```

#### 村庄 list
GET /village/list
- [可选参数] province_id int province表的主键id
- [可选参数] city_id int city表的主键id
- [可选参数] county_id int county表的主键id
- [可选参数] town_id int town表的主键id
- [可选参数] name string 村庄名称

```json
{

}
```

### 级联数据
#### 省市联动
GET /pc/list
#### 省市区联动
GET /pcc/list
#### 省市区乡镇联动
GET /pcct/list
#### 省市区乡镇村庄联动
GET /pcctv/list