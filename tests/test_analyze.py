from src.load_data import load_orders
from src.analyze import (
    get_basic_stats,
    get_top_device,
    get_weekday_insights,
    get_gender_insights,
    get_age_correlation,
    build_report
)


def test_basic_stats():
    df = load_orders()
    stats = get_basic_stats(df)
    assert stats["total_orders"] >= 100
    assert stats["avg_amount"] > 0


def test_top_device():
    df = load_orders()
    result = get_top_device(df)
    assert not result.empty


def test_weekday_insights():
    df = load_orders()
    result = get_weekday_insights(df)
    assert len(result) == 7


def test_gender_insights():
    df = load_orders()
    result = get_gender_insights(df)
    assert not result.empty


def test_age_correlation():
    df = load_orders()
    corr = get_age_correlation(df)
    assert -1 <= corr <= 1


def test_report_contains_lines():
    df = load_orders()
    report = build_report(df)
    assert "Всего заказов" in report
    assert "Средний чек" in report