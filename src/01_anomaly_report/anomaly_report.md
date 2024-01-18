## Main Analysis Insights

After conducting an exploratory data analysis on the information provided about Orders, Returns and People, the following key insights and attention points have been identified:

- **Returns Table:** Returned column only contains YES values. Did all the products returned successfully or there is a problem here?
- **Orders Table:** Sales has a huge standard deviation, presence of outliers.
- **Orders Table:** Profit has also a huge stardard deviation, presence of outliers.
- **Orders Table:** Order ID can be repeated with different items of the same order, the table is expanded on orders and items
- **Orders Table:** All the clientd id are correct linked with one client name, but they can change their addresses along the orders.
- **Orders Table:** All the clientd id are correct linked with one client name, but they can change their addresses along the orders.
- **Orders Table:** There is a different name for the same Product ID, with different prices and profits. Looking deeper at this, we can see that these products were sold in distinct regions, maybe the primary key is composed by product id + region, but it will be more intuitive if the product id was unique for each product.
- **Orders Table:** Usually the discount is applied with a higher quantity, but we can see that correlation between them is very weak. Is the discount being applied correctly?
- **Orders Table:** Higher sales amount is correlated with a higher profit
- **Orders Table:** There are products with a high value being sold and low profit, contradicting the correlation, there is any error?
- **Orders Table:** The products must have been sold with different prices to different customers, or there is an error on the unit price.
- **Orders Table:** The only strange profit value found was on product TEC-MA-10000418, that had always a very negative profit and has one operation with a positive profit.

## KPIs and Metrics

To keep searching for anomalies, there are some KPIs and Metrics that could be used:

- **Sales, Profit, Quantity and Discounts:** As can observed in the dataset, there are a lot of outliers on these dimensions. Track total sales/profit/discount/quantity over time and identify significant deviations, combine this with the sasonality that is clearly observable in the Order Date histogram can keep the business healthy. Create some feature engineering, like calculate the profit margin (Sales/Profit), unity price (Sales/Quantity) and unity price ignoring discount (Sales * (1 + Discount)/Quantity) can help identifing anomalies as well.

- **Order Time:** create metrics like average date between order and ship dates can help identify anomalies on deliveries or processing issues.

- **Geographic Insights:** create filters for regions and states, to compare them and check if there is any problem on specific region or state. You can monitor delivering status for clients locations as well, to see unusual patterns.

- **Customers:** create customers analysis to understand they behaviour, and create a return rate for each customer can help detecting anomalies.

- **Outliers Detection:** create metrics to identify outliers and investigate they extreme cases.