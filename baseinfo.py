# -*- coding: utf-8 -*-
import sqlite3


def insert_new_product(product_name):
    conn = sqlite3.connect('mrp.s3db')
    cu = conn.cursor()
    max_product_id = cu.execute("SELECT MAX(product_id) FROM product").fetchall()[0][0]
    product_id = 'P' + str(int(max_product_id[1:]) + 1)
    conn.execute("INSERT INTO product (product_name, product_id) VALUES ('%s', '%s')" % (product_name, product_id))
    conn.commit()
    conn.close()
    return product_id


def insert_new_material(material_name, is_color):
    conn = sqlite3.connect('mrp.s3db')
    cu = conn.cursor()
    max_material_id = cu.execute("SELECT MAX(material_id) FROM material").fetchall()[0][0]
    material_id = 'M' + str(int(max_material_id[1:]) + 1)
    conn.execute("INSERT INTO material (material_name, material_id, is_color) VALUES ('%s', '%s', '%s')" % (material_name, material_id, is_color))
    conn.commit()
    conn.close()
    return material_id


def insert_new_relation(product_id, material_id, weight_per_ton):
    conn = sqlite3.connect('mrp.s3db')
    conn.execute("INSERT INTO relation (product_id, material_id, weight_per_ton) VALUES ('%s', '%s', '%s')" % (product_id, material_id, weight_per_ton))
    conn.commit()
    conn.close()


def main():    
    while True:
        print('= ' * 25)
        product_name = input('产品名称:')
        if product_name is not '':
            product_id = insert_new_product(product_name)
            while True:
                print('- ' * 15)
                material_name = input('    原料名称:')
                if material_name is not '':
                    weight_per_ton = input('      每2吨 %s 使用的 %s 重量:' % (product_name, material_name))
                    try_find_name = sqlite3.connect('mrp.s3db')\
                        .cursor().execute("SELECT material_name FROM material Where material_name = '%s'" % material_name)\
                        .fetchall()
                    if try_find_name == []:
                        is_or_not_color = input('      是否色素(1/0):')
                        if is_or_not_color == 1:
                            is_color = 1
                        else:
                            is_color = 0
                        material_id = insert_new_material(material_name, is_color)
                        insert_new_relation(product_id, material_id, weight_per_ton)
                    else:
                        material_id = sqlite3.connect('mrp.s3db')\
                            .cursor().execute("SELECT material_id FROM material WHERE material_name = '%s'" % material_name)\
                            .fetchall()[0][0]
                        insert_new_relation(product_id, material_id, weight_per_ton)
                else:
                    break
        else:
            break

if __name__ == '__main__':
    main()
