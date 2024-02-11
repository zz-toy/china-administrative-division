package query

import (
	"alice/dao/model"
	"context"
	"strings"

	"github.com/duke-git/lancet/v2/convertor"
	"github.com/zeromicro/go-zero/core/stores/builder"
	"gorm.io/gen"
	"gorm.io/gorm"
)

var (
	cityFieldNames = builder.RawFieldNames(&model.City{})
	cityRows       = strings.Join(cityFieldNames, ",")
)

var _ CityModel = (*customCityModel)(nil)

type (
	CityModel interface {
		List(ctx context.Context) ([]*model.City, error)
		ListByConditionQuery(ctx context.Context, name string, provinceIds []int64) ([]*model.City, error)
		IdsByName(ctx context.Context, name string) ([]int64, error)
		ListByProvinceId(ctx context.Context, provinceId int64) ([]*model.City, error)
		ToIdMap(ctx context.Context, list []*model.City) map[int64]*model.City
		ListByIds(ctx context.Context, ids []int64) ([]*model.City, error)
		IdMapByIds(ctx context.Context, ids []int64) (map[int64]*model.City, error)
	}

	customCityModel struct {
		Dao *city
	}
)

func NewCityModel(db *gorm.DB, opts ...gen.DOOption) CityModel {
	defaultDao := newCity(db, opts...)
	return &customCityModel{
		Dao: &defaultDao,
	}
}

func (c *customCityModel) List(ctx context.Context) ([]*model.City, error) {
	return c.Dao.WithContext(context.Background()).Select(c.Dao.ID).Find()
}

func (c *customCityModel) ListByConditionQuery(ctx context.Context, name string, provinceIds []int64) ([]*model.City, error) {
	do := c.Dao.WithContext(ctx)
	if name != "" {
		do = do.Where(c.Dao.Name.Eq(name))
	}

	if provinceIds != nil || len(provinceIds) > 0 {
		do = do.Where(c.Dao.ProvinceID.In(provinceIds...))
	}

	return do.Find()
}

func (c *customCityModel) IdsByName(ctx context.Context, name string) ([]int64, error) {
	if name == "" {
		return nil, nil
	}

	cities, err := c.Dao.WithContext(ctx).Select(c.Dao.ID).Where(c.Dao.Name.Eq(name)).Find()
	if err != nil {
		return nil, err
	}

	if cities == nil || len(cities) == 0 {
		return nil, nil
	}

	var cityIds []int64
	for _, v := range cities {
		cityIds = append(cityIds, v.ID)
	}

	return cityIds, nil
}

func (c *customCityModel) ListByProvinceId(ctx context.Context, provinceId int64) ([]*model.City, error) {
	if provinceId <= 0 {
		return nil, nil
	}

	return c.Dao.WithContext(ctx).Where(c.Dao.ProvinceID.Eq(provinceId)).Find()
}

func (c *customCityModel) ToIdMap(ctx context.Context, list []*model.City) map[int64]*model.City {
	if list == nil || len(list) == 0 {
		return nil
	}

	return convertor.ToMap(list, func(city *model.City) (int64, *model.City) {
		return city.ID, city
	})
}

func (c *customCityModel) ListByIds(ctx context.Context, ids []int64) ([]*model.City, error) {
	if ids == nil || len(ids) == 0 {
		return nil, nil
	}

	return c.Dao.WithContext(context.Background()).Where(c.Dao.ID.In(ids...)).Find()
}

func (c *customCityModel) IdMapByIds(ctx context.Context, ids []int64) (map[int64]*model.City, error) {
	list, err := c.ListByIds(ctx, ids)
	if err != nil {
		return nil, err
	}

	return c.ToIdMap(ctx, list), nil
}
