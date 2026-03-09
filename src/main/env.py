from pathlib import Path

import environ  # type: ignore[import-untyped]

env = environ.Env()
env_fp = Path(__file__).parents[2] / "config" / ".env"
if env_fp.exists():
  environ.Env.read_env(env_fp)
