from magus.app import APP_DIR_NAME
from magus.app import CliApp
from magus.app import CliAppOutput
from magus.app import SVC_DIR_NAME


def test_cli_app_init_neither_dirs_exists(in_tmp_dir) -> None:
    app = CliApp()
    output = app.init()
    assert output == CliAppOutput(
        responses=[
            f"{APP_DIR_NAME} dir created",
            f"{SVC_DIR_NAME} dir created",
        ]
    )
    assert (in_tmp_dir / APP_DIR_NAME).exists()
    assert (in_tmp_dir / SVC_DIR_NAME).exists()


def test_cli_app_init_both_dirs_exist(in_tmp_dir) -> None:
    (in_tmp_dir / APP_DIR_NAME).mkdir()
    (in_tmp_dir / SVC_DIR_NAME).mkdir()

    app = CliApp()
    output = app.init()
    assert output == CliAppOutput(
        responses=[
            f"{APP_DIR_NAME} dir already exists in the root directory, "
            f"therefore not creating",
            f"{SVC_DIR_NAME} dir already exists in the root directory, "
            f"therefore not creating",
        ]
    )
    assert (in_tmp_dir / APP_DIR_NAME).exists()
    assert (in_tmp_dir / SVC_DIR_NAME).exists()


def test_cli_app_init_only_app_dir_exists(in_tmp_dir) -> None:
    (in_tmp_dir / APP_DIR_NAME).mkdir()

    app = CliApp()
    output = app.init()
    assert output == CliAppOutput(
        responses=[
            f"{APP_DIR_NAME} dir already exists in the root directory, "
            f"therefore not creating",
            f"{SVC_DIR_NAME} dir created",
        ]
    )
    assert (in_tmp_dir / APP_DIR_NAME).exists()
    assert (in_tmp_dir / SVC_DIR_NAME).exists()


def test_cli_app_init_only_svc_dir_exists(in_tmp_dir) -> None:
    (in_tmp_dir / SVC_DIR_NAME).mkdir()

    app = CliApp()
    output = app.init()
    assert output == CliAppOutput(
        responses=[
            f"{APP_DIR_NAME} dir created",
            f"{SVC_DIR_NAME} dir already exists in the root directory, "
            f"therefore not creating",
        ]
    )
    assert (in_tmp_dir / APP_DIR_NAME).exists()
    assert (in_tmp_dir / SVC_DIR_NAME).exists()
