# -*- coding: utf-8 -*-
import sqlite3


def get_product_id(product_name):
    conn = sqlite3.connect('mrp.s3db')
    cu = conn.cursor()
    product_id = cu.execute("SELECT product_id FROM product WHERE product_name = '%s'" % product_name).fetchall()[0][0]
    return product_id


def insert_new_order(order_date, product_id, product_quantity):  # table product, material and relation
    conn = sqlite3.connect('mrp.s3db')
    conn.execute("INSERT INTO plan (order_date, product_id, product_quantity) VALUES ('%s', '%s', '%f')" % (order_date, product_id, product_quantity))
    conn.commit()
    conn.close()


def main():
    while True:
        print('= ' * 25)
        order_date = input('生产日期(xxxx-xx-xx):')
        if order_date is not '':
            while True:
                print('- ' * 15)
                product_name = input('    产品名(务必确保是已经录入过的产品):')
                '''
                增加判断数据库中是否有该产品，如果没有则返回名称类似的
                '''
                if product_name is not '':
                    product_quantity = float(input('    产量:'))
                    product_id = get_product_id(product_name)
                    insert_new_order(order_date, product_id, product_quantity)
                else:
                    break
        else:
            break

if __name__ == '__main__':
    main()
