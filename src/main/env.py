from pathlib import Path

import environ  # type: ignore[import-untyped]

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env_fp = Path(__file__).parents[2] / ".env"
environ.Env.read_env(env_fp)
