package model

import "github.com/zeromicro/go-zero/core/stores/sqlx"

var _ VillageModel = (*customVillageModel)(nil)

type (
	// VillageModel is an interface to be customized, add more methods here,
	// and implement the added methods in customVillageModel.
	VillageModel interface {
		villageModel
		withSession(session sqlx.Session) VillageModel
	}

	customVillageModel struct {
		*defaultVillageModel
	}
)

// NewVillageModel returns a model for the database table.
func NewVillageModel(conn sqlx.SqlConn) VillageModel {
	return &customVillageModel{
		defaultVillageModel: newVillageModel(conn),
	}
}

func (m *customVillageModel) withSession(session sqlx.Session) VillageModel {
	return NewVillageModel(sqlx.NewSqlConnFromSession(session))
}
