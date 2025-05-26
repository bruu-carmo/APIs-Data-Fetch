import pytest
from src.automation_pipeline import APIClient, DataProcessor, DataAnalyzer

def test_fetch_data():
    client = APIClient("https://jsonplaceholder.typicode.com/users")
    data = client.fetch_data()
    assert data is not None
    assert isinstance(data, list)

def test_process_data():
    processor = DataProcessor()
    sample_data = [{"id": 1, "name": "Test", "status": "active"}]
    processed = processor.process(sample_data)
    assert processed is not None
    assert processed[0]["id"] == 1

def test_analyze_data(capsys):
    analyzer = DataAnalyzer()
    sample_data = [{"status": "active"}, {"status": "inactive"}, {"status": "active"}]
    analyzer.analyze(sample_data)
    captured = capsys.readouterr()
    assert "active: 2" in captured.out
    assert "inactive: 1" in captured.out
