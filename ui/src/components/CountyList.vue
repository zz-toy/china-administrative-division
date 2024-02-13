<script setup>
import { reactive,onMounted } from 'vue'
import axios from 'axios'
import { mockUrls } from '../utils';

const dataSource = reactive({
  options: [],
  value: [],
  selectedText: "",
  countyCount: 0,
  apiData: []
})

const cascaderProps = {
  expandTrigger: 'hover',
}

onMounted(async () => {
  await init()
})

const init = async () => {
  const res = await axios.get(mockUrls.countyUiJson)
  const data = res.data
  if (data && Array.isArray(data) && data.length > 0) {
    dataSource.apiData = data
    dataSource.options = data
    dataSource.countyCount = dataSource.options.length
  } else {
    dataSource.apiData = []
  }
}

const handleChange = (value) => {
  dataSource.selectedText = value
}

const handleExportJsonFile = () => {
  saveJsonFile(dataSource.options, "province.json")
}


</script>

<template>
 <el-card shadow="always" style="height: 250px;">
    <template #header>
      <div class="card-header">
        <span>区县列表</span>
        <div>
          <el-button type="primary" @click="handleExportJsonFile">导出json</el-button>
        </div>
      </div>
    </template>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-text size="large" style="font-weight: bold;color: #409eff;">区县数量: {{dataSource.countyCount}}</el-text>
      </el-col>
      <el-col :span="8">
        <el-text size="large" style="font-weight: bold;color: #409eff;">选中: {{dataSource.selectedText}}</el-text>
      </el-col>
    </el-row>
    <el-select clearable placeholder="请选择" style="width: 300px;" v-model="dataSource.value" @change="handleChange">
      <el-option
        v-for="item in dataSource.options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
    />
    </el-select>
  </el-card>
</template>

<style scoped>
</style>
