<script setup>
import { reactive, watchEffect } from 'vue'
import axios from 'axios'

const props = defineProps({
  title: {
    type: String,
    default: ""
  },
  url: {
    type: String,
    default: ""
  },
})

const dataSource = reactive({
  options: [],
  value: [],
  selectedText: "",
  count: 0,
  remoteData: []
})

const getRemoteData = async () => {
  if (!props.url) {
    return
  }
  
  const res = await axios.get(props.url)
  const data = res.data
  if (data && Array.isArray(data) && data.length > 0) {
    dataSource.remoteData = data
    dataSource.options = data
    dataSource.count = dataSource.options.length
  } else {
    dataSource.apiData = []
  }
}

watchEffect(async () => {
  await getRemoteData()
})

const handleChange = (value) => {
  dataSource.selectedText = value
}

</script>

<template>
 <el-card shadow="always" style="height: 250px;">
    <template #header>
      <div class="card-header">
        <span>{{ title }}</span>
        <div>
          <el-button type="primary">示例</el-button>
        </div>
      </div>
    </template>
    <el-row>
      <el-text size="large" style="font-weight: bold;color: #409eff;">数量: {{dataSource.count}}</el-text>
    </el-row>
    <el-row>
      <el-text size="large" style="font-weight: bold;color: #409eff;">选中: {{dataSource.selectedText}}</el-text>
    </el-row>
    <el-select clearable placeholder="请选择" style="width: 300px;" v-model="dataSource.value" @change="handleChange" value-key="code">
      <el-option
        v-for="item in dataSource.options"
        :key="item.code"
        :label="item.label"
        :value="item"
    />
    </el-select>
  </el-card>
</template>

<style scoped>
</style>
