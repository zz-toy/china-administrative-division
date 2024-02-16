import govStatProvinceCascadeJsonUrl from '../../../../dist/govstat/province-cascade.json?url'
import govStatCityCascadeJsonUrl from '../../../../dist/govstat/city-cascade.json?url'
import govStatCountyCascadeJsonUrl from '../../../../dist/govstat/county-cascade.json?url'
import govStatPcJsonUrl from '../../../../dist/govstat/pc.json?url'
import govStatPccJsonUrl from '../../../../dist/govstat/pcc.json?url'

import bdMapProvinceCascadeJsonUrl from '../../../../dist/bdmap/province-cascade.json?url'
import bdMapCityCascadeJsonUrl from '../../../../dist/bdmap/city-cascade.json?url'
import bdMapCountyCascadeJsonUrl from '../../../../dist/bdmap/county-cascade.json?url'
import bdMapPcJsonUrl from '../../../../dist/bdmap/pc.json?url'
import bdMapPccJsonUrl from '../../../../dist/bdmap/pcc.json?url'

export const govStatMockUrl = {
     provinceUrl: govStatProvinceCascadeJsonUrl,
     cityUrl: govStatCityCascadeJsonUrl,
     countyUrl: govStatCountyCascadeJsonUrl,
     pcUrl: govStatPcJsonUrl,
     pccUrl:govStatPccJsonUrl
}

export const bdMapMockUrl = {
    provinceUrl: bdMapProvinceCascadeJsonUrl,
    cityUrl: bdMapCityCascadeJsonUrl,
    countyUrl: bdMapCountyCascadeJsonUrl,
    pcUrl: bdMapPcJsonUrl,
    pccUrl:bdMapPccJsonUrl
}

export const mockUrl = bdMapMockUrl