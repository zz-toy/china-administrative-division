package county

import (
	"context"
	"time"

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

func (l *ListLogic) List(req *types.CountyListRequest) (resp *types.CountyListResponse, err error) {
	resp = &types.CountyListResponse{
		BaseResponse: types.SuccessResponse(),
		Data:         make([]*types.CountyInfo, 0),
	}

	var provinceIds []int64
	if req.ProvinceName != "" {
		provinceIds, err = l.svcCtx.ProvinceModel.IdsByName(l.ctx, req.ProvinceName)
		if err != nil {
			return nil, types.SearchFailError
		}

		if provinceIds == nil || len(provinceIds) == 0 {
			return resp, nil
		}
	}

	if req.ProvinceId > 0 {
		provinceIds = append(provinceIds, req.ProvinceId)
	}

	var cityIds []int64
	if req.CityName != "" {
		cityIds, err = l.svcCtx.CityModel.IdsByName(l.ctx, req.CityName)
		if err != nil {
			return nil, types.SearchFailError
		}

		if cityIds == nil || len(cityIds) == 0 {
			return resp, nil
		}
	}

	if req.CityId > 0 {
		cityIds = append(cityIds, req.CityId)
	}

	counties, err := l.svcCtx.CountyModel.ListByConditionQuery(l.ctx, req.Name, provinceIds, cityIds)
	if err != nil {
		return nil, types.SearchFailError
	}

	if counties == nil || len(counties) == 0 {
		return resp, nil
	}

	provinceIds = nil
	cityIds = nil
	for _, v := range counties {
		provinceIds = append(provinceIds, v.ProvinceID)
		cityIds = append(cityIds, v.CityID)
	}

	provinceIdMap, err := l.svcCtx.ProvinceModel.IdMapByIds(l.ctx, provinceIds)
	if err != nil {
		return nil, types.SearchFailError
	}

	cityIdMap, err := l.svcCtx.CityModel.IdMapByIds(l.ctx, cityIds)
	if err != nil {
		return nil, types.SearchFailError
	}

	for _, v := range counties {
		countyInfo := &types.CountyInfo{
			Id:         v.ID,
			Name:       v.Name,
			Code:       v.Code,
			ProvinceId: v.ProvinceID,
			CityId:     v.CityID,
			Url:        v.URL,
			ChildUrl:   v.ChildURL,
			CreatedAt:  v.CreatedAt.Format(time.DateTime),
			UpdatedAt:  v.CreatedAt.Format(time.DateTime),
		}

		if provinceIdMap != nil {
			_v, ok := provinceIdMap[v.ProvinceID]
			if ok {
				countyInfo.ProvinceName = _v.Name
				countyInfo.ProvinceName = _v.Name
				countyInfo.ProvinceCode = _v.Code
				countyInfo.ProvinceUrl = _v.URL
			}
		}

		if cityIdMap != nil {
			_vv, ok := cityIdMap[v.CityID]
			if ok {
				countyInfo.CityName = _vv.Name
				countyInfo.CityName = _vv.Name
				countyInfo.CityCode = _vv.Code
				countyInfo.CityUrl = _vv.URL
			}
		}

		resp.Data = append(resp.Data, countyInfo)
	}

	return resp, nil
}
