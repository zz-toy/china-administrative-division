package main

import (
	"flag"
	"strings"

	"github.com/zeromicro/go-zero/core/conf"
	"gorm.io/driver/mysql"
	"gorm.io/gen"
	"gorm.io/gorm"
)

type Config struct {
	DataSource string
	QueryPath  string
}

var g *gen.Generator

func main() {

	var configFile = flag.String("f", "conf.yaml", "the config file")
	flag.Parse()

	var c Config
	conf.MustLoad(*configFile, &c)

	g = gen.NewGenerator(gen.Config{
		OutPath:          c.QueryPath,
		Mode:             gen.WithoutContext | gen.WithDefaultQuery | gen.WithQueryInterface,
		FieldWithTypeTag: true,
		FieldCoverable:   true,
		FieldNullable:    true,
	})

	gormDb, _ := gorm.Open(mysql.Open(c.DataSource))
	g.UseDB(gormDb)
	setDataType()

	g.ApplyBasic(g.GenerateAllTable()...)
	g.Execute()
}

func setDataType() {
	var dataMap = map[string]func(gorm.ColumnType) (dataType string){
		// int mapping
		"int": func(columnType gorm.ColumnType) (dataType string) {
			if n, ok := columnType.Nullable(); ok && n {
				return "*int64"
			}
			return "int64"
		},

		// tinyint mapping
		"tinyint": func(columnType gorm.ColumnType) (dataType string) {
			ct, _ := columnType.ColumnType()
			if strings.HasPrefix(ct, "tinyint(1)") {
				return "bool"
			}
			return "byte"
		},
	}

	g.WithDataTypeMap(dataMap)
}
