import argparse
from src.load_data import load_orders
from src.analyze import build_report, get_basic_stats
from src.graphics import create_charts

def main():
    parser = argparse.ArgumentParser(
        prog="electronics-analysis",
        description="Анализ заказов электроники по CSV-файлу.",
        epilog=(
            "Примеры:\n"
            "  python main.py stats\n"
            "  python main.py analyze\n"
            "  python main.py charts"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "command",
        choices=["stats", "analyze", "charts"],
        help="Команда для запуска"
    )

    args = parser.parse_args()
    df = load_orders()

    if args.command == "stats":
        print("Краткая статистика")
        print(get_basic_stats(df))
    elif args.command == "analyze":
        print(build_report(df))
    elif args.command == "charts":
        for path in create_charts(df):
            print(path)

if __name__ == "__main__":
    main()