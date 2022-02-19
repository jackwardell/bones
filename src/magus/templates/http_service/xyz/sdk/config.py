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
    def host(self) -> str:
        rv = self.data["environments"][self.environment.value][
            "host"
        ].as_marked_up()
        return rv

    @property
    def port(self) -> int:
        rv = self.data["environments"][self.environment.value][
            "port"
        ].as_marked_up()
        return rv
