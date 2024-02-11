package query

import (
	"alice/dao/model"
	"context"
	"strconv"
	"strings"

	"github.com/duke-git/lancet/v2/convertor"
	"github.com/zeromicro/go-zero/core/stores/builder"
	"gorm.io/gen"
	"gorm.io/gorm"
)

var (
	provinceFieldNames = builder.RawFieldNames(&model.Province{})
	provinceRows       = strings.Join(provinceFieldNames, ",")
)

var _ ProvinceModel = (*customProvinceModel)(nil)

type (
	ProvinceModel interface {
		List(ctx context.Context) ([]*model.Province, error)
		ListByConditionQuery(ctx context.Context, name string, isMunicipality string) ([]*model.Province, error)
		IdsByName(ctx context.Context, name string) ([]int64, error)
		ToIdMap(ctx context.Context, list []*model.Province) map[int64]*model.Province
		ListByIds(ctx context.Context, ids []int64) ([]*model.Province, error)
		IdMapByIds(ctx context.Context, ids []int64) (map[int64]*model.Province, error)
	}

	customProvinceModel struct {
		Dao *province
	}
)

func NewProvinceModel(db *gorm.DB, opts ...gen.DOOption) ProvinceModel {
	defaultDao := newProvince(db, opts...)
	return &customProvinceModel{
		Dao: &defaultDao,
	}
}

func (c *customProvinceModel) List(ctx context.Context) ([]*model.Province, error) {
	return c.Dao.WithContext(context.Background()).Select(c.Dao.ID).Find()
}

func (c *customProvinceModel) ListByConditionQuery(ctx context.Context, name string, isMunicipality string) ([]*model.Province, error) {
	do := c.Dao.WithContext(ctx)
	if name != "" {
		do = do.Where(c.Dao.Name.Eq(name))
	}

	if isMunicipality != "" {
		IsMunicipalityBool, err := strconv.ParseBool(isMunicipality)
		if err != nil {
			return nil, err
		}

		do = do.Where(c.Dao.IsMunicipality.Is(IsMunicipalityBool))
	}

	return do.Find()
}

func (c *customProvinceModel) IdsByName(ctx context.Context, name string) ([]int64, error) {
	if name == "" {
		return nil, nil
	}

	provinces, err := c.Dao.WithContext(ctx).Select(c.Dao.ID).Where(c.Dao.Name.Eq(name)).Find()
	if err != nil {
		return nil, err
	}

	if provinces == nil || len(provinces) == 0 {
		return nil, nil
	}

	var provinceIds []int64
	for _, v := range provinces {
		provinceIds = append(provinceIds, v.ID)
	}

	return provinceIds, nil
}

func (c *customProvinceModel) ToIdMap(ctx context.Context, list []*model.Province) map[int64]*model.Province {
	if list == nil || len(list) == 0 {
		return nil
	}

	return convertor.ToMap(list, func(province *model.Province) (int64, *model.Province) {
		return province.ID, province
	})
}

func (c *customProvinceModel) ListByIds(ctx context.Context, ids []int64) ([]*model.Province, error) {
	if ids == nil || len(ids) == 0 {
		return nil, nil
	}

	return c.Dao.WithContext(context.Background()).Where(c.Dao.ID.In(ids...)).Find()
}

func (c *customProvinceModel) IdMapByIds(ctx context.Context, ids []int64) (map[int64]*model.Province, error) {
	list, err := c.ListByIds(ctx, ids)
	if err != nil {
		return nil, err
	}

	return c.ToIdMap(ctx, list), nil
}
