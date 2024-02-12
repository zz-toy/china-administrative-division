// 单级别数据 ====================================================

export const getZnProvinceTree = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const provinceList = []

    list.forEach((province) => {
        provinceList.push({
            label: province.name,
            value: province.name,
        })
    })

    const res = {
        errcode:200,
        errmsg:"请求成功",
        data: provinceList
    }

    return res
}

// 级联数据 ====================================================

export const znCascadeTree = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const provinceList = []
    const cityList = []
    const countyList = []

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

    const cityIdToCountyMap = {}
    if (countyList.length > 0) {
        countyList.forEach((county) => {
            if (!cityIdToCountyMap[county.city_id]) {
                cityIdToCountyMap[county.city_id] = []
            }

            const _county = {
                label: county.name,
                value: county.name,
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

    const cascaderList = []
    provinceList.forEach((province) => {
        const _province = {
            label: province.name,
            value: province.name,
            children: []
        }

        if (provinceIdToCityMap && provinceIdToCityMap[province.id]) {
            _province.children = provinceIdToCityMap[province.id]
        }

        if (_province.children.length === 0) {
            delete _province.children
        }

        cascaderList.push(_province)
    })

    const res = {
        errcode:200,
        errmsg:"请求成功",
        data: cascaderList
    }

    return res
}