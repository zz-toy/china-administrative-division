<script setup>
import { reactive,onMounted } from 'vue'
import axios from 'axios'
import { rebuildTree, getProvinceListApiUrl, saveFile } from '../utils';

const dataSource = reactive({
  options: [],
  value: [],
  selectedText: "",
  provinceCount: 0
})

const cascaderProps = {
  expandTrigger: 'hover',
}

onMounted(async () => {
  await init()
})

const init = async () => {
  const res = await axios.get(getProvinceListApiUrl())
  const data = res.data.data
  if (data && Array.isArray(data)) {
    dataSource.options = rebuildTree(data)
    dataSource.provinceCount = dataSource.options.length
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
  saveFile(dataSource.options, "province.json")
}

</script>

<template>
 <el-card shadow="always" style="height: 250px;">
    <template #header>
      <div class="card-header">
        <span>省列表</span>
        <el-button type="primary" @click="handleExportJsonFile">导出json</el-button>
      </div>
    </template>
    <el-cascader clearable placeholder="请选择" style="width: 400px;"
        v-model="dataSource.value"
        :options="dataSource.options"
        :props="cascaderProps"
        @change="handleChange"
    />
    <el-text size="large" style="font-weight: bold;color: #409eff;">省份数量:{{dataSource.provinceCount}}</el-text>
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
