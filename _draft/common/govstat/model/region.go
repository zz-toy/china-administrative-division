package model

type Region struct {
	Id        int64  `json:"id" xorm:"id"`
	Province  string `json:"province" xorm:"province"`
	City      string `json:"city" xorm:"city"`
	District  string `json:"district" xorm:"district"`
	Street    string `json:"street" xorm:"street"`
	Village   string `json:"village" xorm:"village"`
	CreatedAt string `json:"created_at" xorm:"created_at"`
	UpdatedAt string `json:"updated_at" xorm:"updated_at"`
}
