import pandas as pd

df = pd.read_csv('Module 1-2. Python для анализа данных/files/orders.csv')
unique_cities_count = df.city_id.nunique()

unique_vendor_id_with_fish_count = df[df.spec == 'Рыба'].vendor_id.nunique()

types = df.dtypes

float64_count_attributes = types[types == 'float64'].count()

orders_less_20 = df[(df.vendor_id == 40065) & (df.successful_orders < 20)].date.nunique()


print(unique_cities_count)
print(unique_vendor_id_with_fish_count)
print(float64_count_attributes)
print(orders_less_20)
