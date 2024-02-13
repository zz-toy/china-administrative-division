# -*- coding:utf-8 -*-
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from export.province import export_province
from export.city import export_city
from export.county import export_county
from export.pc import export_pc
from export.pcc import export_pcc


def main():
    export_province()
    export_city()
    export_county()
    export_pc()
    export_pcc()
    print("数据更新成功")


if __name__ == "__main__":
    main()
