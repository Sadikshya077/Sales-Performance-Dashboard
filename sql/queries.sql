
-- Query 1: Total Orders
SELECT COUNT(*) AS total_orders
from sales;

-- Query 2: Total Sales
SELECT sum(sales) as total_sales
from sales;

-- Query 3: Total Profit
SELECT round(sum(profit),2) as total_profit
from sales;

-- Query 4: Average sales per order
SELECT round(avg(sales),2) as average_sales
from sales;

-- Query 5: Highest sale
SELECT max(sales) as highest_sale
from sales;

-- Query 6: Lowest sale
SELECT min(sales) as lowest_sale
from sales;

-- group by
-- Query 7: sales by category
SELECT category,round(sum(sales),2) as total_sales
from sales
GROUP BY category

-- Query 8: profit by category
SELECT category,round(sum(profit),2) as total_profit
from sales
GROUP BY category

-- Query 9: sales by region
SELECT region, round(sum(sales),2) as total_sales
from sales
GROUP BY region

-- Query 10: profit by region
SELECT region, round(sum(profit),2) as total_profit
from sales
GROUP BY region

-- Order by
-- Query 11: Top 10 customers by sale
SELECT "Customer Name",round(sum(sales),2) as total_sales
from sales
GROUP BY "Customer Name"
Order by total_sales desc
limit 10;

-- Query 12: Top 10 Products
SELECT "Product Name",round(sum(sales),2) as total_sales
from sales
group by 'Product Name'
order by total_sales desc
limit 10;

-- Query 13: Most Profitable States
SELECT 'state', round(sum(profit),2) as total_profit
from sales
group by 'state'
order by total_profit desc
limit 10;

-- Query 14: Which categories have the highest average profit?
SELECT category,round(avg(profit)) as average_profit
from sales
group by category
order by average_profit desc;

-- Query 15: Which shipping mode is used the most?
SELECT 'ship mode',round(sum(sales)) as total_sales
from sales
group by 'ship mode'
order by total_sales desc;

-- Where
-- Query 16: Total Sales for Technology Category
SELECT round(sum(sales),2) as total_sales
from sales
where category="Technology";

-- Query 17: Total Profit from West Region
SELECT round(sum(profit),2) as total_profit
from sales
where region="West";

-- Query 18: Orders with High Discount
SELECT count(*) as High_discount
from sales
where discount>0.2;

-- Query 19: Loss Making Orders
SELECT count(*) as loss_orders
from sales
where profit<0;

-- Query 20: Technology Products in the West Region
SELECT round(sum(sales),2) as tech_west_sales
from sales
where category="Technology" and region="West";

-- Query 21: Furniture OR Office Supplies
SELECT count(*) as orders
from sales
where category="furniture" or category="office supplies";

-- Query 22: Average Sales in 2017
SELECT round(avg(sales),2) as average_2017
from sales
where year="2017";

-- Having 
-- Where is used to filter individual rows while Having filters in group
-- Query 23: Categories with total sales greater than 700000.

SELECT category,round(sum(sales),2) as total_sales
from sales
group by category
having total_sales>700000

-- Query 24: Customers whose total purchases are greater than 10000.
SELECT "Customer Name",round(sum(sales),2) as total_purchase
from sales
group by "Customer Name"
having total_purchase>10000

-- Query 25: States with average profit greater than 30.
SELECT "state", round(avg(profit),2) as average_profit
from sales
group by "state"
having average_profit>30

-- Questions
-- q1: Top 5 customers by profit.
-- We give double quote for column name while single/double for category inside the column
SELECT "Customer Name",round(sum(profit),2) as total_profit 
from sales
group by "Customer Name"
order by total_profit desc
limit 5;

-- q2: Which Sub-Category generated the highest sales?
SELECT "sub-category",round(sum(sales),2) as total_sales
from sales
group by "sub-category"
order by total_sales desc;

-- q3: Calculate the average profit margin by Category.
SELECT category,round(avg((profit/nullif(sales,0))*100),2) as average_profit_margin
from sales
group by category;