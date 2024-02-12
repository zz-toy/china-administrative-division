import FileSaver from 'file-saver'

export const getApiBaseUrl = () => {
    console.log(`${window.location.protocol}//${window.location.hostname}:6800`)
    return `${window.location.protocol}//${window.location.hostname}:6800`
}

export const getPcListApiUrl = () => {
    return `${getApiBaseUrl()}/pc/list`
}

export const getPccListApiUrl = () => {
    return `${getApiBaseUrl()}/pcc/list`
}

export const getProvinceListApiUrl = () => {
    return `${getApiBaseUrl()}/province/list`
}

export const getCityListApiUrl = () => {
    return `${getApiBaseUrl()}/city/list`
}

export const getCountyListApiUrl = () => {
    return `${getApiBaseUrl()}/county/list`
}

export const saveFile = (data, filename, type='application/json;charset=utf-8') => {
    if (!data || !filename) {
        return
    }

    const blob = new Blob([JSON.stringify(data, null, 2)], {
        type: type
    })

    try {
        FileSaver.saveAs(blob, filename)
    } catch (e) {
        console.log(e)
    }
}