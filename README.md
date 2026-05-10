# electronics-analysis

Проект для анализа заказов электроники на Python.

## Возможности

- Загрузка данных из CSV
- Краткая статистика
- Анализ заказов
- Построение графиков
- Запуск через терминал

## Установка

Клонировать репозиторий:

git clone https://github.com/k1tayama/electronics-analysis

Перейти в папку проекта:

cd project-name (ука)

Установить зависимости:

pip install -r requirements.txt

## Запуск

Краткая статистика:

python main.py stats

Полный анализ:

python main.py analyze

Построение графиков:

python main.py charts

## Структура проекта

main.py — точка входа

src/load_data.py — загрузка данных

src/analyze.py — анализ данных

src/graphics.py — построение графиков

tests/ — тесты проекта

## Используемые библиотеки

- pandas
- matplotlib
- pytest
- numpy
