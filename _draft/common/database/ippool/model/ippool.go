package model

type IpPool struct {
	Id        int64  `json:"id" xorm:"id"`
	Ip        string `json:"ip" xorm:"ip"`
	Port      string `json:"port" xorm:"port"`
	Status    int    `json:"status" xorm:"status"`
	AgentId   string `json:"agent_id" xorm:"agent_id"`
	CreatedAt string `json:"created_at" xorm:"created_at"`
	UpdatedAt string `json:"updated_at" xorm:"updated_at"`
}
