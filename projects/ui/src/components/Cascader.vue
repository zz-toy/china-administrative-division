<script setup>
import { ref, reactive, watchEffect } from 'vue'
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

const cascaderRef = ref()
const dataSource = reactive({
  options: [],
  value: [],
  selectedText: "",
  remoteData: [],
  selectedItem: null
})

const cascaderProps = {
  expandTrigger: 'hover',
}

const getRemoteData = async () => {
  if (!props.url) {
    return
  }

  const res = await axios.get(props.url)
  const data = res.data
  if (data && Array.isArray(data) && data.length > 0) {
    dataSource.remoteData = data
    dataSource.options = data
  } else if (data && Object.prototype.toString.call(data) === "[object Object]" && data.hasOwnProperty('data')) {
    dataSource.remoteData = data.data
    dataSource.options = data.data
  } else {
    dataSource.remoteData = []
    dataSource.options = []
  }
}

watchEffect(async () => {
  await getRemoteData()
})

const handleChange = (value) => {
  if (Array.isArray(value)) {
    dataSource.selectedText = value.join(",")
  } else {
    dataSource.selectedText = ""
  }

  dataSource.selectedItem = cascaderRef.value.getCheckedNodes()[0].data
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
      <el-text size="large" style="font-weight: bold;color: #409eff;">选中: {{dataSource.selectedText}}</el-text>
    </el-row>
    <el-row>
      <el-text size="large" style="font-weight: bold;color: #409eff;">选中item: {{dataSource.selectedItem}}</el-text>
    </el-row>
    <el-cascader ref="cascaderRef" clearable placeholder="请选择" style="width: 400px;"
        v-model="dataSource.value"
        :options="dataSource.options"
        :props="cascaderProps"
        @change="handleChange"
    />
  </el-card>
</template>

<style scoped>

</style>
