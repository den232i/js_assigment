from envparse import Env


env = Env()

# Postgres
POSTGRES_SERVER = env.str("POSTGRES_SERVER", default="localhost")
POSTGRES_PORT = env.str("POSTGRES_PORT", default="5432")
POSTGRES_DB = env.str("POSTGRES_DB", default="postgres")
POSTGRES_USER = env.str("POSTGRES_USER", default="postgres")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default="postgres")

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
URL_PREFIX = "/api/v1"
