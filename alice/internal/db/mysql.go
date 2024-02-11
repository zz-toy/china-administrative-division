package db

import (
	"alice/dao/query"
	"alice/internal/config"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

func NewGormMysqlDB(c config.Config) *gorm.DB {
	db, err := gorm.Open(mysql.Open(c.Mysql.DataSource), &gorm.Config{
		Logger:                                   NewGormLogger(c),
		SkipDefaultTransaction:                   true,
		DisableForeignKeyConstraintWhenMigrating: true,
	})

	if err != nil {
		panic("failed to connect mysql")
	}

	query.SetDefault(db)

	return db
}
