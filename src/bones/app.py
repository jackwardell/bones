import os
import pathlib
import shutil
import typing

import attr

THIS_FILE = pathlib.Path(__file__)
TEMPLATES_DIR = THIS_FILE.parent / "templates"

APP_DIR_NAME = ".bones"
SVC_DIR_NAME = "services"
TEMPLATES_DIR_NAME = "templates"

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
        templates_dir = app_dir / TEMPLATES_DIR_NAME

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

        if templates_dir.exists():
            output.add(
                f"{TEMPLATES_DIR_NAME} dir already exists in the root "
                f"directory, therefore not creating"
            )

        else:
            # templates_dir.mkdir()
            output.add(f"{TEMPLATES_DIR_NAME} dir created")
            # shutil.copytree(TEMPLATES_DIR, templates_dir, fi)
            shutil.copytree(
                TEMPLATES_DIR,
                templates_dir,
                symlinks=False,
                ignore=None,
                ignore_dangling_symlinks=False,
                dirs_exist_ok=False,
            )

        return output
