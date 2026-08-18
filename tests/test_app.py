from app import search_students


def test_search_students():
    result = search_students("Nguyen")
    assert len(result) >= 1
    assert "Nguyen" in result[0]["name"]


