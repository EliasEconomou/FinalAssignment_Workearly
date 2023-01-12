import matplotlib.pyplot as plt
import pandas as pd


def spaces():
    print()
    print('-------------------------------------------------------------------------------')
    print()


if __name__ == '__main__':
    spaces()
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
    spaces()

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
    spaces()

    # Finally let's plot the results
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.3,
                        hspace=0.4)
    maxesDF['item_number'] = maxesDF['item_number'].astype(str)
    maxesDF['zip_code'] = maxesDF['zip_code'].astype(str)
    classes = pd.Categorical(maxesDF['item_number']).codes

    plt.subplot(1, 2, 1)
    plt.xlabel('zip code')
    plt.ylabel('bottles sold')
    plt.grid(color='g', linestyle='--', linewidth=0.1)
    for i, j, k in zip(maxesDF['item_number'], maxesDF['zip_code'], maxesDF['bottles_sold']):
        plt.scatter(j,
                    k,
                    label=i)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 8})
    plt.xticks(fontsize=8, rotation=50)
    plt.title('Product with max bottles sold per zip code')

    sales_perStore["store_number"] = sales_perStore["store_number"].astype(str)
    sales_perStore["percent_of_total"] = sales_perStore["percent_of_total"].round(2)
    sales_perStore = sales_perStore.sort_values(by=['percent_of_total'], ascending=True)
    plt.subplot(1, 2, 2)
    y = sales_perStore["store_number"]
    x = sales_perStore["percent_of_total"]
    bars = plt.barh(y, x)
    plt.ylabel('store number')
    plt.xlabel('sales percentage')
    plt.title('Percentage of sales per store')
    plt.bar_label(bars)

    plt.show()







