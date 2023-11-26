#чему равна общая выручка с точностью до 1 знака после запятой
import sqlite3
import pandas as pd
connect = sqlite3.connect('my_online_store.db')
cursor = connect.cursor()
query = (
'''SELECT  sum(total_price)
FROM orders
''')
# products = cursor.execute(query)
# products_df = pd.DataFrame(products)
# print(products_df)
dfalbum = pd.read_sql_query(query, connect)
print(dfalbum)
#Ответ: 145545,4
connect.commit()
connect.close()