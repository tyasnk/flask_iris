import os
from py_dotenv import read_dotenv

try:
    read_dotenv(os.path.join(os.getcwd(), ".env"))
except FileNotFoundError:
    pass

name = "flask_iris"
bind = "{}:{}".format(
    os.getenv("APP_HOST", "localhost"),
    os.getenv("APP_PORT", 5000)
)

worker_class = "gthread"
threads = os.cpu_count() * 2 + 1
loglevel = os.getenv("APP_LOG_LEVEL", "INFO")

accesslog = "-"
access_log_format = (
    '{"time": "%(t)s", "status_line": "%(r)s", "status": %(s)s, '
    '"response_time_micros": %(D)s, "process_id": "%(p)s"}'
)
errorlog = "-"
