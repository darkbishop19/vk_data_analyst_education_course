#чему равна общая выручка с точностью до 2 знаков после запятой
import sqlite3
import pandas as pd
connect = sqlite3.connect('my_online_store.db')
cursor = connect.cursor()
query = (
'''SELECT  sum(total_price)
FROM orders
''')
products = cursor.execute(query)
products_df = pd.DataFrame(products)
print(products_df)
#Ответ: 145545,39
connect.commit()
connect.close()