import govStatProvinceJsonUrl from '../../../../dist/govstat/province-cascade.json?url'
import govStatCityJsonUrl from '../../../../dist/govstat/city-cascade.json?url'
import govStatCountyJsonUrl from '../../../../dist/govstat/county-cascade.json?url'
import govStatPcJsonUrl from '../../../../dist/govstat/pc.json?url'
import govStatPccJsonUrl from '../../../../dist/govstat/pcc.json?url'

import bdMapProvinceJsonUrl from '../../../../dist/bdmap/province-cascade.json?url'
import bdMapCityJsonUrl from '../../../../dist/bdmap/city-cascade.json?url'
import bdMapCountyJsonUrl from '../../../../dist/bdmap/county-cascade.json?url'
import bdMapPcJsonUrl from '../../../../dist/bdmap/pc.json?url'
import bdMapPccJsonUrl from '../../../../dist/bdmap/pcc.json?url'

import znProvinceJsonUrl from '../../../../dist/zn/province-zn.json?url'
import znPcJsonUrl from '../../../../dist/zn/pc-zn.json?url'
import znPccJsonUrl from '../../../../dist/zn/pcc-zn.json?url'


export const govStatMockUrl = {
     provinceUrl: govStatProvinceJsonUrl,
     cityUrl: govStatCityJsonUrl,
     countyUrl: govStatCountyJsonUrl,
     pcUrl: govStatPcJsonUrl,
     pccUrl:govStatPccJsonUrl
}

export const bdMapMockUrl = {
    provinceUrl: bdMapProvinceJsonUrl,
    cityUrl: bdMapCityJsonUrl,
    countyUrl: bdMapCountyJsonUrl,
    pcUrl: bdMapPcJsonUrl,
    pccUrl:bdMapPccJsonUrl
}

export const znMockUrl = {
    provinceUrl: znProvinceJsonUrl,
    pcUrl: znPcJsonUrl,
    pccUrl: znPccJsonUrl
}

export const mockUrl = bdMapMockUrl