package query

import (
	"alice/dao/model"
	"context"
	"strings"

	"github.com/zeromicro/go-zero/core/stores/builder"
	"gorm.io/gen"
	"gorm.io/gorm"
)

var (
	countyFieldNames = builder.RawFieldNames(&model.County{})
	countyRows       = strings.Join(countyFieldNames, ",")
)

var _ CountyModel = (*customCountyModel)(nil)

type (
	CountyModel interface {
		List(ctx context.Context) ([]*model.County, error)
		ListByConditionQuery(ctx context.Context, name string, provinceIds []int64, cityIds []int64) ([]*model.County, error)
		IdsByName(ctx context.Context, name string) ([]int64, error)
		ListByProvinceId(ctx context.Context, provinceId int64) ([]*model.County, error)
		ListByCityId(ctx context.Context, cityId int64) ([]*model.County, error)
	}

	customCountyModel struct {
		Dao *county
	}
)

func NewCountyModel(db *gorm.DB, opts ...gen.DOOption) CountyModel {
	defaultDao := newCounty(db, opts...)
	return &customCountyModel{
		Dao: &defaultDao,
	}
}

func (c *customCountyModel) List(ctx context.Context) ([]*model.County, error) {
	return c.Dao.WithContext(context.Background()).Select(c.Dao.ID).Find()
}

func (c *customCountyModel) ListByConditionQuery(ctx context.Context, name string, provinceIds []int64, cityIds []int64) ([]*model.County, error) {
	do := c.Dao.WithContext(ctx)
	if name != "" {
		do = do.Where(c.Dao.Name.Eq(name))
	}

	if provinceIds != nil || len(provinceIds) > 0 {
		do = do.Where(c.Dao.ProvinceID.In(provinceIds...))
	}

	if cityIds != nil || len(cityIds) > 0 {
		do = do.Where(c.Dao.CityID.In(cityIds...))
	}

	return do.Find()
}

func (c *customCountyModel) IdsByName(ctx context.Context, name string) ([]int64, error) {
	if name == "" {
		return nil, nil
	}

	counties, err := c.Dao.WithContext(ctx).Select(c.Dao.ID).Where(c.Dao.Name.Eq(name)).Find()
	if err != nil {
		return nil, err
	}

	if counties == nil || len(counties) == 0 {
		return nil, nil
	}

	var countyIds []int64
	for _, v := range counties {
		countyIds = append(countyIds, v.ID)
	}

	return countyIds, nil
}

func (c *customCountyModel) ListByProvinceId(ctx context.Context, provinceId int64) ([]*model.County, error) {
	if provinceId <= 0 {
		return nil, nil
	}

	return c.Dao.WithContext(ctx).Where(c.Dao.ProvinceID.Eq(provinceId)).Find()
}

func (c *customCountyModel) ListByCityId(ctx context.Context, cityId int64) ([]*model.County, error) {
	if cityId <= 0 {
		return nil, nil
	}

	return c.Dao.WithContext(ctx).Where(c.Dao.CityID.Eq(cityId)).Find()
}
