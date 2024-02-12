package pcc

import (
	"context"
	"time"

	"alice/internal/config"
	"alice/internal/svc"
	"alice/internal/types"

	"github.com/zeromicro/go-zero/core/logx"
)

type ListLogic struct {
	logx.Logger
	ctx    context.Context
	svcCtx *svc.ServiceContext
}

func NewListLogic(ctx context.Context, svcCtx *svc.ServiceContext) *ListLogic {
	return &ListLogic{
		Logger: logx.WithContext(ctx),
		ctx:    ctx,
		svcCtx: svcCtx,
	}
}

func (l *ListLogic) List(req *types.PCCListRequest) (resp *types.PCCListResponse, err error) {
	resp = &types.PCCListResponse{
		BaseResponse: types.SuccessResponse(),
		Data:         make([]*types.ProvinceItem, 0),
	}

	// 根据条件查询province表
	provinces, err := l.svcCtx.ProvinceModel.ListByConditionQuery(l.ctx, req.Name, req.IsMunicipality)
	if err != nil {
		return nil, types.SearchFailError
	}

	if provinces == nil || len(provinces) == 0 {
		return resp, nil
	}

	// province list 转 map
	provinceIdMap := l.svcCtx.ProvinceModel.ToIdMap(l.ctx, provinces)
	if provinceIdMap == nil {
		return resp, nil
	}

	var provinceIds []int64
	for _, v := range provinces {
		provinceIds = append(provinceIds, v.ID)
	}

	// 通过province_id 查询 city 表
	cities, err := l.svcCtx.CityModel.ListByProvinceIds(l.ctx, provinceIds)
	if err != nil {
		return nil, types.SearchFailError
	}

	// city list 转 map
	cityIdMap := l.svcCtx.CityModel.ToIdMap(l.ctx, cities)
	if cityIdMap == nil {
		return resp, nil
	}

	// 查询county 表
	counties, err := l.svcCtx.CountyModel.ListByProvinceIds(l.ctx, provinceIds)
	if err != nil {
		return nil, types.SearchFailError
	}

	cityIdToCountyMap := make(map[int64][]*types.CountyItem)
	if counties != nil && len(counties) > 0 {
		// 遍历 county 列表
		for _, v := range counties {
			cityId := v.CityID
			if _, ok := cityIdToCountyMap[cityId]; !ok {
				cityIdToCountyMap[cityId] = make([]*types.CountyItem, 0)
			}

			countyItem := &types.CountyItem{
				Id:         v.ID,
				Name:       v.Name,
				Code:       v.Code,
				FullCode:   v.FullCode,
				Level:      config.COUNTY_LEVEL,
				ProvinceId: v.ProvinceID,
				CityId:     v.CityID,
				Url:        v.URL,
				ChildUrl:   v.ChildURL,
				Children:   make([]any, 0),
				CreatedAt:  v.CreatedAt.Format(time.DateTime),
				UpdatedAt:  v.UpdatedAt.Format(time.DateTime),
			}

			if cityIdMap != nil {
				_v, ok := cityIdMap[v.CityID]
				if ok {
					countyItem.CityName = _v.Name
					countyItem.CityCode = _v.Code
					countyItem.CityFullCode = _v.FullCode
					countyItem.CityUrl = _v.URL
				}
			}

			if provinceIdMap != nil {
				_v, ok := provinceIdMap[v.ProvinceID]
				if ok {
					countyItem.ProvinceName = _v.Name
					countyItem.ProvinceCode = _v.Code
					countyItem.ProvinceFullCode = _v.FullCode
					countyItem.ProvinceUrl = _v.URL
				}
			}

			cityIdToCountyMap[cityId] = append(cityIdToCountyMap[cityId], countyItem)
		}
	}

	provinceIdToCityMap := make(map[int64][]*types.CityItem)
	if cities != nil && len(cities) > 0 {
		// 遍历 city列表
		for _, v := range cities {
			provinceId := v.ProvinceID
			if _, ok := provinceIdToCityMap[provinceId]; !ok {
				provinceIdToCityMap[provinceId] = make([]*types.CityItem, 0)
			}

			cityItem := &types.CityItem{
				Id:         v.ID,
				Name:       v.Name,
				Code:       v.Code,
				FullCode:   v.FullCode,
				Level:      config.CITY_LEVEL,
				ProvinceId: v.ProvinceID,
				Url:        v.URL,
				ChildUrl:   v.ChildURL,
				Children:   make([]*types.CountyItem, 0),
				CreatedAt:  v.CreatedAt.Format(time.DateTime),
				UpdatedAt:  v.UpdatedAt.Format(time.DateTime),
			}

			if provinceIdMap != nil {
				_v, ok := provinceIdMap[v.ProvinceID]
				if ok {
					cityItem.ProvinceName = _v.Name
					cityItem.ProvinceCode = _v.Code
					cityItem.ProvinceFullCode = _v.FullCode
					cityItem.ProvinceUrl = _v.URL
				}
			}

			if cityIdToCountyMap != nil {
				_v, ok := cityIdToCountyMap[v.ID]
				if ok {
					cityItem.Children = _v
				}
			}

			provinceIdToCityMap[provinceId] = append(provinceIdToCityMap[provinceId], cityItem)
		}
	}

	for _, v := range provinces {
		provinceItem := &types.ProvinceItem{
			Id:             v.ID,
			Name:           v.Name,
			Code:           v.Code,
			FullCode:       v.FullCode,
			Url:            v.URL,
			IsMunicipality: v.IsMunicipality,
			Level:          config.PROVINCE_LEVEL,
			ChildUrl:       v.ChildURL,
			CreatedAt:      v.CreatedAt.Format(time.DateTime),
			UpdatedAt:      v.CreatedAt.Format(time.DateTime),
			Children:       make([]*types.CityItem, 0),
		}

		if provinceIdToCityMap != nil {
			_v, ok := provinceIdToCityMap[v.ID]
			if ok {
				provinceItem.Children = _v
			}
		}

		resp.Data = append(resp.Data, provinceItem)
	}

	return resp, nil
}
