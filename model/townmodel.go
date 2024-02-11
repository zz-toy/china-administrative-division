package model

import "github.com/zeromicro/go-zero/core/stores/sqlx"

var _ TownModel = (*customTownModel)(nil)

type (
	// TownModel is an interface to be customized, add more methods here,
	// and implement the added methods in customTownModel.
	TownModel interface {
		townModel
		withSession(session sqlx.Session) TownModel
	}

	customTownModel struct {
		*defaultTownModel
	}
)

// NewTownModel returns a model for the database table.
func NewTownModel(conn sqlx.SqlConn) TownModel {
	return &customTownModel{
		defaultTownModel: newTownModel(conn),
	}
}

func (m *customTownModel) withSession(session sqlx.Session) TownModel {
	return NewTownModel(sqlx.NewSqlConnFromSession(session))
}
