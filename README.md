# Crypto Airflow Pipeline

A production-grade data pipeline that automatically fetches and transforms cryptocurrency prices daily.

## Architecture

## What it does

- Fetches daily crypto prices (Bitcoin, Ethereum, Binancecoin) from CoinGecko API
- Loads data into PostgreSQL
- Runs dbt transformations automatically
- Scheduled to run daily via Apache Airflow

## Tech Stack

- Apache Airflow 2.9.1
- PostgreSQL
- dbt
- Docker
- Python

## DAG Structure

- `fetch_and_load_prices` → Fetches crypto prices and loads to PostgreSQL
- `run_dbt_models` → Runs dbt transformations (staging → intermediate → marts)

## Setup

1. Clone the repo
2. Run `docker compose up -d`
3. Open `http://localhost:8080`
4. Login with `airflow` / `123456789`
5. Trigger `crypto_pipeline` DAG
