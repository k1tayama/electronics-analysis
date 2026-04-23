import pandas as pd
import numpy as np
from pathlib import Path 

if Path('students_extended.csv').is_file():
    ddf = pd.read_csv("students_extended.csv")
else:
    raise ValueError("ОШИБКА\nФайл students_extended.txt не находится в нужной директории")

class AdvancedStudentAnalytics:
    def __init__(self, df):
        self.df = df
        self.data_validation()
        print(f"\n{'.'*10} Валидация данных прошла успешно! {'.'*10}")
        self._prepare_data()
    def data_validation(self):
        required_columns = {
        'name',
        'math',
        'physics',
        'cs',
        'attendance',
        'project_score',
        'scholarship',
        'city'
    }
        miss = required_columns - set(self.df.columns)
        if miss: raise ValueError(f'Отсутствуют колонки: {', '.join(miss)}')
        numeric_cols = ['math', 'physics', 'cs', 'attendance', 'project_score']
        for col in numeric_cols:
            if not pd.api.types.is_numeric_dtype(self.df[col]):
                raise ValueError(f"Колонка '{col}' должна быть числовой")
        
        critical_cols = ['name', 'math', 'physics', 'cs']
        if self.df[critical_cols].isna().any().any():
            raise ValueError('Обнаружены пустые значения в критичных колонках')
        
        if self.df['scholarship'].isna().any():
            raise ValueError("Колонка 'scholarship' содержит NaN")

        return True
    def _prepare_data(self):
        self.df["project_score"] = self.df["project_score"].fillna(self.df["project_score"].median())
        self.df["average_grade"] = ((self.df["math"] + self.df["physics"] + self.df['cs'])/3).round(3)
        self.df['performance_level'] = np.select(
            [
                self.df['project_score'] >= 85,
                self.df['project_score'] >= 70
            ],
            ['high', 'medium'],default='low'
        )
        self.df['risk_level'] = np.select( 
            [
                (self.df['attendance'] < 60) | (self.df['average_grade'] <65),
                self.df['attendance'] < 75
            ],
            ['high risk', 'medium risk'], default='low risk'
        )
    def top_students(self, n):
        top = self.df.sort_values(by='average_grade', ascending=False).head(n)
        return '\n'.join(top['name'])
    def group_stats(self):
        return f"""Средний балл: {self.df['average_grade'].mean().round(3)}
Средняя посещаемость: {self.df['attendance'].mean().round(3)}\nКоличество студентов: {self.df.shape[0]}"""
    def at_risk_students(self):
        return self.df[self.df['risk_level'] == 'high risk']['name']
    def scholarship_analysis(self):
        with_scr = self.df[self.df['scholarship'] == True]
        without_scr = self.df[self.df['scholarship'] == False]
        return f"""\n{'='*20} Студенты со стипендией {'='*20}\n {with_scr[['name', 'average_grade', 'attendance']]}\n
{'='*20} Студенты без стипендии {'='*20}\n {without_scr[['name', 'average_grade', 'attendance']]}"""
    def city_performance(self):
        avg_city = self.df.groupby('city')['average_grade'].mean().round(3)
        best = avg_city.idxmax()
        worst = avg_city.idxmin()
        return f"""Лучший город: {best}\nХудший город: {worst}"""
    def hidden_top_students(self):
        return '\n'.join(self.df.loc[(self.df['average_grade']>85) & (self.df['scholarship']==True), 'name'])
    def lazy_geniuses(self):
        return f'{'\n'.join(self.df.loc[(self.df['average_grade']>85) & (self.df['attendance']<60), 'name'])}'
    def full_analysis(self):
        print(f"\n\n{'-'*50} ПОЛНЫЙ АНАЛИЗ ДАННЫХ {'-'*50}\n\n")
        return f"""
{'-'*20} Топ-3 студента {'-'*20}\n{self.top_students(3)}\n
{'-'*20} Статистика по группам {'-'*20}\n{self.group_stats()}\n
{'-'*20} Количество студентов с высоким риском {'-'*20}\n{len(self.at_risk_students())}\n
{'-'*20} Количество “скрытых отличников“ {'-'*20}\n{self.hidden_top_students()}\n
{'-'*20} Количество “ленивых гениев“ {'-'*20}\n{self.lazy_geniuses()}\n
{'-'*20} Лучший и худший город {'-'*20}\n{self.city_performance()}\n
{'-'*20} Анализ стипендий {'-'*20}\n{self.scholarship_analysis()}
"""
    def performance_distribution(self):
        return f"""\n{'/'*20} Проценты по категориям {r'\\'*10}
Категория 'high': {(self.df['performance_level'] == 'high').sum()/(len(self.df['performance_level']))*100}%
Категория 'meduim': {(self.df['performance_level'] == 'medium').sum()/(len(self.df['performance_level']))*100}%
Категория 'low': {(self.df['performance_level'] == 'low').sum()/(len(self.df['performance_level']))*100}%"""
    
if __name__ == '__main__':
    analytics = AdvancedStudentAnalytics(ddf)

    # print(analytics.top_students(3))
    # print(analytics.group_stats())
    # print(analytics.full_analysis())
    # print(analytics.performance_distribution()) #доп задание
    print(analytics.full_analysis())
