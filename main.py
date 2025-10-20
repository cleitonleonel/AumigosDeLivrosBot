import os
from smartbot.bot import Client
from smartbot.paths import SESSIONS_DIR
from telethon.network import ConnectionTcpFull
from smartbot.config import (
    BOT_TOKEN,
    APP_NAME,
    DEVICE_MODEL,
    SYSTEM_VERSION,
    APP_VERSION,
    ADMIN_IDS,
    API_ID,
    API_HASH,
)

SESSION_PATH: str = os.path.join(
    SESSIONS_DIR,
    APP_NAME
)

from constants import (
    ADMIN_COMMANDS,
    DEFAULT_COMMANDS
)


plugins: dict[str, str | list[str]] = dict(
    root="aumigodelivrosbot.plugins",
    include=[
        "commands.start_handler",
        "commands.menu_handler",
        "commands.help_handler",
        "commands.adoption_handler",
        "commands.voluntary_handler",
        "commands.donate_handler",
        "commands.buy_handler",
        "commands.events_handler",
        "commands.social_handler",

        "callbacks.back_menu_handler",
        "callbacks.menu_handler",
        "callbacks.help_handler",
        "callbacks.team_handler",
        "callbacks.ong_handler",
        "callbacks.points_handler",
        "callbacks.adoption_handler",
        "callbacks.donate_pix_handler",
        "callbacks.voluntary_handler",
        "callbacks.donate_handler",
        "callbacks.buy_handler",
        "callbacks.events_handler",
        "callbacks.social_handler",
    ],
    exclude=["message"]
)
commands: dict[str, list[str]] = dict(
    admin_commands=ADMIN_COMMANDS,
    default_commands=DEFAULT_COMMANDS
)

profile: dict[str, str] = dict(
    name=APP_NAME,
    logo="src/media/logo.png",
    lang="pt",
    description="Bot do Instituto Aumigos de Livros para doações e engajamento social.",
    about="Conectando leitores e amantes dos animais por meio da solidariedade."
)

client: Client = Client(
    bot_token=BOT_TOKEN,
    session=SESSION_PATH,
    api_id=API_ID,
    api_hash=API_HASH,
    connection=ConnectionTcpFull,
    device_model=DEVICE_MODEL,
    system_version=SYSTEM_VERSION,
    app_version=APP_VERSION,
    admin_ids=ADMIN_IDS,
    commands=commands,
    plugins=plugins,
    config=profile
)

if __name__ == "__main__":
    client.start_service()
