import unittest
import pandas as pd
import os

from main import load_data, add_full_name, categorize_age_groups ,calculate_price_by_age, merge_datasets, plot_chart, save_files

class TestChallenge(unittest.TestCase):
  
  def setUp(self):
    self.customers_df, self.purchases_df = load_data()

  def test_load_data(self):
    """Tests the load_data() function."""
    self.assertEqual(len(self.customers_df), 50000)
    self.assertEqual(len(self.purchases_df), 50000)

  def test_add_full_name(self):
    """Tests the add_full_name() function."""
    customers_df = add_full_name(self.customers_df)
    customers_df = categorize_age_groups(customers_df)
    
    self.assertEqual(customers_df['full_name'].iloc[0], 'Afqft Upuoxrm')
    self.assertEqual(customers_df['age_group'].iloc[0], 'Middle-aged')

  def test_merge_datasets(self):
    """Tests the merge_datasets() function."""
    combined_df = merge_datasets(self.customers_df, self.purchases_df)

    self.assertEqual(len(combined_df), 50000)

  def calculate_price_by_age(self):
    """Tests the calculate_price_by_age() function."""
    customers_df = categorize_age_groups(self.customers_df)
    combined_df = merge_datasets(customers_df, self.purchases_df)
    age_group_spending = calculate_price_by_age(combined_df)

    self.assertEqual(age_group_spending.index[0], 'Middle-aged')
    self.assertEqual(age_group_spending.values[0], 13424403)

  def test_visualization(self):
    """Tests the visualization() function."""
    customers_df = categorize_age_groups(self.customers_df)
    combined_df = merge_datasets(customers_df, self.purchases_df)
    age_group_spending = calculate_price_by_age(combined_df)
    plot_chart(age_group_spending)

    self.assertTrue(os.path.exists('total_spending.png'))

  def test_save_files(self):
    """ Test the save_files() function"""
    customers_df = categorize_age_groups(self.customers_df)
    combined_df = merge_datasets(customers_df, self.purchases_df)
    age_group_spending = calculate_price_by_age(combined_df)
    save_files(combined_df,age_group_spending)

    self.assertTrue(os.path.exists('combined_data.csv'))
    self.assertTrue(os.path.exists('age_group_spending.csv'))

if __name__ == '__main__':
    unittest.main()