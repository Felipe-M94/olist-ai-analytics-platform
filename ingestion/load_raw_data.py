import os
import yaml
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from datetime import datetime

# =============================
# LOAD ENV VARIABLES
# =============================

load_dotenv()

# =============================
# CONFIG
# =============================

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_PATH, "data", "raw")
CONFIG_PATH = os.path.join(BASE_PATH, "ingestion", "config", "tables_config.yml")

SCHEMA = "bronze"

# =============================
# LOGGING
# =============================

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

# =============================
# DB CONNECTION
# =============================

def get_db_uri():
    required_vars = [
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_DB"
    ]

    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing environment variable: {var}")

    return (
        f"postgresql://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    )

# =============================
# LOAD CONFIG
# =============================

def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

# =============================
# LOAD DATA
# =============================

def load_table(engine, table_name, file_name):
    try:
        file_path = os.path.join(DATA_PATH, file_name)

        log(f"Loading file: {file_name} from {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        df = pd.read_csv(file_path, low_memory=False)

        log(f"Inserting into {SCHEMA}.{table_name} ({len(df)} rows)")

        df.to_sql(
            table_name,
            engine,
            schema=SCHEMA,
            if_exists="replace",
            index=False
        )

        log(f"Finished loading {table_name}")

    except Exception as e:
        log(f"Error loading {table_name}: {str(e)}")
        raise

# =============================
# MAIN
# =============================

def main():
    log("Starting ingestion process")

    try:
        engine = create_engine(get_db_uri())
        config = load_config()

        for table in config["tables"]:
            load_table(engine, table["name"], table["file"])

        log("Ingestion completed successfully")

    except Exception as e:
        log(f"Pipeline failed: {str(e)}")
        raise

# =============================
# ENTRYPOINT
# =============================

if __name__ == "__main__":
    main()