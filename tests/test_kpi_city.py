from src.kpi_city import city_kpi


def test_city_kpi_happy_path() -> None:
    result = city_kpi("Mumbai")

    assert result["customer_count"] == 3
    assert result["total_monthly_spend"] == 420.5
    assert result["churn_rate"] == 1 / 3


def test_city_kpi_rejects_injection_attempt() -> None:
    result = city_kpi("Mumbai' OR 1=1 --")

    assert result["customer_count"] == 0
    assert result["total_monthly_spend"] == 0
    assert result["churn_rate"] == 0