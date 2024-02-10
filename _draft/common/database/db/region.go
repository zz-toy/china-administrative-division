package db

import (
	"sync"

	"xorm.io/xorm"
)

var (
	regionEngine *xorm.Engine
	once         sync.Once
)

func GetRegionEngine() *xorm.Engine {
	once.Do(func() {
		regionEngine, _ = NewSqliteEngine("../storage/region.sqlite3")
	})

	return regionEngine
}
