#у какого продукта наибольшее количество продаж
import sqlite3
import pandas as pd
connect = sqlite3.connect('my_online_store.db')
cursor = connect.cursor()
# query = (
# '''SELECT   p.product_name, s.count
# FROM products p
# LEFT JOIN
# (SELECT product_id, sum(quantity) as count
# FROM    orders
# GROUP BY    product_id
# ORDER BY    count desc
# LIMIT 1) s on p.product_id = s.product_id
# WHERE s.product_id is not null
# ''')

query = (
'''
SELECT distinct product_id, sum(quantity) as count
FROM    orders
GROUP BY    product_id
ORDER BY    count desc
''')
# products = cursor.execute(query)
# products_df = pd.DataFrame(products)
# print(products_df)
dfalbum = pd.read_sql_query(query, connect)
print(dfalbum)
#Ответ: HFvpNNVhmAUgDZ
connect.commit()
connect.close()