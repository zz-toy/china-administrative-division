<script setup>
import { reactive,onMounted } from 'vue'
import axios from 'axios'
import { cascadeTree,getPccListApiUrl,saveJsonFile } from '../utils';

const dataSource = reactive({
  options: [],
  value: [],
  selectedText: "",
  apiData: []
})

const cascaderProps = {
  expandTrigger: 'hover',
}

onMounted(async () => {
  await init()
})

const init = async () => {
  const res = await axios.get(getPccListApiUrl())
  const data = res.data.data
  if (data && Array.isArray(data) && data.length > 0) {
    dataSource.apiData = data
    dataSource.options = cascadeTree(data)
  } else {
    dataSource.apiData = []
  }
}

const handleChange = (value) => {
  if (value) {
    dataSource.selectedText = `${value[0]} ${value[1]} ${value[2]}`
  } else {
    dataSource.selectedText = ""
  }
}

const handleExportJsonFile = () => {
  saveJsonFile(dataSource.options, "pcc.json")
}

const handleExportZnJsonFile = () => {
  saveJsonFile(znCascadeTree(dataSource.apiData), "zn-province-city-district.json")
}

</script>

<template>
  <el-card shadow="always" style="height: 250px;">
    <template #header>
      <div class="card-header">
        <span>省市区三级联动</span>
        <div>
          <el-button type="primary" @click="handleExportJsonFile">导出json</el-button>
          <el-button type="danger" @click="handleExportZnJsonFile">导出zn-json</el-button>
        </div>
        
      </div>
    </template>
    <el-cascader clearable placeholder="请选择" style="width: 400px;"
        v-model="dataSource.value"
        :options="dataSource.options"
        :props="cascaderProps"
        @change="handleChange"
    />
    
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
