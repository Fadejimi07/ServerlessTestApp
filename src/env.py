import pathlib
from functools import lru_cache
from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent.parent
print(f"Base directory: {BASE_DIR}")
ENV_PATH = BASE_DIR / ".env"
print(f"Environment file path: {ENV_PATH}")

env_file_exists = ENV_PATH.exists()


@lru_cache()
def get_config():
    if ENV_PATH.exists():
        return Config(RepositoryEnv(str(ENV_PATH)))
    from decouple import config

    return config


config = get_config()
