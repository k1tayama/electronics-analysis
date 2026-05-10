import numpy as np
import pandas as pd
from functools import lru_cache


def chunked(iterable, size=25):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


def row_iterator(df):
    for _, row in df.iterrows():
        yield row


def get_basic_stats(df):
    total_orders = len(df)
    avg_amount = np.mean(df["order_amount"])
    median_amount = np.median(df["order_amount"])
    avg_delivery = np.mean(df["delivery_days"])
    avg_rating = np.mean(df["rating"])
    return {
        "total_orders": int(total_orders),
        "avg_amount": round(float(avg_amount), 2),
        "median_amount": round(float(median_amount), 2),
        "avg_delivery": round(float(avg_delivery), 2),
        "avg_rating": round(float(avg_rating), 2),
    }


def get_top_device(df):
    return df.groupby("device_type")["order_amount"].agg(["count", "mean"]).sort_values(by="count", ascending=False).head(1)


def get_weekday_insights(df):
    temp = df.copy()
    temp["weekday"] = temp["date"].dt.day_name()
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    result = temp.groupby("weekday")["order_amount"].mean().reindex(order)
    return result


def get_gender_insights(df):
    return df.groupby("gender").agg(
        orders=("order_id", "count"),
        avg_amount=("order_amount", "mean"),
        avg_rating=("rating", "mean"),
        avg_delivery=("delivery_days", "mean")
    )


def get_repeat_customer_insights(df):
    return df.groupby("is_repeat_customer").agg(
        orders=("order_id", "count"),
        avg_amount=("order_amount", "mean"),
        avg_rating=("rating", "mean"),
        avg_delivery=("delivery_days", "mean")
    )


def get_age_correlation(df):
    return float(df["age"].corr(df["order_amount"]))


@lru_cache(maxsize=32)
def cached_device_rankings(device_tuple):
    s = pd.Series(device_tuple)
    return s.value_counts().to_dict()


def build_report(df):
    stats = get_basic_stats(df)
    top_device = df["device_type"].value_counts().idxmax()
    weekday_means = get_weekday_insights(df)
    best_day = weekday_means.idxmax()
    worst_day = weekday_means.idxmin()
    gender = get_gender_insights(df)
    repeat = get_repeat_customer_insights(df)
    corr = get_age_correlation(df)

    top_gender = gender["avg_amount"].idxmax()
    repeat_label = "повторные" if repeat.loc[True, "avg_amount"] > repeat.loc[False, "avg_amount"] else "новые"
    best_delivery_group = "повторные покупатели" if repeat["avg_delivery"].idxmin() == True else "новые покупатели"

    lines = [
        f"Всего заказов: {stats['total_orders']}.",
        f"Средний чек: {stats['avg_amount']}, медиана: {stats['median_amount']}.",
        f"Самое популярное устройство: {top_device}.",
        f"Самый выгодный день недели по среднему чеку: {best_day}, самый слабый: {worst_day}.",
        f"Самая высокая средняя сумма заказов у группы: {top_gender}.",
        f"Связь между возрастом и суммой заказа слабая: коэффициент корреляции {corr:.3f}.",
        f"{repeat_label.capitalize()} покупатели тратят больше в среднем; лучшая доставка у группы: {best_delivery_group}.",
    ]
    return "\n".join(lines)