// Code generated by gorm.io/gen. DO NOT EDIT.
// Code generated by gorm.io/gen. DO NOT EDIT.
// Code generated by gorm.io/gen. DO NOT EDIT.

package model

import (
	"time"
)

const TableNameCounty = "county"

// County 县城表
type County struct {
	ID            int32     `gorm:"column:id;primaryKey;autoIncrement:true" json:"id"`
	Name          string    `gorm:"column:name;not null;comment:县名称" json:"name"`                                                    // 县名称
	Code          string    `gorm:"column:code;not null;comment:统计用区划代码" json:"code"`                                                // 统计用区划代码
	ProvinceID    int32     `gorm:"column:province_id;not null;comment:province表id字段" json:"province_id"`                            // province表id字段
	CityID        int32     `gorm:"column:city_id;not null;comment:city表id字段" json:"city_id"`                                        // city表id字段
	URL           string    `gorm:"column:url;not null;comment:被抓取的url" json:"url"`                                                  // 被抓取的url
	ChildURL      string    `gorm:"column:child_url;not null;comment:指向的子url" json:"child_url"`                                      // 指向的子url
	Creator       string    `gorm:"column:creator;not null;comment:创建者" json:"creator"`                                              // 创建者
	Updater       string    `gorm:"column:updater;not null;comment:更新者" json:"updater"`                                              // 更新者
	CreatedAt     time.Time `gorm:"column:created_at;not null;default:CURRENT_TIMESTAMP;comment:创建时间" json:"created_at"`             // 创建时间
	UpdatedAt     time.Time `gorm:"column:updated_at;not null;default:CURRENT_TIMESTAMP;comment:更新时间" json:"updated_at"`             // 更新时间
	DataUpdatedAt time.Time `gorm:"column:data_updated_at;not null;default:CURRENT_TIMESTAMP;comment:数据更新时间" json:"data_updated_at"` // 数据更新时间
}

// TableName County's table name
func (*County) TableName() string {
	return TableNameCounty
}
