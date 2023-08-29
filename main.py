import pandas as pd
import matplotlib.pyplot as plt

import multiprocessing as mp

def load_data():
    """Load datasets

    Returns:
        df (pandas.DataFrame): Customers dataset
        df (pandas.DataFrame): Purchases dataset
    """
    customers_df = pd.read_csv("./customers.csv")
    purchases_df = pd.read_csv("./purchases.csv")

    return customers_df,purchases_df

def add_full_name(df):
    """Generating full name column

    Args:
        df (pandas.DataFrame): Customers dataset

    Returns:
        pandas.DataFrame: Customers dataset with fullname
    """
    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    return df

def categorize_age_groups(df):
    """Categorize customers into age groups

    Args:
        df (pandas.DataFrame): Customers dataset

    Returns:
        pandas.DataFrame: Customers dataset after age categories 
    """
    df['age_group'] = df['age'].apply(
    lambda x: 'Young' if x >= 18 and x < 30 else 'Middle-aged' if x >= 30 and x< 45 else 'Senior')
    return df

def merge_datasets(cust_df, purc_df):
    """Merging the customers and purchases datasets

    Args:
        cust_df (pandas.DataFrame): Customers dataset
        purc_df (pandas.DataFrame): Purchases dataset

    Returns:
        pandas.DataFrame: Combined dataframe
    """
    final_df = cust_df.merge(purc_df, on='customer_id')
    return final_df

def calculate_price_by_age(df):
    """Computing the total spending for each age group.

    Args:
        df (pandas.DataFrame): Combined dataframe

    Returns:
        pandas.DataFrame: _description_
    """
    # Group the DataFrame by age and sum the amount column
    final_df = df.groupby('age_group')['price'].sum().reset_index()
    return final_df

# def calculate_price_by_age(df):
#     # using multiprocessing (for large datasets)

#     grouped = df.groupby('age_group')
#     pool = mp.Pool(mp.cpu_count())
#     results = pool.map(sum_b, [group for name, group in grouped])
#     final_df = pd.DataFrame({'age_group': [name for name, group in grouped],
#                              'price': results})
#     pool.close()
#     pool.join()
#     return final_df

# def sum_b(group):
#     return group['price'].sum()

def plot_chart(df):
    """Plotting the grouped dataset

    Args:
        df (pandas.DataFrame): Combined dataframe
    """

    plt.bar(df['age_group'], df['price'])
    plt.xlabel('Age Group')
    plt.ylabel('Total Spending')
    plt.title('Total Spending by Age Group')
    plt.savefig('total_spending.png')

def save_files(merged_df,age_group_spending):
    """Saving the result datasets

    Args:
        merged_df (pandas.DataFrame) : Combined dataframe
        age_group_spending (pandas.DataFrame): Final Grouped dataframe
    """
    merged_df.to_csv('./combined_data.csv')
    age_group_spending.to_csv('./age_group_spending.csv')

if __name__ == '__main__':
    #loading  the csv files
    customers, purchases = load_data()

    # adding fullnames and categorizing age
    customers = add_full_name(customers)
    customers = categorize_age_groups(customers)
    #merging datasets
    merged_df = merge_datasets(customers,purchases)

    if customers.shape[0] == purchases.shape[0] == merged_df.shape[0]:
        print ("No loss happened during merge")

    #Compute the total spending for each age group
    age_group_spending = calculate_price_by_age(merged_df)
    #ploting results
    plot_chart(age_group_spending)
    # save_files(merged_df,age_group_spending)
    print ("Completed! All files have been saved")
