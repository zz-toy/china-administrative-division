package collector

import (
	"github.com/gocolly/colly/v2"
	"github.com/zz-open/china-administrative-division/govstat/internal/config"
	"github.com/zz-open/china-administrative-division/govstat/internal/crawler"
)

var GgovStatCollector *colly.Collector

func InitGovStatCollector(crawler *crawler.GovStatCrawler) {
	c := colly.NewCollector(
		colly.UserAgent(crawler.UserAgent),
		colly.AllowedDomains(crawler.Domain),
		colly.MaxDepth(5),
		colly.IgnoreRobotsTxt(),
		colly.CacheDir(config.COLLECTOR_CACHE_DIR),
		colly.AllowURLRevisit(),
	)

	GgovStatCollector = c
}

// Limit 并发请求设置
// func (c *Collector) Limit() {
// 	c.C.Limit(&colly.LimitRule{
// 		DomainGlob:  "*stats.gov.cn*", // 匹配URL包含baidu的
// 		Parallelism: 10,               // 并发请求10
// 		RandomDelay: 1 * time.Second,  // 设置发起请求随机延时0-5
// 	})
// }

// func (c *Collector) Proxy() {
// 	// 设置代理:http https socks5
// 	proxyPool, err := proxy.RoundRobinProxySwitcher("http://111.3.102.207:30001", "http://183.247.211.41:30001")
// 	if err != nil {
// 		fmt.Println("设置代理失败", err)
// 		return
// 	}
// 	c.C.SetProxyFunc(proxyPool)
// }
