// 单级别数据 ====================================================

export const getProvinceCsvList = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const provinceCsvList = []

    list.forEach((province) => {
        provinceCsvList.push([province.code, `"${province.name}"`])
    })

    return buildCsv(provinceCsvList, ["code", "name"])
}

export const getCityCsvList = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const cityCsvList = []

    list.forEach((city) => {
        cityCsvList.push([city.code, `"${city.name}"`, city.province_code])
    })

    return buildCsv(cityCsvList,["code", "name", "province_code"])
}

export const getCountyCsvList = (list = []) => {
    if (!list || !Array.isArray(list) || list.length === 0) {
        return []
    }

    const countyCsvList = []

    list.forEach((county) => {
        countyCsvList.push([county.code, `"${county.name}"`, county.province_code, county.city_code])
    })

    return buildCsv(countyCsvList, ["code", "name", "province_code", "city_code"])
}

export const buildCsv = (data = [], header = []) => {
    // '\n' 表示一行的结束，','表示数据依次放在新的单元格
	let res = ""
    if (header && Array.isArray(header) && header.length > 0) {
        res = header.join(',')+"\n"
    }

    if (data && Array.isArray(data) && data.length > 0) {
        res += data.map((item) => {
			return item.join(',')
		}).join("\n");
    }

	// encodeURIComponent解决中文乱码
    return res;
}