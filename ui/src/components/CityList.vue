<script setup>
import { reactive,onMounted } from 'vue'
import axios from 'axios'
import { getCityTree, getCityListApiUrl, saveJsonFile } from '../utils';

const dataSource = reactive({
  options: [],
  value: [],
  selectedText: "",
  cityCount: 0,
  apiData: []
})

const cascaderProps = {
  expandTrigger: 'hover',
}

onMounted(async () => {
  await init()
})

const init = async () => {
  const res = await axios.get(getCityListApiUrl())
  const data = res.data.data
  if (data && Array.isArray(data) && data.length > 0) {
    dataSource.apiData = data
    dataSource.options = getCityTree(data)
    dataSource.cityCount = dataSource.options.length
  } else {
    dataSource.apiData = []
  }
}

const handleChange = (value) => {
  if (value) {
    dataSource.selectedText = `${value[0]}`
  } else {
    dataSource.selectedText = ""
  }
}

const handleExportJsonFile = () => {
  saveJsonFile(dataSource.options, "province.json")
}


</script>

<template>
 <el-card shadow="always" style="height: 250px;">
    <template #header>
      <div class="card-header">
        <span>城市列表</span>
        <div>
          <el-button type="primary" @click="handleExportJsonFile">导出json</el-button>
        <el-button type="primary" @click="handleExportJsonFile">导出json</el-button>
        </div>
        
      </div>
    </template>
    <el-cascader clearable placeholder="请选择" style="width: 400px;"
        v-model="dataSource.value"
        :options="dataSource.options"
        :props="cascaderProps"
        @change="handleChange"
    />
    <el-text size="large" style="font-weight: bold;color: #409eff;">城市数量:{{dataSource.cityCount}}</el-text>
    <div style="margin-top: 10px;">
      <el-text size="large" style="font-weight: bold;color: #409eff;">{{dataSource.selectedText}}</el-text>
    </div>
  </el-card>
</template>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 480px;
}
</style>
