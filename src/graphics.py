from pathlib import Path
import matplotlib.pyplot as plt


def create_charts(df):
    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)

    paths = []

    device_counts = df["device_type"].value_counts()
    plt.figure(figsize=(8, 5))
    device_counts.plot(kind="bar", color="steelblue")
    plt.title("Популярность устройств")
    plt.ylabel("Количество заказов")
    plt.tight_layout()
    p1 = out_dir / "device_counts.png"
    plt.savefig(p1)
    plt.close()
    paths.append(str(p1))

    gender_avg = df.groupby("gender")["order_amount"].mean()
    plt.figure(figsize=(6, 4))
    gender_avg.plot(kind="bar", color="darkorange")
    plt.title("Средний чек по полу")
    plt.ylabel("Сумма заказа")
    plt.tight_layout()
    p2 = out_dir / "gender_avg_amount.png"
    plt.savefig(p2)
    plt.close()
    paths.append(str(p2))

    monthly = df.copy()
    monthly["month"] = monthly["date"].dt.to_period("M").astype(str)
    monthly_avg = monthly.groupby("month")["order_amount"].mean()
    plt.figure(figsize=(10, 4))
    monthly_avg.plot(kind="line", marker="o", color="green")
    plt.title("Средний чек по месяцам")
    plt.ylabel("Сумма заказа")
    plt.xticks(rotation=45)
    plt.tight_layout()
    p3 = out_dir / "monthly_avg_amount.png"
    plt.savefig(p3)
    plt.close()
    paths.append(str(p3))

    return paths