import pandas as pd
import pytest
from main import AdvancedStudentAnalytics

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "name": ["A", "B", "C"],
        "math": [90, 70, 50],
        "physics": [80, 60, 40],
        "cs": [85, 75, 55],
        "attendance": [90, 70, 50],
        "project_score": [95, 80, 60],
        "scholarship": [True, False, True],
        "city": ["london", "paris", "berlin"]
    })

def test_missing_columns():
    df = pd.DataFrame({"name": ["A"]})

    with pytest.raises(ValueError):
        AdvancedStudentAnalytics(df)

def test_non_numeric():
    df = pd.DataFrame({
        "name": ["A"],
        "math": ["bad"],
        "physics": [80],
        "cs": [90],
        "attendance": [90],
        "project_score": [95],
        "scholarship": [True],
        "city": ["A"]
    })

    with pytest.raises(ValueError):
        AdvancedStudentAnalytics(df)

def test_nan_in_critical():
    df = pd.DataFrame({
        "name": [None],
        "math": [90],
        "physics": [80],
        "cs": [70],
        "attendance": [90],
        "project_score": [95],
        "scholarship": [True],
        "city": ["A"]
    })

    with pytest.raises(ValueError):
        AdvancedStudentAnalytics(df)

def test_average_grade(sample_df):
    obj = AdvancedStudentAnalytics(sample_df)
    assert "average_grade" in obj.df.columns
def test_average_grade_value(sample_df):
    obj = AdvancedStudentAnalytics(sample_df)
    assert obj.df.loc[0, "average_grade"] == round((90+80+85)/3, 3)
def test_top_students(sample_df):
    obj = AdvancedStudentAnalytics(sample_df)
    result = obj.top_students(1)

    assert isinstance(result, str)
    assert "A" in result  
def test_hidden_top_students(sample_df):
    obj = AdvancedStudentAnalytics(sample_df)
    result = obj.hidden_top_students()
    assert isinstance(result, str)
def test_city_performance(sample_df):
    obj = AdvancedStudentAnalytics(sample_df)
    result = obj.city_performance()
    assert "Лучший город" in result
    assert "Худший город" in result
def test_performance_distribution(sample_df):
    obj = AdvancedStudentAnalytics(sample_df)
    result = obj.performance_distribution()
    assert "high" in result
    assert "%" in result

