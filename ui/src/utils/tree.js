// 单级别数据 ====================================================

export const getProvinceTree = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const provinceList = []

    list.forEach((province) => {
        provinceList.push({
            label: province.name,
            value: province.name,
            code: province.code,
        })
    })

    return provinceList
}

export const getCityTree = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const cityList = []

    list.forEach((city) => {
        cityList.push({
            label: city.name,
            value: city.name,
            code: city.code,
            province_code: city.province_code,
        })
    })

    return cityList
}

export const getCountyTree = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const countyList = []

    list.forEach((county) => {
        countyList.push({
            label: county.name,
            value: county.name,
            code: county.code,
            city_code: county.city_code,
            province_code: county.province_code,
        })
    })

    return countyList
}

// 级联数据
export const cascadeTree = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const provinceList = []
    const cityList = []
    const countyList = []
    const townList = []
    const villageList = []

    // 递归每一层，平铺成 list
    list.forEach((province) => {
        provinceList.push({
            id: province.id,
            name: province.name,
            code: province.code,
            url: province.url,
            child_url: province.child_url,
            created_at: province.created_at,
            updated_at: province.updated_at,
        })
        if (province.children && Array.isArray(province.children) && province.children.length > 0) {
            province.children.forEach((city) => {
                cityList.push({
                    id: city.id,
                    name: city.name,
                    code: city.code,
                    url: city.url,
                    province_id: city.province_id,
                    province_name: city.province_name,
                    province_url: city.province_url,
                    child_url: city.child_url,
                    created_at: city.created_at,
                    updated_at: city.updated_at,
                })

                if (city.children && Array.isArray(city.children) && city.children.length > 0) {
                    city.children.forEach((county) => {
                        countyList.push({
                            id: county.id,
                            name: county.name,
                            code: county.code,
                            province_id: county.province_id,
                            province_name: county.province_name,
                            province_url: county.province_url,
                            city_id: county.city_id,
                            city_name: county.city_name,
                            city_url: county.city_url,
                            url: county.url,
                            child_url: county.child_url,
                            created_at: county.created_at,
                            updated_at: county.updated_at,
                        })
                    })
                }
            })
        }
    })

    if (provinceList.length === 0) {
        return []
    }

    // 组装新的结构
    const cityIdToCountyMap = {}
    if (countyList.length > 0) {
        countyList.forEach((county) => {
            if (!cityIdToCountyMap[county.city_id]) {
                cityIdToCountyMap[county.city_id] = []
            }

            const _county = {
                label: county.name,
                value: county.name,
                code: county.code,
                children: []
            }

            if (_county.children.length === 0) {
                delete _county.children
            }

            cityIdToCountyMap[county.city_id].push(_county)
        })
    }


    const provinceIdToCityMap = {}
    if (cityList.length > 0) {
        cityList.forEach((city) => {
            if (!provinceIdToCityMap[city.province_id]) {
                provinceIdToCityMap[city.province_id] = []
            }
            
            const _city = {
                label: city.name,
                value: city.name,
                code: city.code,
                children: []
            }
            
            if (cityIdToCountyMap && cityIdToCountyMap[city.id]) {
                _city.children = cityIdToCountyMap[city.id]
            }

            if (_city.children.length === 0) {
                delete _city.children
            }

            provinceIdToCityMap[city.province_id].push(_city)
        })
    }

    const res = []
    provinceList.forEach((province) => {
        const _province = {
            label: province.name,
            value: province.name,
            code: province.code,
            children: []
        }

        if (provinceIdToCityMap && provinceIdToCityMap[province.id]) {
            _province.children = provinceIdToCityMap[province.id]
        }

        if (_province.children.length === 0) {
            delete _province.children
        }

        res.push(_province)
    })


    return res
}