from pathlib import Path

from tectonic import config
from tectonic.core import fs, process, ui

INSTALL_DIR = Path.home() / ".kimi-code"
BINARY = INSTALL_DIR / "bin" / "kimi"
LINK = config.DIR_LOCAL / "bin" / "kimi"


def install() -> None:
    if BINARY.exists():
        ui.info("kimi-code already installed")
        return

    ui.step("Installing kimi-code")
    url = config.configs.get("urls.kimi-code")
    process.run_shell(f"KIMI_NO_MODIFY_PATH=1 curl -fsSL {url} | sh")
    ui.ok("kimi-code installed")


def link() -> None:
    fs.symlink(BINARY, LINK)


def run() -> None:
    ui.section("kimi-code")
    install()
    link()
    ui.ok("kimi-code ready")
