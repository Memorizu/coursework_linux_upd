from src.main import main


def test_main():
    data = main()
    assert data is not None
    assert type(data) == str
