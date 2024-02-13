<script setup>
import PcCascader from './components/PCCascader.vue'
import PCCCascader from './components/PCCCascader.vue'
import ProvinceList from './components/ProvinceList.vue'
import CityList from './components/CityList.vue'
import CountyList from './components/CountyList.vue'
</script>

<template>
  <el-row :gutter="12">
    <el-col :span="8">
      <PCCascader />
    </el-col>
    <el-col :span="8">
      <PCCCascader />
    </el-col>
    <el-col :span="8">
      <el-card shadow="never"> Never </el-card>
    </el-col>
  </el-row>
 
  <el-row :gutter="12">
    <el-col :span="8">
      <ProvinceList />
    </el-col>
    <el-col :span="8">
      <CityList />
    </el-col>
    <el-col :span="8">
     <CountyList />
    </el-col>
  </el-row>
  
</template>

<style scoped>
</style>
