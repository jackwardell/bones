import os
import pathlib
import typing

import attr

APP_DIR_NAME = ".magus"
SVC_DIR_NAME = "services"
CONFIG_YAML = "config.yaml"


@attr.define
class CliAppOutput:
    responses: typing.List[str] = attr.Factory(list)

    def add(self, response: str) -> None:
        self.responses.append(response)

    def __len__(self) -> int:
        return len(self.responses)

    def __getitem__(self, item: int) -> str:
        return self.responses[item]


@attr.define
class CliApp:
    def init(self) -> CliAppOutput:
        current_working_dir = pathlib.Path(os.getcwd())
        app_dir = current_working_dir / APP_DIR_NAME
        svc_dir = current_working_dir / SVC_DIR_NAME

        output = CliAppOutput()

        if app_dir.exists():
            output.add(
                f"{APP_DIR_NAME} dir already exists in the root directory, "
                f"therefore not creating"
            )

        else:
            app_dir.mkdir()
            output.add(f"{APP_DIR_NAME} dir created")

        if svc_dir.exists():
            output.add(
                f"{SVC_DIR_NAME} dir already exists in the root directory, "
                f"therefore not creating"
            )

        else:
            svc_dir.mkdir()
            output.add(f"{SVC_DIR_NAME} dir created")

        return output
