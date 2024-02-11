// Code generated by goctl. DO NOT EDIT.

package model

import (
	"context"
	"database/sql"
	"fmt"
	"strings"
	"time"

	"github.com/zeromicro/go-zero/core/stores/builder"
	"github.com/zeromicro/go-zero/core/stores/sqlx"
	"github.com/zeromicro/go-zero/core/stringx"
)

var (
	townFieldNames          = builder.RawFieldNames(&Town{})
	townRows                = strings.Join(townFieldNames, ",")
	townRowsExpectAutoSet   = strings.Join(stringx.Remove(townFieldNames, "`id`", "`create_at`", "`create_time`", "`created_at`", "`update_at`", "`update_time`", "`updated_at`"), ",")
	townRowsWithPlaceHolder = strings.Join(stringx.Remove(townFieldNames, "`id`", "`create_at`", "`create_time`", "`created_at`", "`update_at`", "`update_time`", "`updated_at`"), "=?,") + "=?"
)

type (
	townModel interface {
		Insert(ctx context.Context, data *Town) (sql.Result, error)
		FindOne(ctx context.Context, id int64) (*Town, error)
		Update(ctx context.Context, data *Town) error
		Delete(ctx context.Context, id int64) error
	}

	defaultTownModel struct {
		conn  sqlx.SqlConn
		table string
	}

	Town struct {
		Id            int64     `db:"id"`
		Name          string    `db:"name"`            // 乡镇名称
		Code          string    `db:"code"`            // 统计用区划代码
		ProvinceId    int64     `db:"province_id"`     // province表id字段
		CityId        int64     `db:"city_id"`         // city表id字段
		CountyId      int64     `db:"county_id"`       // county表id字段
		Url           string    `db:"url"`             // 被抓取的url
		ChildUrl      string    `db:"child_url"`       // 指向的子url
		Creator       string    `db:"creator"`         // 创建者
		Updater       string    `db:"updater"`         // 更新者
		CreatedAt     time.Time `db:"created_at"`      // 创建时间
		UpdatedAt     time.Time `db:"updated_at"`      // 更新时间
		DataUpdatedAt time.Time `db:"data_updated_at"` // 数据更新时间
	}
)

func newTownModel(conn sqlx.SqlConn) *defaultTownModel {
	return &defaultTownModel{
		conn:  conn,
		table: "`town`",
	}
}

func (m *defaultTownModel) Delete(ctx context.Context, id int64) error {
	query := fmt.Sprintf("delete from %s where `id` = ?", m.table)
	_, err := m.conn.ExecCtx(ctx, query, id)
	return err
}

func (m *defaultTownModel) FindOne(ctx context.Context, id int64) (*Town, error) {
	query := fmt.Sprintf("select %s from %s where `id` = ? limit 1", townRows, m.table)
	var resp Town
	err := m.conn.QueryRowCtx(ctx, &resp, query, id)
	switch err {
	case nil:
		return &resp, nil
	case sqlx.ErrNotFound:
		return nil, ErrNotFound
	default:
		return nil, err
	}
}

func (m *defaultTownModel) Insert(ctx context.Context, data *Town) (sql.Result, error) {
	query := fmt.Sprintf("insert into %s (%s) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", m.table, townRowsExpectAutoSet)
	ret, err := m.conn.ExecCtx(ctx, query, data.Name, data.Code, data.ProvinceId, data.CityId, data.CountyId, data.Url, data.ChildUrl, data.Creator, data.Updater, data.DataUpdatedAt)
	return ret, err
}

func (m *defaultTownModel) Update(ctx context.Context, data *Town) error {
	query := fmt.Sprintf("update %s set %s where `id` = ?", m.table, townRowsWithPlaceHolder)
	_, err := m.conn.ExecCtx(ctx, query, data.Name, data.Code, data.ProvinceId, data.CityId, data.CountyId, data.Url, data.ChildUrl, data.Creator, data.Updater, data.DataUpdatedAt, data.Id)
	return err
}

func (m *defaultTownModel) tableName() string {
	return m.table
}
