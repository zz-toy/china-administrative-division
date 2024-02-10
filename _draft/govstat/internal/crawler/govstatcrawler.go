package crawler

import (
	"fmt"

	"github.com/zz-open/china-administrative-division/govstat/internal/config"
)

var GgovStatCrawller *GovStatCrawler

func InitGovStatCrawller() {
	GgovStatCrawller = NewGovStatCrawler()
}

type GovStatCrawler struct {
	Protocol  string `json:"protocol"`
	Domain    string `json:"domain"`
	UserAgent string `json:"user_agent"`
	Year      string `json:"year"`
}

func NewGovStatCrawler() *GovStatCrawler {
	crawler := &GovStatCrawler{}
	crawler.Protocol = "https"
	crawler.Domain = "www.stats.gov.cn"
	crawler.UserAgent = config.USER_AGENT
	crawler.Year = "2023"
	return crawler
}

func (c *GovStatCrawler) UrlPrefix() string {
	return fmt.Sprintf("%s://%s/sj/tjbz/tjyqhdmhcxhfdm/%s", c.Protocol, c.Domain, c.Year)
}

func (c *GovStatCrawler) ProvinceIndexUrl() string {
	return fmt.Sprintf("%s/index.html", c.UrlPrefix())
}

func (c *GovStatCrawler) CityIndexUrl(provinceZoneCode string) string {
	return fmt.Sprintf("%s/%s.html", c.UrlPrefix(), provinceZoneCode)
}

func (c *GovStatCrawler) DistrictIndexUrl(provinceZoneCode string, cityZoneCode string) string {
	return fmt.Sprintf("%s/%s/%s.html", c.UrlPrefix(), provinceZoneCode, cityZoneCode)
}

func (c *GovStatCrawler) StreetIndexUrl(provinceZoneCode string, cityZoneCode string, streetZoneCode string) string {
	return fmt.Sprintf("%s/%s/%s/%s.html", c.UrlPrefix(), provinceZoneCode, cityZoneCode, streetZoneCode)
}

func (c *GovStatCrawler) VillageIndexUrl(provinceZoneCode string, cityZoneCode string, streetZoneCode string, villageZoneCode string) string {
	return fmt.Sprintf("%s/%s/%s/%s/%s.html", c.UrlPrefix(), provinceZoneCode, cityZoneCode, streetZoneCode, villageZoneCode)
}
