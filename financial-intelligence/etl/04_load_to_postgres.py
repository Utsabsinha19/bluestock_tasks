from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://username:password@localhost:5432/finance_db")

def load(file, table):
    df = pd.read_csv(file)
    df.to_sql(table, engine, if_exists='append', index=False)
    print(f"{table} loaded")

load("data/clean/companies.csv", "dim_company")
load("data/clean/profitandloss.csv", "fact_profit_loss")
load("data/clean/balancesheet.csv", "fact_balance_sheet")
load("data/clean/cashflow.csv", "fact_cash_flow")