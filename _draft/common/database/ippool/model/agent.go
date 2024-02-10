package model

type Agent struct {
	Id        int64  `json:"id" xorm:"id"`
	Name      string `json:"name" xorm:"name"`
	Website   string `json:"website" xorm:"website"`
	CreatedAt string `json:"created_at" xorm:"created_at"`
	UpdatedAt string `json:"updated_at" xorm:"updated_at"`
}
