<script setup>
import {ref} from 'vue'
import Select from './Select.vue'
import Cascader from './Cascader.vue'
import {mockUrl, znMockUrl} from '../utils';

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


const znComponentProps = ref([
  {title: "[省] 列表", url: znMockUrl.provinceUrl},
  {title: "[省市] 列表", url: znMockUrl.pcUrl},
  {title: "[省市区] 列表", url: znMockUrl.pccUrl},
])

</script>

<template>
  <el-alert title="ZN" center type="success" :closable="false" />
  <el-row>
    <el-col :span="8" v-for="(opt, index) in znComponentProps">
      <Cascader v-bind="opt"/>
    </el-col>
  </el-row>
  <el-alert title="百度地图" center type="success" :closable="false" />
  <el-row>
    <el-col :span="8" v-for="(opt, index) in selectComponentProps">
      <Select v-bind="opt"/>
    </el-col>
  </el-row>
  <el-alert title="govstat" center type="success" :closable="false" />
  <el-row>
    <el-col :span="8" v-for="(opt, index) in cascaderComponentProps">
      <Cascader v-bind="opt"/>
    </el-col>
  </el-row>

</template>

<style scoped>
</style>
