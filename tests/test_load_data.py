import pandas as pd
from src.load_data import load_orders


def test_load_orders_shape():
    df = load_orders()
    assert len(df) >= 100


def test_load_orders_columns():
    df = load_orders()
    required = {"order_id", "customer_id", "age", "gender", "device_type", "order_amount", "rating", "delivery_days"}
    assert required.issubset(set(df.columns))


def test_repeat_customer_boolean():
    df = load_orders()
    assert df["is_repeat_customer"].dropna().isin([True, False]).all()