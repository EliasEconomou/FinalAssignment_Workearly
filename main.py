import pandas as pd


if __name__ == '__main__':
    print()
    print('-------------------------------------------------------------------------------')
    print()
    salesDataDF = pd.read_csv('sales_16-19.csv')
    pd.set_option('display.max_rows', 500)
    print('First 5 rows of dataset :')
    print(salesDataDF.head())
    print()

    # We'll get the number of bottles sold per item in each zip code
    groupedZipCodes = salesDataDF.groupby(['zip_code', 'item_number'])
    bottlesSold_perProduct_perZipCodeDF = groupedZipCodes.agg({'bottles_sold': 'sum'})

    # Reset the double index
    bottlesSold_perProduct_perZipCodeDF = bottlesSold_perProduct_perZipCodeDF.reset_index()

    # Finally sort rows by bottles sold for every group and keep the first meaning the max one
    maxesDF = bottlesSold_perProduct_perZipCodeDF.sort_values(['zip_code', 'bottles_sold'], ascending=False)\
        .groupby(['zip_code']).first()\
        .reset_index()

    print('Product (item) with most bottles sold per zip code:')
    print(maxesDF)
    print()
    print('-------------------------------------------------------------------------------')
    print()

    # Let's get sales per store
    groupedStores = salesDataDF.groupby(['store_number'])
    sales_perStore = groupedStores.agg({'sale_dollars': 'sum'})

    # Reset the index
    sales_perStore = sales_perStore.reset_index()

    # Compute total sales and create a new column with percentage
    sumSales = sum(sales_perStore['sale_dollars'])
    sales_perStore["percent_of_total"] = (sales_perStore["sale_dollars"] / sumSales) * 100
    print('Sales percentage per store :')
    print(sales_perStore)






