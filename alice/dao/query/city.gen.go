// Code generated by gorm.io/gen. DO NOT EDIT.
// Code generated by gorm.io/gen. DO NOT EDIT.
// Code generated by gorm.io/gen. DO NOT EDIT.

package query

import (
	"context"

	"gorm.io/gorm"
	"gorm.io/gorm/clause"
	"gorm.io/gorm/schema"

	"gorm.io/gen"
	"gorm.io/gen/field"

	"gorm.io/plugin/dbresolver"

	"alice/dao/model"
)

func newCity(db *gorm.DB, opts ...gen.DOOption) city {
	_city := city{}

	_city.cityDo.UseDB(db, opts...)
	_city.cityDo.UseModel(&model.City{})

	tableName := _city.cityDo.TableName()
	_city.ALL = field.NewAsterisk(tableName)
	_city.ID = field.NewInt64(tableName, "id")
	_city.Name = field.NewString(tableName, "name")
	_city.Code = field.NewString(tableName, "code")
	_city.FullCode = field.NewString(tableName, "full_code")
	_city.ProvinceID = field.NewInt64(tableName, "province_id")
	_city.URL = field.NewString(tableName, "url")
	_city.ChildURL = field.NewString(tableName, "child_url")
	_city.Creator = field.NewString(tableName, "creator")
	_city.Updater = field.NewString(tableName, "updater")
	_city.CreatedAt = field.NewTime(tableName, "created_at")
	_city.UpdatedAt = field.NewTime(tableName, "updated_at")
	_city.DataUpdatedAt = field.NewTime(tableName, "data_updated_at")

	_city.fillFieldMap()

	return _city
}

// city 城市表
type city struct {
	cityDo

	ALL           field.Asterisk
	ID            field.Int64
	Name          field.String // 城市名称
	Code          field.String // 地级代码
	FullCode      field.String // 统计用区划代码
	ProvinceID    field.Int64  // province表id字段
	URL           field.String // 被抓取的url
	ChildURL      field.String // 指向的子url
	Creator       field.String // 创建者
	Updater       field.String // 更新者
	CreatedAt     field.Time   // 创建时间
	UpdatedAt     field.Time   // 更新时间
	DataUpdatedAt field.Time   // 更新时间

	fieldMap map[string]field.Expr
}

func (c city) Table(newTableName string) *city {
	c.cityDo.UseTable(newTableName)
	return c.updateTableName(newTableName)
}

func (c city) As(alias string) *city {
	c.cityDo.DO = *(c.cityDo.As(alias).(*gen.DO))
	return c.updateTableName(alias)
}

func (c *city) updateTableName(table string) *city {
	c.ALL = field.NewAsterisk(table)
	c.ID = field.NewInt64(table, "id")
	c.Name = field.NewString(table, "name")
	c.Code = field.NewString(table, "code")
	c.FullCode = field.NewString(table, "full_code")
	c.ProvinceID = field.NewInt64(table, "province_id")
	c.URL = field.NewString(table, "url")
	c.ChildURL = field.NewString(table, "child_url")
	c.Creator = field.NewString(table, "creator")
	c.Updater = field.NewString(table, "updater")
	c.CreatedAt = field.NewTime(table, "created_at")
	c.UpdatedAt = field.NewTime(table, "updated_at")
	c.DataUpdatedAt = field.NewTime(table, "data_updated_at")

	c.fillFieldMap()

	return c
}

func (c *city) GetFieldByName(fieldName string) (field.OrderExpr, bool) {
	_f, ok := c.fieldMap[fieldName]
	if !ok || _f == nil {
		return nil, false
	}
	_oe, ok := _f.(field.OrderExpr)
	return _oe, ok
}

func (c *city) fillFieldMap() {
	c.fieldMap = make(map[string]field.Expr, 12)
	c.fieldMap["id"] = c.ID
	c.fieldMap["name"] = c.Name
	c.fieldMap["code"] = c.Code
	c.fieldMap["full_code"] = c.FullCode
	c.fieldMap["province_id"] = c.ProvinceID
	c.fieldMap["url"] = c.URL
	c.fieldMap["child_url"] = c.ChildURL
	c.fieldMap["creator"] = c.Creator
	c.fieldMap["updater"] = c.Updater
	c.fieldMap["created_at"] = c.CreatedAt
	c.fieldMap["updated_at"] = c.UpdatedAt
	c.fieldMap["data_updated_at"] = c.DataUpdatedAt
}

func (c city) clone(db *gorm.DB) city {
	c.cityDo.ReplaceConnPool(db.Statement.ConnPool)
	return c
}

func (c city) replaceDB(db *gorm.DB) city {
	c.cityDo.ReplaceDB(db)
	return c
}

type cityDo struct{ gen.DO }

type ICityDo interface {
	gen.SubQuery
	Debug() ICityDo
	WithContext(ctx context.Context) ICityDo
	WithResult(fc func(tx gen.Dao)) gen.ResultInfo
	ReplaceDB(db *gorm.DB)
	ReadDB() ICityDo
	WriteDB() ICityDo
	As(alias string) gen.Dao
	Session(config *gorm.Session) ICityDo
	Columns(cols ...field.Expr) gen.Columns
	Clauses(conds ...clause.Expression) ICityDo
	Not(conds ...gen.Condition) ICityDo
	Or(conds ...gen.Condition) ICityDo
	Select(conds ...field.Expr) ICityDo
	Where(conds ...gen.Condition) ICityDo
	Order(conds ...field.Expr) ICityDo
	Distinct(cols ...field.Expr) ICityDo
	Omit(cols ...field.Expr) ICityDo
	Join(table schema.Tabler, on ...field.Expr) ICityDo
	LeftJoin(table schema.Tabler, on ...field.Expr) ICityDo
	RightJoin(table schema.Tabler, on ...field.Expr) ICityDo
	Group(cols ...field.Expr) ICityDo
	Having(conds ...gen.Condition) ICityDo
	Limit(limit int) ICityDo
	Offset(offset int) ICityDo
	Count() (count int64, err error)
	Scopes(funcs ...func(gen.Dao) gen.Dao) ICityDo
	Unscoped() ICityDo
	Create(values ...*model.City) error
	CreateInBatches(values []*model.City, batchSize int) error
	Save(values ...*model.City) error
	First() (*model.City, error)
	Take() (*model.City, error)
	Last() (*model.City, error)
	Find() ([]*model.City, error)
	FindInBatch(batchSize int, fc func(tx gen.Dao, batch int) error) (results []*model.City, err error)
	FindInBatches(result *[]*model.City, batchSize int, fc func(tx gen.Dao, batch int) error) error
	Pluck(column field.Expr, dest interface{}) error
	Delete(...*model.City) (info gen.ResultInfo, err error)
	Update(column field.Expr, value interface{}) (info gen.ResultInfo, err error)
	UpdateSimple(columns ...field.AssignExpr) (info gen.ResultInfo, err error)
	Updates(value interface{}) (info gen.ResultInfo, err error)
	UpdateColumn(column field.Expr, value interface{}) (info gen.ResultInfo, err error)
	UpdateColumnSimple(columns ...field.AssignExpr) (info gen.ResultInfo, err error)
	UpdateColumns(value interface{}) (info gen.ResultInfo, err error)
	UpdateFrom(q gen.SubQuery) gen.Dao
	Attrs(attrs ...field.AssignExpr) ICityDo
	Assign(attrs ...field.AssignExpr) ICityDo
	Joins(fields ...field.RelationField) ICityDo
	Preload(fields ...field.RelationField) ICityDo
	FirstOrInit() (*model.City, error)
	FirstOrCreate() (*model.City, error)
	FindByPage(offset int, limit int) (result []*model.City, count int64, err error)
	ScanByPage(result interface{}, offset int, limit int) (count int64, err error)
	Scan(result interface{}) (err error)
	Returning(value interface{}, columns ...string) ICityDo
	UnderlyingDB() *gorm.DB
	schema.Tabler
}

func (c cityDo) Debug() ICityDo {
	return c.withDO(c.DO.Debug())
}

func (c cityDo) WithContext(ctx context.Context) ICityDo {
	return c.withDO(c.DO.WithContext(ctx))
}

func (c cityDo) ReadDB() ICityDo {
	return c.Clauses(dbresolver.Read)
}

func (c cityDo) WriteDB() ICityDo {
	return c.Clauses(dbresolver.Write)
}

func (c cityDo) Session(config *gorm.Session) ICityDo {
	return c.withDO(c.DO.Session(config))
}

func (c cityDo) Clauses(conds ...clause.Expression) ICityDo {
	return c.withDO(c.DO.Clauses(conds...))
}

func (c cityDo) Returning(value interface{}, columns ...string) ICityDo {
	return c.withDO(c.DO.Returning(value, columns...))
}

func (c cityDo) Not(conds ...gen.Condition) ICityDo {
	return c.withDO(c.DO.Not(conds...))
}

func (c cityDo) Or(conds ...gen.Condition) ICityDo {
	return c.withDO(c.DO.Or(conds...))
}

func (c cityDo) Select(conds ...field.Expr) ICityDo {
	return c.withDO(c.DO.Select(conds...))
}

func (c cityDo) Where(conds ...gen.Condition) ICityDo {
	return c.withDO(c.DO.Where(conds...))
}

func (c cityDo) Order(conds ...field.Expr) ICityDo {
	return c.withDO(c.DO.Order(conds...))
}

func (c cityDo) Distinct(cols ...field.Expr) ICityDo {
	return c.withDO(c.DO.Distinct(cols...))
}

func (c cityDo) Omit(cols ...field.Expr) ICityDo {
	return c.withDO(c.DO.Omit(cols...))
}

func (c cityDo) Join(table schema.Tabler, on ...field.Expr) ICityDo {
	return c.withDO(c.DO.Join(table, on...))
}

func (c cityDo) LeftJoin(table schema.Tabler, on ...field.Expr) ICityDo {
	return c.withDO(c.DO.LeftJoin(table, on...))
}

func (c cityDo) RightJoin(table schema.Tabler, on ...field.Expr) ICityDo {
	return c.withDO(c.DO.RightJoin(table, on...))
}

func (c cityDo) Group(cols ...field.Expr) ICityDo {
	return c.withDO(c.DO.Group(cols...))
}

func (c cityDo) Having(conds ...gen.Condition) ICityDo {
	return c.withDO(c.DO.Having(conds...))
}

func (c cityDo) Limit(limit int) ICityDo {
	return c.withDO(c.DO.Limit(limit))
}

func (c cityDo) Offset(offset int) ICityDo {
	return c.withDO(c.DO.Offset(offset))
}

func (c cityDo) Scopes(funcs ...func(gen.Dao) gen.Dao) ICityDo {
	return c.withDO(c.DO.Scopes(funcs...))
}

func (c cityDo) Unscoped() ICityDo {
	return c.withDO(c.DO.Unscoped())
}

func (c cityDo) Create(values ...*model.City) error {
	if len(values) == 0 {
		return nil
	}
	return c.DO.Create(values)
}

func (c cityDo) CreateInBatches(values []*model.City, batchSize int) error {
	return c.DO.CreateInBatches(values, batchSize)
}

// Save : !!! underlying implementation is different with GORM
// The method is equivalent to executing the statement: db.Clauses(clause.OnConflict{UpdateAll: true}).Create(values)
func (c cityDo) Save(values ...*model.City) error {
	if len(values) == 0 {
		return nil
	}
	return c.DO.Save(values)
}

func (c cityDo) First() (*model.City, error) {
	if result, err := c.DO.First(); err != nil {
		return nil, err
	} else {
		return result.(*model.City), nil
	}
}

func (c cityDo) Take() (*model.City, error) {
	if result, err := c.DO.Take(); err != nil {
		return nil, err
	} else {
		return result.(*model.City), nil
	}
}

func (c cityDo) Last() (*model.City, error) {
	if result, err := c.DO.Last(); err != nil {
		return nil, err
	} else {
		return result.(*model.City), nil
	}
}

func (c cityDo) Find() ([]*model.City, error) {
	result, err := c.DO.Find()
	return result.([]*model.City), err
}

func (c cityDo) FindInBatch(batchSize int, fc func(tx gen.Dao, batch int) error) (results []*model.City, err error) {
	buf := make([]*model.City, 0, batchSize)
	err = c.DO.FindInBatches(&buf, batchSize, func(tx gen.Dao, batch int) error {
		defer func() { results = append(results, buf...) }()
		return fc(tx, batch)
	})
	return results, err
}

func (c cityDo) FindInBatches(result *[]*model.City, batchSize int, fc func(tx gen.Dao, batch int) error) error {
	return c.DO.FindInBatches(result, batchSize, fc)
}

func (c cityDo) Attrs(attrs ...field.AssignExpr) ICityDo {
	return c.withDO(c.DO.Attrs(attrs...))
}

func (c cityDo) Assign(attrs ...field.AssignExpr) ICityDo {
	return c.withDO(c.DO.Assign(attrs...))
}

func (c cityDo) Joins(fields ...field.RelationField) ICityDo {
	for _, _f := range fields {
		c = *c.withDO(c.DO.Joins(_f))
	}
	return &c
}

func (c cityDo) Preload(fields ...field.RelationField) ICityDo {
	for _, _f := range fields {
		c = *c.withDO(c.DO.Preload(_f))
	}
	return &c
}

func (c cityDo) FirstOrInit() (*model.City, error) {
	if result, err := c.DO.FirstOrInit(); err != nil {
		return nil, err
	} else {
		return result.(*model.City), nil
	}
}

func (c cityDo) FirstOrCreate() (*model.City, error) {
	if result, err := c.DO.FirstOrCreate(); err != nil {
		return nil, err
	} else {
		return result.(*model.City), nil
	}
}

func (c cityDo) FindByPage(offset int, limit int) (result []*model.City, count int64, err error) {
	result, err = c.Offset(offset).Limit(limit).Find()
	if err != nil {
		return
	}

	if size := len(result); 0 < limit && 0 < size && size < limit {
		count = int64(size + offset)
		return
	}

	count, err = c.Offset(-1).Limit(-1).Count()
	return
}

func (c cityDo) ScanByPage(result interface{}, offset int, limit int) (count int64, err error) {
	count, err = c.Count()
	if err != nil {
		return
	}

	err = c.Offset(offset).Limit(limit).Scan(result)
	return
}

func (c cityDo) Scan(result interface{}) (err error) {
	return c.DO.Scan(result)
}

func (c cityDo) Delete(models ...*model.City) (result gen.ResultInfo, err error) {
	return c.DO.Delete(models)
}

func (c *cityDo) withDO(do gen.Dao) *cityDo {
	c.DO = *do.(*gen.DO)
	return c
}
