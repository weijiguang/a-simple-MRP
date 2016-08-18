# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('mrp.s3db')


def get_product_sum(product_id, start_date, end_date):
    # conn = sqlite3.connect('mrp.s3db')
    plan = conn.execute("SELECT product_quantity FROM plan WHERE product_id = '%s' AND order_date BETWEEN '%s' AND '%s'" % (product_id, start_date, end_date))
    product_sum = 0
    for row in plan:
        product_quantity = row[0]
        product_sum += product_quantity
    # conn.close()
    return product_sum


def get_weight_per_ton(material_id, product_id):
    # conn = sqlite3.connect('mrp.s3db')
    cu = conn.cursor()
    record = cu.execute("SELECT weight_per_ton FROM relation WHERE material_id = '%s' AND product_id = '%s'" % (material_id, product_id))
    w = record.fetchall()
    if w == []:
        weight_per_ton = 0
    else:
        weight_per_ton = w[0][0]
    # conn.close()
    return weight_per_ton


def main():
    # conn = sqlite3.connect('mrp.s3db')

    start_date = input('输入开始日期(xxxx-xx-xx):')
    if start_date == '':
        start_date = '0000-00-00'
    end_date = input('输入结束日期(xxxx-xx-xx):')
    if end_date == '':
        end_date = '9999-12-31'
    materials = conn.execute('SELECT material_id, material_name, is_color FROM material ORDER BY is_color, material_name')

    for row in materials:
        material_id = row[0]  # ******************************************************************
        material_name = row[1]
        product = conn.execute("SELECT product_id FROM product")
        material_sum = 0
        for row in product:
            product_id = row[0]  # ***************************************************************
            product_sum = get_product_sum(product_id, start_date, end_date)
            weight_per_ton = get_weight_per_ton(material_id, product_id)
            m_for_p = weight_per_ton * product_sum  # ********************************************
            if m_for_p != 0:
                # print(material_name, product_id, m_for_p)
                material_sum += m_for_p
        material_sum = round(material_sum, 3)
        print(material_name, material_sum)

    conn.close()

if __name__ == '__main__':
    main()
