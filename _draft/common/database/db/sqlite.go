package db

import (
	_ "github.com/mattn/go-sqlite3"
	"xorm.io/xorm"
)

func NewSqliteEngine(dataSourceName string) (*xorm.Engine, error) {
	engine, err := xorm.NewEngine("sqlite3", dataSourceName)
	if err != nil {
		return nil, err
	}

	return engine, nil
}
