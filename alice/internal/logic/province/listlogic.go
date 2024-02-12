package province

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

func (l *ListLogic) List(req *types.ProvinceListRequest) (resp *types.ProvinceListResponse, err error) {
	resp = &types.ProvinceListResponse{
		BaseResponse: types.SuccessResponse(),
		Data:         make([]*types.ProviceInfo, 0),
	}

	provinces, err := l.svcCtx.ProvinceModel.ListByConditionQuery(l.ctx, req.Name, req.IsMunicipality)
	if err != nil {
		return nil, types.SearchFailError
	}

	if provinces == nil || len(provinces) == 0 {
		return resp, nil
	}

	for _, v := range provinces {
		provinceInfo := &types.ProviceInfo{
			Id:             v.ID,
			Name:           v.Name,
			Code:           v.Code,
			FullCode:       v.FullCode,
			Url:            v.URL,
			IsMunicipality: v.IsMunicipality,
			ChildUrl:       v.ChildURL,
			CreatedAt:      v.CreatedAt.Format(time.DateTime),
			UpdatedAt:      v.CreatedAt.Format(time.DateTime),
		}

		resp.Data = append(resp.Data, provinceInfo)
	}

	return resp, nil
}
