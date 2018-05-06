import os
from configparser import ConfigParser

cwd = os.getcwd()


class Config:
    debug = True
    host = "localhost"
    port = 7723
    model_dir = os.path.join(cwd, "model")
    model_filename = "model.pkl"

    log_dir = os.path.join(cwd, "logs")
    log_level = "DEBUG"
    log_handler = "basic"

    BOOLEAN_STATES = {'1': True, 'yes': True, 'true': True, 'on': True,
                      '0': False, 'no': False, 'false': False, 'off': False}

    def __init__(self, filename=None):
        self._config = ConfigParser()
        if not filename:
            filename = os.getenv(
                "APP_CONFIG_FILENAME",
                os.path.join(cwd, "configs", "config.ini")
            )
        filename = os.path.realpath(filename)
        self._config.read(filename)

        is_debug = os.getenv("APP_DEBUG", None)
        if is_debug:
            self.debug = self.parse_boolean(is_debug)

        if self._config.has_option("General", "debug"):
            self.debug = self._config.getboolean("General", "debug")

        if self._config.has_option("General", "host"):
            self.host = self._config.get("General", "host")
        self.host = os.getenv("APP_HOST", self.host)

        if self._config.has_option("General", "port"):
            self.port = self._config.getint("General", "port")
        self.port = int(os.getenv("APP_PORT", self.port))

        if self._config.has_option("General", "model_dir"):
            self.model_dir = self._config.get("General", "model_dir")
        self.model_dir = os.path.realpath(os.getenv("APP_MODEL_DIR",
                                                    self.model_dir))

        if self._config.has_option("General", "model_filename"):
            self.model_filename = self._config.get("General", "model_filename")

        if self._config.has_option("General", "log_dir"):
            self.log_dir = self._config.get("General", "log_dir")
        self.log_dir = os.path.realpath(os.getenv("APP_LOG_DIR", self.log_dir))

        if self._config.has_option("General", "log_level"):
            self.log_level = self._config.get("General", "log_level")
        self.log_level = os.getenv("APP_LOG_LEVEL", self.log_level).upper()

        if self._config.has_option("General", "log_handler"):
            self.log_handler = self._config.get("General", "log_handler")
        self.log_handler = os.getenv("APP_LOG_HANDLER",
                                     self.log_handler).lower()

    def parse_boolean(self, s):
        s_lower = s.lower()
        if s_lower not in self.BOOLEAN_STATES:
            raise ValueError('Not a boolean: %s' % s)
        return self.BOOLEAN_STATES[s_lower]


config = Config()
