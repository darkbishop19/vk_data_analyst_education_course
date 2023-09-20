import pandas as pd

df = pd.read_csv('C:/Users/kaspe/Documents/Jupyter notebook files/orders.csv')
unique_cities = df.city_id.nunique()

fish_count = df[df.spec == 'Рыба'].vendor_id.nunique()

types = df.dtypes

float64_count_attributes = types[types == 'float64'].count()

orders_less_20 = df[(df.vendor_id == 40065) & (df.successful_orders < 20)].date.nunique()


print(unique_cities)
print(fish_count)
print(float64_count_attributes)
print(orders_less_20)