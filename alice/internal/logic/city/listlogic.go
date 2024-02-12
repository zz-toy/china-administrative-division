package city

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

func (l *ListLogic) List(req *types.CityListRequest) (resp *types.CityListResponse, err error) {
	resp = &types.CityListResponse{
		BaseResponse: types.SuccessResponse(),
		Data:         make([]*types.CityInfo, 0),
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

	cities, err := l.svcCtx.CityModel.ListByConditionQuery(l.ctx, req.Name, provinceIds)
	if err != nil {
		return nil, types.SearchFailError
	}

	if cities == nil || len(cities) == 0 {
		return resp, nil
	}

	provinceIds = nil
	for _, v := range cities {
		provinceIds = append(provinceIds, v.ProvinceID)
	}

	provinceIdMap, err := l.svcCtx.ProvinceModel.IdMapByIds(l.ctx, provinceIds)
	if err != nil {
		return nil, types.SearchFailError
	}

	for _, v := range cities {
		cityInfo := &types.CityInfo{
			Id:         v.ID,
			Name:       v.Name,
			Code:       v.Code,
			ProvinceId: v.ProvinceID,
			Url:        v.URL,
			ChildUrl:   v.ChildURL,
			CreatedAt:  v.CreatedAt.Format(time.DateTime),
			UpdatedAt:  v.CreatedAt.Format(time.DateTime),
		}

		if provinceIdMap != nil {
			_v, ok := provinceIdMap[v.ProvinceID]
			if ok {
				cityInfo.ProvinceName = _v.Name
				cityInfo.ProvinceCode = _v.Code
				cityInfo.ProvinceUrl = _v.URL
			}
		}

		resp.Data = append(resp.Data, cityInfo)
	}

	return resp, nil
}
