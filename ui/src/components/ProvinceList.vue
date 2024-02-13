<script setup>
import { reactive,onMounted } from 'vue'
import axios from 'axios'
import { mockUrls } from '../utils';

const dataSource = reactive({
  options: [],
  value: [],
  selectedText: "",
  provinceCount: 0,
  apiData: []
})

const cascaderProps = {
  expandTrigger: 'hover',
}

onMounted(async () => {
  await init()
})

const init = async () => {
  const res = await axios.get(mockUrls.provinceUiJson)
  const data = res.data
  if (data && Array.isArray(data) && data.length > 0) {
    dataSource.apiData = data
    dataSource.options = data
    dataSource.provinceCount = dataSource.options.length
  } else {
    dataSource.apiData = []
  }
}

const handleChange = (value) => {
  dataSource.selectedText = value
}

</script>

<template>
 <el-card shadow="always" style="height: 250px;">
    <template #header>
      <div class="card-header">
        <span>[省] 列表</span>
        <div>
          <el-button type="primary">示例</el-button>
        </div>
      </div>
    </template>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-text size="large" style="font-weight: bold;color: #409eff;">省数量: {{dataSource.provinceCount}}</el-text>
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
