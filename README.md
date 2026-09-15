# Applied Analytics KPI Demo

This beginner-friendly project loads customer data from CSV into SQLite and calculates city-level KPIs.

## Run the project

```powershell
python -m pip install -r requirements.txt
python src/etl_load_sqlite.py
python src/kpi_city.py
python -m pytest
```

Run the commands from the project root while your `.venv` is activated.

## Files

- `data/raw/customers_raw.csv`: Small sample customer dataset.
- `data/db/analytics.db`: SQLite database created by the ETL script.
- `src/etl_load_sqlite.py`: Loads the CSV into the SQLite table.
- `src/kpi_city.py`: Calculates and prints KPIs for a selected city.
- `tests/test_kpi_city.py`: Tests the normal city query and SQL injection protection.
- `requirements.txt`: Lists the required Python packages.
- `.gitignore`: Keeps environments, caches, and the local database out of Git.