<script setup>
import {ref} from 'vue'
import Select from './Select.vue'
import Cascader from './Cascader.vue'
import {mockUrl} from '../utils';

const selectComponentProps = ref([
  {title: "[省] 列表", url: mockUrl.provinceUrl},
  {title: "[城市] 列表", url: mockUrl.cityUrl},
  {title: "[区县] 列表", url: mockUrl.countyUrl},
])


const cascaderComponentProps = ref([
  {title: "[省市] 列表", url: mockUrl.pcUrl},
  {title: "[省市区] 列表", url: mockUrl.pccUrl},
  {title: "[省市区乡镇] 列表", url: ''},
])
</script>

<template>
  <el-row>
    <el-col :span="8" v-for="(opt, index) in selectComponentProps">
      <Select v-bind="opt"/>
    </el-col>
  </el-row>

  <el-row>
    <el-col :span="8" v-for="(opt, index) in cascaderComponentProps">
      <Cascader v-bind="opt"/>
    </el-col>
  </el-row>
</template>

<style scoped>
</style>
