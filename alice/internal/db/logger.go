package db

import (
	"alice/internal/config"
	"fmt"
	"log"
	"os"
	"time"

	"gorm.io/gorm/logger"
)

func NewGormLogger(conf config.Config) logger.Interface {
	// db log name
	filename := fmt.Sprintf("%s/%s%s%s", conf.Log.Path, "sql.", time.Now().Format(time.DateOnly), ".log")
	file, err := os.Create(filename)
	if err != nil {
		panic(err)
	}

	// logger.Default.LogMode(logger.Info)
	newLogger := logger.New(
		log.New(file, "\r\n", log.LstdFlags),
		logger.Config{
			SlowThreshold:             time.Second,
			LogLevel:                  logger.Info,
			IgnoreRecordNotFoundError: true,
			ParameterizedQueries:      false,
			Colorful:                  false,
		},
	)

	return newLogger
}
