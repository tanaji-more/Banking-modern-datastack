import os
import json
import requests
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

# -----------------------------
# Build connector JSON in memory
# -----------------------------
#connector_config = {
  #  "name": "postgres-connector",
   # "config": {
   #     "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    #    "database.hostname": os.getenv("POSTGRES_DOCKER_HOST"),
     #   "database.port": os.getenv("POSTGRES_PORT"),
      #  "database.user": os.getenv("POSTGRES_USER"),
    #    "database.password": os.getenv("POSTGRES_PASSWORD"),
     #   "database.dbname": os.getenv("POSTGRES_DB"),
  #      "topic.prefix": "banking_server",
   #     "table.include.list": "public.customers,public.accounts,public.transactions",
    #    "plugin.name": "pgoutput",
     #   "slot.name": "banking_slot",
      #  "publication.autocreate.mode": "all_tables",
       # "tombstones.on.delete": "false",
     #   "decimal.handling.mode": "double",
   # },
#}

connector_config = {
    "name": "postgres-connector",
    "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": "postgres",
        "database.port": "5432",
        "database.user": "postgres",
        "database.password": "Tanaji",
        "database.dbname": "banking",
        "topic.prefix": "banking_server",
        "plugin.name": "pgoutput",
        "slot.name": "banking_slot",
        "publication.autocreate.mode": "all_tables",
        "snapshot.mode": "initial",
        "tombstones.on.delete": "false",
        "decimal.handling.mode": "double"
    },
}


# -----------------------------
# Send request to Debezium Connect
# -----------------------------
url = "http://127.0.0.1:8083/connectors"

response = requests.post(url, json=connector_config)

if response.status_code == 201:
    print("✅ Connector created successfully!")
elif response.status_code == 409:
    print("⚠️ Connector already exists ")
else:
    print(f"❌ Failed to create connector ({response.status_code}): {response.text}")
