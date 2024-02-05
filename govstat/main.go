package main

import (
	"io"
	"log"
	"os"
	"sync"
	"time"

	"github.com/zz-open/china-administrative-division/govstat/internal/collector"
	"github.com/zz-open/china-administrative-division/govstat/internal/crawler"
	"github.com/zz-open/china-administrative-division/govstat/internal/task"
)

var provinceChan = make(chan any, 5)

// var cityChan = make(chan any, 5)
// var districtChan = make(chan any, 5)
// var streetChan = make(chan any, 10)
// var villageChan = make(chan any, 10)

var wg sync.WaitGroup
var logFile *os.File
var logger *log.Logger

func init() {
	var err error
	logger = log.New(os.Stderr, "", log.LstdFlags)
	logFile, err = os.OpenFile("../logs/govstat.log", os.O_CREATE|os.O_APPEND|os.O_RDWR, os.ModePerm)
	if err != nil {
		return
	}

	multiWriter := io.MultiWriter(os.Stdout, logFile)
	logger.SetOutput(multiWriter)
}

func main() {
	defer logFile.Close()

	start := time.Now()
	logger.Println("====== START ======")

	// 全局初始化
	crawler.InitGovStatCrawller()
	collector.InitGovStatCollector(crawler.GgovStatCrawller)

	task.StartAsyncProvinceTask(&wg, provinceChan)
	task.StartAsyncCityTask(&wg, provinceChan)

	wg.Wait()

	end := time.Since(start)
	logger.Println("耗时：", end)
	logger.Println("====== END ======")
}
