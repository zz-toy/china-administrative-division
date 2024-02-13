<script setup>
import PcCascader from './components/PcCascader.vue'
import PccCascader from './components/PccCascader.vue'
import ProvinceList from './components/ProvinceList.vue'
import CityList from './components/CityList.vue'
import CountyList from './components/CountyList.vue'
</script>

<template>
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

  <el-row :gutter="12">
    <el-col :span="8">
      <PcCascader />
    </el-col>
    <el-col :span="8">
      <PccCascader />
    </el-col>
  </el-row>
</template>

<style scoped>
</style>
