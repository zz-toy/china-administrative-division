<script setup>
import { reactive,onMounted } from 'vue'
import axios from 'axios'
import { mockUrls} from '../utils';

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
  const res = await axios.get(mockUrls.pccUiJson)
  const data = res.data
  if (data && Array.isArray(data) && data.length > 0) {
    dataSource.apiData = data
    dataSource.options = data
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

</script>

<template>
  <el-card shadow="always" style="height: 250px;">
    <template #header>
      <div class="card-header">
        <span>[省市区] 三级联动</span>
        <div>
          <el-button type="primary">示例</el-button>
        </div>
      </div>
    </template>
    <el-row :gutter="12">
      <el-text size="large" style="font-weight: bold;color: #409eff;">选中: {{dataSource.selectedText}}</el-text>
    </el-row>
    <el-cascader clearable placeholder="请选择" style="width: 400px;"
        v-model="dataSource.value"
        :options="dataSource.options"
        :props="cascaderProps"
        @change="handleChange"
    />
  </el-card>
</template>

<style scoped>

</style>
