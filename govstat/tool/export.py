# -*- coding:utf-8 -*-
from tool.export.province import export_province
from tool.export.city import export_city
from tool.export.county import export_county
from tool.export.pc import export_pc
from tool.export.pcc import export_pcc


def main():
    export_province()
    export_city()
    export_county()
    export_pc()
    export_pcc()
    print("数据更新成功")


if __name__ == "__main__":
    main()
