package svc

import (
	"alice/dao/query"
	"alice/internal/config"
	"alice/internal/db"
)

type ServiceContext struct {
	Config        config.Config
	ProvinceModel query.ProvinceModel
	CityModel     query.CityModel
	CountyModel   query.CountyModel
}

func NewServiceContext(c config.Config) *ServiceContext {
	gormDB := db.NewGormMysqlDB(c)

	return &ServiceContext{
		Config:        c,
		ProvinceModel: query.NewProvinceModel(gormDB),
		CityModel:     query.NewCityModel(gormDB),
		CountyModel:   query.NewCountyModel(gormDB),
	}
}
