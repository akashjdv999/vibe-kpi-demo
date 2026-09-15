from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "db" / "analytics.db"


def city_kpi(city: str) -> dict[str, float | int]:
    query = """
        SELECT
            COUNT(*) AS customer_count,
            COALESCE(SUM(monthly_spend), 0) AS total_monthly_spend,
            COALESCE(AVG(churned), 0) AS churn_rate
        FROM customers_raw
        WHERE city = ?
    """

    with sqlite3.connect(DB_PATH) as connection:
        row = connection.execute(query, (city,)).fetchone()

    return {
        "city": city,
        "customer_count": row[0],
        "total_monthly_spend": row[1],
        "churn_rate": row[2],
    }


if __name__ == "__main__":
    print(city_kpi("Mumbai"))
    print(city_kpi("Mumbai' OR 1=1 --"))