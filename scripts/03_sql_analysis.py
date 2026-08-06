import sqlite3
import pandas as pd

# connect to database
conn=sqlite3.connect('database/sales.db')

query1='''
SELECT COUNT(*) AS total_orders
from sales;
'''
print(pd.read_sql_query(query1,conn))

query2='''
SELECT sum(sales) as total_sales
from sales;
'''
print(pd.read_sql_query(query2,conn))

query3='''
SELECT round(sum(profit),2) as total_profit
from sales;
'''
print(pd.read_sql_query(query3,conn))

query4='''
SELECT round(avg(sales),2) as average_sales
from sales;
'''
print(pd.read_sql_query(query4,conn))

query5='''
SELECT max(sales) as highest_sale
from sales;
'''
print(pd.read_sql_query(query5,conn))

query6='''
SELECT min(sales) as lowest_sale
from sales;
'''
print(pd.read_sql_query(query6,conn))

query7='''
SELECT category,round(sum(sales),2) as total_sales
from sales
GROUP BY category
'''
print(pd.read_sql_query(query7,conn))

query8='''
SELECT category,round(sum(profit),2) as total_profit
from sales
GROUP BY category
'''
print(pd.read_sql_query(query8,conn))

query9='''
SELECT region, round(sum(sales),2) as total_sales
from sales
GROUP BY region
'''
print(pd.read_sql_query(query9,conn))

query10='''
SELECT region, round(sum(profit),2) as total_profit
from sales
GROUP BY region
'''
print(pd.read_sql_query(query10,conn))

query11='''
SELECT "Customer Name",round(sum(sales),2) as total_sales
from sales
GROUP BY "Customer Name"
Order by total_sales desc
limit 10;
'''
print(pd.read_sql_query(query11,conn))

query12='''
SELECT "Product Name",round(sum(sales),2) as total_sales
from sales
group by "Product Name"
order by total_sales desc
limit 10;
'''
print(pd.read_sql_query(query12,conn))

query13='''
SELECT "state", round(sum(profit),2) as total_profit
from sales
group by "state"
order by total_profit desc
limit 10;
'''
print(pd.read_sql_query(query13,conn))

query14='''
SELECT category,round(avg(profit)) as average_profit
from sales
group by category
order by average_profit desc;
'''
print(pd.read_sql_query(query14,conn))

query15='''
SELECT "ship mode",round(sum(sales)) as total_sales
from sales
group by "ship mode"
order by total_sales desc;
'''
print(pd.read_sql_query(query15,conn))

query16='''
SELECT round(sum(sales),2) as total_sales
from sales
where category="Technology";
'''
print(pd.read_sql_query(query16,conn))

query17='''
SELECT round(sum(profit),2) as total_profit
from sales
where region="West";
'''
print(pd.read_sql_query(query17,conn))

query18='''
SELECT count(*) as High_discount
from sales
where discount>0.2;
'''
print(pd.read_sql_query(query18,conn))

query19='''
SELECT count(*) as loss_orders
from sales
where profit<0;
'''
print(pd.read_sql_query(query19,conn))

query20='''
SELECT round(sum(sales),2) as tech_west_sales
from sales
where category='Technology' and region='West';
'''
print(pd.read_sql_query(query20,conn))

query21='''
SELECT count(*) as orders
from sales
where category='Furniture' or category='Office Supplies';
'''
print(pd.read_sql_query(query21,conn))

query22='''
SELECT round(avg(sales),2) as average_2017
from sales
where year='2017';
'''
print(pd.read_sql_query(query22,conn))

query23='''
SELECT category,round(sum(sales),2) as total_sales
from sales
group by category
having total_sales>700000
'''
print(pd.read_sql_query(query23,conn))

query24='''
SELECT "Customer Name",round(sum(sales),2) as total_purchase
from sales
group by "Customer Name"
having total_purchase>10000
'''
print(pd.read_sql_query(query24,conn))

query25='''
SELECT "state", round(avg(profit),2) as average_profit
from sales
group by "state"
having average_profit>30
'''
print(pd.read_sql_query(query25,conn))
# To check categories
# q='''
# select distinct category from sales
# '''
# print(pd.read_sql_query(q,conn))

q1='''
SELECT "Customer Name",round(sum(profit),2) as total_profit 
from sales
group by "Customer Name"
order by total_profit desc
limit 5;
'''
print(pd.read_sql_query(q1,conn))

q2='''
SELECT "sub-category",round(sum(sales),2) as total_sales
from sales
group by "sub-category"
order by total_sales desc;
'''
print(pd.read_sql_query(q2,conn))

q3='''
SELECT category,round(avg((profit/nullif(sales,0))*100),2) as average_profit_margin
from sales
group by category;
'''
print(pd.read_sql_query(q3,conn))


conn.close()
