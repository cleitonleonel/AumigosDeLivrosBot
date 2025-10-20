import logging
from telethon import events, Button
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import (
    with_stack_and_cleanup,
    MENU_KEY,
    DELETE_KEY
)
from aumigodelivrosbot.plugins.helpers.buttons import get_menu_buttons

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='^📚 Menu Principal$'))
@with_stack_and_cleanup()
async def handle_menu(event: Any):
    """
    """
    sender = await event.get_sender()
    sender_id = sender.id
    await event.delete()

    logging.info(f"Callback Triggered by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    help_msg = await event.respond(
        "__**Em que posso te ajudar???**__",
        buttons=Button.clear()
    )

    event.client.drivers[sender_id][MENU_KEY].clear()
    event.client.drivers[sender_id][DELETE_KEY].append(help_msg.id)

    menu_buttons = get_menu_buttons()
    menu_title = "📚 **Menu Principal**"
    await event.respond(menu_title, buttons=menu_buttons)
