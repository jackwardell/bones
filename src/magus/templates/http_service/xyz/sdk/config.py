import enum
import os
import pathlib

import attr
import strictyaml

SERVICE_ROOT_DIR = pathlib.Path(__file__).parent.parent


class XYZEnvironment(enum.Enum):
    PRODUCTION = "PRODUCTION"
    STAGING = "STAGING"
    DEVELOPMENT = "DEVELOPMENT"


def load_yaml() -> strictyaml.YAML:
    return strictyaml.load((SERVICE_ROOT_DIR / "config.yaml").read_text())


def get_environment() -> XYZEnvironment:
    return XYZEnvironment(os.environ["SERVICE_ENVIRONMENT"])


@attr.define
class XYZConfig:
    data: strictyaml.YAML = attr.Factory(load_yaml)
    environment: XYZEnvironment = attr.Factory(get_environment)

    @property
    def bind_data(self) -> strictyaml.YAML:
        return self.data["environments"][self.environment.value]

    @property
    def host(self) -> str:
        return self.bind_data["host"].as_marked_up()

    @property
    def port(self) -> int:
        return self.bind_data["port"].as_marked_up()

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"
