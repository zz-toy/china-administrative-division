package model

import (
	"context"
	"fmt"

	"github.com/duke-git/lancet/v2/slice"
	"github.com/zeromicro/go-zero/core/stores/sqlx"
)

var _ CityModel = (*customCityModel)(nil)

type (
	// CityModel is an interface to be customized, add more methods here,
	// and implement the added methods in customCityModel.
	CityModel interface {
		cityModel
		withSession(session sqlx.Session) CityModel
		List(ctx context.Context) ([]*City, error)
		ListByAndWhere(ctx context.Context, name string, provinceIds []int64) ([]*City, error)
		ListByProvinceId(ctx context.Context, provinceId int64) ([]*City, error)
		IdsByName(ctx context.Context, name string) ([]int64, error)
	}

	customCityModel struct {
		*defaultCityModel
	}
)

// NewCityModel returns a model for the database table.
func NewCityModel(conn sqlx.SqlConn) CityModel {
	return &customCityModel{
		defaultCityModel: newCityModel(conn),
	}
}

func (m *customCityModel) withSession(session sqlx.Session) CityModel {
	return NewCityModel(sqlx.NewSqlConnFromSession(session))
}

func (c *customCityModel) List(ctx context.Context) ([]*City, error) {
	query := fmt.Sprintf("SELECT %s FROM %s ", cityRows, c.table)
	var resp []*City
	err := c.conn.QueryRowsCtx(ctx, &resp, query)
	return resp, err
}

func (c *customCityModel) ListByAndWhere(ctx context.Context, name string, provinceIds []int64) ([]*City, error) {
	query := fmt.Sprintf("SELECT %s FROM %s WHERE 1=1", cityRows, c.table)
	args := make([]any, 0)
	if name != "" {
		query = fmt.Sprintf("%s AND name = ?", query)
		args = append(args, name)
	}

	if provinceIds != nil && len(provinceIds) > 0 {
		query = fmt.Sprintf("%s AND province_id in (?)", query)
		args = append(args, slice.Join(provinceIds, ","))
	}

	var resp []*City
	err := c.conn.QueryRowsCtx(ctx, &resp, query, args...)
	return resp, err
}

func (c *customCityModel) ListByProvinceId(ctx context.Context, provinceId int64) ([]*City, error) {
	if provinceId <= 0 {
		return nil, nil
	}

	query := fmt.Sprintf("SELECT %s FROM %s WHERE province_id = ?", cityRows, c.table)
	var resp []*City
	err := c.conn.QueryRowsCtx(ctx, &resp, query, provinceId)
	return resp, err
}

func (c *customCityModel) IdsByName(ctx context.Context, name string) ([]int64, error) {
	if name == "" {
		return nil, nil
	}

	query := fmt.Sprintf("SELECT id FROM %s WHERE name = ?", c.table)
	var resp []int64
	err := c.conn.QueryRowsCtx(ctx, &resp, query, name)
	return resp, err
}
