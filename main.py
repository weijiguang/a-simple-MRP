# -*- coding: utf-8 -*-
import plan
import baseinfo
import solve

while True:
    print('1.每日生产情况录入\n2.新产品信息录入\n3.计算指定日期内原料消耗')
    i = input('请选择(1/2/3):')
    print('- ' * 25)
    if i == '1':
        plan.main()
    elif i == '2':
        baseinfo.main()
    else:
        if i == '3':
            solve.main()
