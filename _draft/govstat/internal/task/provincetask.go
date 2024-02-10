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
	"github.com/zz-open/china-administrative-division/govstat/internal/utils"
)

var provinceLogFile *os.File
var provinceLogger *log.Logger

func init() {
	var err error
	provinceLogger = log.New(os.Stderr, "", log.LstdFlags)
	provinceLogFile, err = os.OpenFile("../logs/province.log", os.O_CREATE|os.O_APPEND|os.O_RDWR, os.ModePerm)
	if err != nil {
		return
	}

	multiWriter := io.MultiWriter(provinceLogFile)
	provinceLogger.SetOutput(multiWriter)
}

func StartAsyncProvinceTask(wg *sync.WaitGroup, writeChan chan<- any) {
	crawler := crawler.GgovStatCrawller
	c := collector.GgovStatCollector
	wg.Add(1)
	go func() {
		defer wg.Done()

		c.OnRequest(func(r *colly.Request) {
			provinceLogger.Println("Visiting", r.URL)
		})

		c.OnError(func(_ *colly.Response, err error) {
			provinceLogger.Println("Something went wrong:", err)
		})

		c.OnResponse(func(r *colly.Response) {
			provinceLogger.Println("Visited", r.Request.URL)
		})

		c.OnHTML(".provincetr", func(e *colly.HTMLElement) {
			e.ForEach("td > a", func(_ int, elem *colly.HTMLElement) {
				provinceText := elem.Text
				if provinceText == "" {
					provinceLogger.Println("===沒有值===")
					return
				}

				zoneCode := utils.TrimZoneCode(elem.Attr("href"))
				t := &transfer.TransferInfo{
					Province:             provinceText,
					ProvinceZoneCode:     zoneCode,
					FullProvinceZoneCode: zoneCode + "0000000000", //
				}

				provinceLogger.Println("provinceText:", t)
				writeChan <- t
			})
		})

		c.OnScraped(func(r *colly.Response) {
			close(writeChan)
			provinceLogger.Println("Finished", r.Request.URL)
		})

		err := c.Visit(crawler.ProvinceIndexUrl())
		if err != nil {
			provinceLogger.Println(err)
		}
	}()
}
