from pathlib import Path
import pandas as pd
import functools
import time

DATA_PATH = Path("data") / "electronics_orders.csv"


def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Вызов: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Завершено: {func.__name__}")
        return result
    return wrapper


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIME] {func.__name__}: {end - start:.4f} сек")
        return result
    return wrapper


@log_calls
@timer
def load_orders(path: Path = DATA_PATH):
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    if "date" not in df.columns and "orderdate" in df.columns:
        df["date"] = pd.to_datetime(df["orderdate"], errors="coerce")
    elif "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    else:
        df["date"] = pd.to_datetime(df.iloc[:, 1], errors="coerce")

    rename_map = {
        "orderid": "order_id",
        "customerid": "customer_id",
        "age": "age",
        "gender": "gender",
        "city": "city",
        "devicetype": "device_type",
        "orderamount": "order_amount",
        "rating": "rating",
        "isrepeatcustomer": "is_repeat_customer",
        "deliverydays": "delivery_days",
    }
    df = df.rename(columns=rename_map)

    if "order_amount" in df.columns:
        df["order_amount"] = pd.to_numeric(df["order_amount"], errors="coerce")
    if "rating" in df.columns:
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    if "delivery_days" in df.columns:
        df["delivery_days"] = pd.to_numeric(df["delivery_days"], errors="coerce")
    if "age" in df.columns:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")

    if "is_repeat_customer" in df.columns:
        df["is_repeat_customer"] = df["is_repeat_customer"].astype(str).str.strip().str.lower().map(
            {"yes": True, "no": False}
        )

    return df
