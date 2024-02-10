package utils

import (
	"fmt"
	"strings"
)

func TrimZoneCode(url string) string {
	if url == "" {
		return ""
	}

	return strings.TrimSuffix(url, ".html")
}

func FullProvinceZoneCode(provinceCode string) string {
	return fmt.Sprintf("%s0000000000", provinceCode)
}

func FullCityZoneCode(provinceCode string, cityCode string) string {
	return fmt.Sprintf("%s%s0000000000", provinceCode, cityCode)
}

func FullStreetZoneCode(provinceCode string, cityCode string) string {
	return fmt.Sprintf("%s%s0000000000", provinceCode, cityCode)
}
