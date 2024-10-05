import pandas as pd

def load_csv_data():
    apt_info_df = pd.read_csv('data/apt_info.csv')
    apt_review_df = pd.read_csv('data/apt_review.csv')
    apt_trade_df = pd.read_csv('data/apt_trade.csv')
    return apt_info_df, apt_review_df, apt_trade_df