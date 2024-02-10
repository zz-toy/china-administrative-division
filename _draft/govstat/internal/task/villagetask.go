package task

import (
	"encoding/csv"
	"os"
)

func _write() {
	// 创建要写入的 CSV 文件
	file, err := os.Create("data.csv")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// 创建 CSV writer
	writer := csv.NewWriter(file)
	defer writer.Flush()

	// 写入 CSV 头部
	header := []string{"姓名", "年龄", "城市"}
	writer.Write(header)

	// 写入数据行
	data1 := []string{"张三", "25", "北京"}
	writer.Write(data1)

	data2 := []string{"李四", "30", "上海"}
	writer.Write(data2)

	// 注意：写入文件时，要调用 Flush 方法将数据刷新到文件中

	// 手动刷新，确保所有数据写入文件
	writer.Flush()

	// 检查写入过程中是否发生错误
	if err := writer.Error(); err != nil {
		panic(err)
	}
}
