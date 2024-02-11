package types

import (
	"errors"
	"fmt"
	"time"
)

type BaseResponseOption func(*BaseResponse)

func WithMsg(message string) BaseResponseOption {
	return func(resp *BaseResponse) {
		resp.Msg = message
	}
}

func WithCode(code int) BaseResponseOption {
	return func(resp *BaseResponse) {
		resp.Code = code
	}
}

func NewApiResponse(opts ...BaseResponseOption) BaseResponse {
	res := BaseResponse{
		Time: time.Now().Format(time.DateTime),
	}

	for _, opt := range opts {
		opt(&res)
	}

	return res
}

const SuccessCode = 200
const FailCode = 500

const SuccessMsg = "success"
const FailMsg = "网络开小差，请稍后重试"

var SearchFailError = errors.New("查询失败，请重试")

func RequestParameterInValidMsg(field string) string {
	return fmt.Sprintf("参数:%v 无效，请检查", field)
}

func SuccessResponse() BaseResponse {
	return NewApiResponse(WithCode(SuccessCode), WithMsg(SuccessMsg))
}

func DefaultFailResponse() BaseResponse {
	return FailResponse(FailCode, FailMsg)
}

func FailResponse(code int, message string) BaseResponse {
	return NewApiResponse(WithCode(code), WithMsg(message))
}

func FailResponseWithMessage(message string) BaseResponse {
	return NewApiResponse(WithCode(FailCode), WithMsg(message))
}
