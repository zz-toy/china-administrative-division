package transfer

type TransferInfo struct {
	Province             string `json:"province"`                // 省
	ProvinceZoneCode     string `json:"province_zone_code"`      // 省区划代码，前2位
	FullProvinceZoneCode string `json:"full_province_zone_code"` // 完整省区划代码，12位
	City                 string `json:"city"`
	CityZoneCode         string `json:"city_zone_code"`
	FullCityZoneCode     string `json:"full_city_zone_code"`
	District             string `json:"district"`
	DistrictZoneCode     string `json:"district_zone_code"`
	FullDistrictZoneCode string `json:"full_district_zone_code"`
	Street               string `json:"street"`
	StreetZoneCode       string `json:"street_zone_code"`
	FullStreetZoneCode   string `json:"full_street_zone_code"`
	Village              string `json:"village"`
	VillageZoneCode      string `json:"village_zone_code"`
	FullVillageZoneCode  string `json:"full_village_zone_code"`
}
