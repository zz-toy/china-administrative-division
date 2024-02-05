package task

import (
	"io"
	"log"
	"os"
	"sync"

	"github.com/gocolly/colly/v2"
	"github.com/zz-open/china-administrative-division/govstat/internal/collector"
	"github.com/zz-open/china-administrative-division/govstat/internal/crawler"
	"github.com/zz-open/china-administrative-division/govstat/internal/transfer"
)

var cityLogFile *os.File
var cityLogger *log.Logger

func init() {
	var err error
	cityLogger = log.New(os.Stderr, "", log.LstdFlags)
	cityLogFile, err = os.OpenFile("../logs/city.log", os.O_CREATE|os.O_APPEND|os.O_RDWR, os.ModePerm)
	if err != nil {
		return
	}

	multiWriter := io.MultiWriter(cityLogFile)
	cityLogger.SetOutput(multiWriter)
}

func StartAsyncCityTask(wg *sync.WaitGroup, readChan <-chan any) {
	crawler := crawler.GgovStatCrawller
	c := collector.GgovStatCollector.Clone()

	wg.Add(1)
	go func() {
		defer wg.Done()

		c.OnRequest(func(r *colly.Request) {
			cityLogger.Println("Visiting", r.URL)
		})

		c.OnError(func(_ *colly.Response, err error) {
			cityLogger.Println("Something went wrong:", err)
		})

		c.OnResponse(func(r *colly.Response) {
			cityLogger.Println("Visited", r.Request.URL)
		})

		c.OnHTML(".provincetr", func(e *colly.HTMLElement) {
			// e.ForEach("td > a", func(_ int, elem *colly.HTMLElement) {
			// 	fmt.Println(elem.Text)
			// })
		})

		c.OnScraped(func(r *colly.Response) {
			cityLogger.Println("Finished", r.Request.URL)
		})

		for v := range readChan {
			log.Printf("v=%+v \n", v)
			transfer, ok := v.(*transfer.TransferInfo)
			cityLogger.Printf("transfer=%+v, ok=%+v\n", transfer, ok)
			if !ok {
				cityLogger.Printf("沒有值\n")
				continue
			}

			cityLogger.Println("city index:", crawler.CityIndexUrl(transfer.ProvinceZoneCode))

			// err := c.Visit(crawler.CityIndexUrl(transfer.ProvinceZoneCode))
			// if err != nil {
			// 	log.Println(err)
			// }
		}
	}()
}
