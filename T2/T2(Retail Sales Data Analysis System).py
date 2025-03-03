# Name : George Malak Magdy
# Date : 26/2/2025
# Task : 2 retail sales data analysis
import numpy as np
import pandas as pd

# Phase 1 collect and store the data
def loadDT():
    while True:
        # File : sales_dataset.csv
        dpath = input("Enter the path to your sales data file: ")
        print("Loading data...")
        try:
            dt = pd.read_csv(dpath)
            print(f"Data loaded! Total transactions: {len(dt)}")
            return dt
        except FileNotFoundError:
            print("Error : File not found try again !! please check from folder's path.")
        except pd.errors.EmptyDataError:
            print("Error: File is empty!! please provide a valid sales data file.")
        except Exception as e:
            print(f" Unexpected error: {e}")
# Phase 2 calculations on the data
def Calculations(df):
    df['TransactionPrice'] = df['UnitPrice'] * df['Quantity']
    total_rev = tot_revenue(df['TransactionPrice'])
    avg_sale = avr_sale(df['TransactionPrice'])
    high_low = high_low_sale(df)
    best_product = best_sell(df)
    # send as tuple
    return total_rev, avg_sale, high_low[0], high_low[1], high_low[2], high_low[3], best_product
def tot_revenue(Transection):
    return np.sum(Transection)
def avr_sale(Transection):
    return np.mean(Transection)
def high_low_sale(df):
    hig_idx = df["TransactionPrice"].idxmax()
    lw_idx = df["TransactionPrice"].idxmin()
    high = df.loc[hig_idx, "TransactionPrice"]
    low = df.loc[lw_idx, "TransactionPrice"]
    hig_product = df.loc[hig_idx, 'Product']
    lw_product = df.loc[lw_idx, 'Product']
    return high, low, hig_product, lw_product
def best_sell(df):
    return df.groupby('Product')['Quantity'].sum().idxmax()
# Display requirements
def display(df, metrics):
    total_rev, avg_sale, high_sal, low_sal, high_prod, lowe_prod, best_prod = metrics
    print("\nRetail Sales Report")
    print("-" * 30)
    print(f"Total Transactions: {len(df)}")
    print(f"Total Revenue: ${total_rev:,.2f}")
    print(f"Average Sale: ${avg_sale:,.2f}")
    print(f"Highest Sale: ${high_sal:,.2f} (Product: {high_prod})")
    print(f"Lowest Sale: ${low_sal:,.2f} (Product: {lowe_prod})")
    print(f"Best-Selling Product: {best_prod}")
# Main Programme
def main():
    df = loadDT()
    metrics = Calculations(df)
    display(df, metrics)
if __name__ == '__main__':
    main()