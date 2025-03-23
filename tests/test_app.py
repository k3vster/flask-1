import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("/thug", 200),
    ("/", 200),
    ("BLARGH", 404)
])
def test_uri(client, test_input, expected):
    response = client.get(test_input)
    assert response.status_code == expected
