import pandas as pd


if __name__ == '__main__':
    print()
    print('-------------------------------------------------------------------------------')
    print()
    salesDataDF = pd.read_csv('sales_16-19.csv')
    pd.set_option('display.max_rows', 500)
    print('First 5 rows:')
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

    print('Product with most bottles sold per zip code:')
    print(maxesDF)
    print()
    print('-------------------------------------------------------------------------------')
    print()








