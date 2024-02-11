package model

import (
	"context"
	"fmt"
	"strconv"

	"github.com/zeromicro/go-zero/core/stores/sqlx"
)

var _ ProvinceModel = (*customProvinceModel)(nil)

type (
	// ProvinceModel is an interface to be customized, add more methods here,
	// and implement the added methods in customProvinceModel.
	ProvinceModel interface {
		provinceModel
		withSession(session sqlx.Session) ProvinceModel
		List(ctx context.Context) ([]*Province, error)
		ListByAndWhere(ctx context.Context, name string, isMunicipality string) ([]*Province, error)
		IdsByName(ctx context.Context, name string) ([]int64, error)
	}

	customProvinceModel struct {
		*defaultProvinceModel
	}
)

// NewProvinceModel returns a model for the database table.
func NewProvinceModel(conn sqlx.SqlConn) ProvinceModel {
	return &customProvinceModel{
		defaultProvinceModel: newProvinceModel(conn),
	}
}

func (m *customProvinceModel) withSession(session sqlx.Session) ProvinceModel {
	return NewProvinceModel(sqlx.NewSqlConnFromSession(session))
}

func (c *customProvinceModel) List(ctx context.Context) ([]*Province, error) {
	query := fmt.Sprintf("SELECT %s FROM %s ", provinceRows, c.table)
	var resp []*Province
	err := c.conn.QueryRowsCtx(ctx, &resp, query)
	return resp, err
}

func (c *customProvinceModel) ListByAndWhere(ctx context.Context, name string, isMunicipality string) ([]*Province, error) {
	query := fmt.Sprintf("SELECT %s FROM %s WHERE 1=1", provinceRows, c.table)
	args := make([]any, 0)
	if name != "" {
		query = fmt.Sprintf("%s AND name = ?", query)
		args = append(args, name)
	}

	if isMunicipality != "" {
		query = fmt.Sprintf("%s AND is_municipality = ?", query)
		isMunicipalityNumber, err := strconv.Atoi(isMunicipality)
		if err != nil {
			return nil, err
		}

		args = append(args, isMunicipalityNumber)
	}

	var resp []*Province
	err := c.conn.QueryRowsCtx(ctx, &resp, query, args...)
	return resp, err
}

func (c *customProvinceModel) IdsByName(ctx context.Context, name string) ([]int64, error) {
	if name == "" {
		return nil, nil
	}

	query := fmt.Sprintf("SELECT id FROM %s WHERE name = ?", c.table)
	var resp []int64
	err := c.conn.QueryRowsCtx(ctx, &resp, query, name)
	return resp, err
}
