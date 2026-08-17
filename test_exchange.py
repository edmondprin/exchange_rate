import pytest
from exchange_rate_v2 import get_amount, get_currency, get_exchange_rate, convert_currency

# monkeypatch & capsys are pytest fixtures

def test_convert_currency():
    money_amount = convert_currency(2, 1.45)
    assert money_amount == pytest.approx(2.90)

def test_get_amount(monkeypatch, capsys):
    responses = iter(["-2", "hello", "50000"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(responses))
    response = get_amount()
    captured = capsys.readouterr()

    assert response == 50000.00
    assert "Only positive numbers are allowed." in captured.out
    assert "Please enter a number." in captured.out

def test_get_currency(monkeypatch):
    responses = iter(["AUD", "EUR"])
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(responses)
    )
    source_currency, target_currency = get_currency()
    assert source_currency == "AUD"
    assert target_currency == "EUR"

def test_get_exchange_rate():
    new_rate = get_exchange_rate("EUR", "USD")
    assert new_rate > 1
    assert isinstance(new_rate, float)




