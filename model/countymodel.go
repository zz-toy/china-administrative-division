package model

import (
	"context"
	"fmt"

	"github.com/duke-git/lancet/v2/slice"
	"github.com/zeromicro/go-zero/core/stores/sqlx"
)

var _ CountyModel = (*customCountyModel)(nil)

type (
	// CountyModel is an interface to be customized, add more methods here,
	// and implement the added methods in customCountyModel.
	CountyModel interface {
		countyModel
		withSession(session sqlx.Session) CountyModel
		List(ctx context.Context) ([]*County, error)
		ListByAndWhere(ctx context.Context, name string, provinceIds []int64, cityIds []int64) ([]*County, error)
		ListByProvinceId(ctx context.Context, provinceId int64) ([]*County, error)
		ListByCityId(ctx context.Context, cityId int64) ([]*County, error)
		IdsByName(ctx context.Context, name string) ([]int64, error)
	}

	customCountyModel struct {
		*defaultCountyModel
	}
)

// NewCountyModel returns a model for the database table.
func NewCountyModel(conn sqlx.SqlConn) CountyModel {
	return &customCountyModel{
		defaultCountyModel: newCountyModel(conn),
	}
}

func (m *customCountyModel) withSession(session sqlx.Session) CountyModel {
	return NewCountyModel(sqlx.NewSqlConnFromSession(session))
}

func (c *customCountyModel) List(ctx context.Context) ([]*County, error) {
	query := fmt.Sprintf("SELECT %s FROM %s ", countyRows, c.table)
	var resp []*County
	err := c.conn.QueryRowsCtx(ctx, &resp, query)
	return resp, err
}

func (c *customCountyModel) ListByAndWhere(ctx context.Context, name string, provinceIds []int64, cityIds []int64) ([]*County, error) {
	query := fmt.Sprintf("SELECT %s FROM %s WHERE 1=1", countyRows, c.table)
	args := make([]any, 0)
	if name != "" {
		query = fmt.Sprintf("%s AND name = ?", query)
		args = append(args, name)
	}

	if provinceIds != nil && len(provinceIds) > 0 {
		query = fmt.Sprintf("%s AND province_id in (?)", query)
		args = append(args, slice.Join(provinceIds, ","))
	}

	if cityIds != nil && len(cityIds) > 0 {
		query = fmt.Sprintf("%s AND city_id in (?)", query)
		args = append(args, slice.Join(cityIds, ","))
	}

	var resp []*County
	err := c.conn.QueryRowsCtx(ctx, &resp, query, args...)
	return resp, err
}

func (c *customCountyModel) ListByProvinceId(ctx context.Context, provinceId int64) ([]*County, error) {
	if provinceId <= 0 {
		return nil, nil
	}

	query := fmt.Sprintf("SELECT %s FROM %s WHERE province_id = ?", countyRows, c.table)
	var resp []*County
	err := c.conn.QueryRowsCtx(ctx, &resp, query, provinceId)
	return resp, err
}

func (c *customCountyModel) ListByCityId(ctx context.Context, cityId int64) ([]*County, error) {
	if cityId <= 0 {
		return nil, nil
	}

	query := fmt.Sprintf("SELECT %s FROM %s WHERE city_id = ?", countyRows, c.table)
	var resp []*County
	err := c.conn.QueryRowsCtx(ctx, &resp, query, cityId)
	return resp, err
}

func (c *customCountyModel) IdsByName(ctx context.Context, name string) ([]int64, error) {
	if name == "" {
		return nil, nil
	}

	query := fmt.Sprintf("SELECT id FROM %s WHERE name = ?", c.table)
	var resp []int64
	err := c.conn.QueryRowsCtx(ctx, &resp, query, name)
	return resp, err
}
