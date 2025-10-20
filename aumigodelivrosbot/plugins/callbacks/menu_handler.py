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


@client.on(events.CallbackQuery(pattern='^default_menu$'))
@with_stack_and_cleanup()
async def handle_menu(event: Any):
    """
    Handles callback queries with the 'default_menu' pattern by showing a main menu interface
    to the user and logging relevant information.

    :param event: Event instance associated with the callback query. It contains information
        about the interaction, including the sender and the context of the query.
    :return: An asyncio Task resulting from the response action containing the menu title
        and buttons displayed to the user.
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Menu Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    help_msg = await event.respond(
        "__**Em que posso te ajudar???**__",
        buttons=Button.clear()
    )

    # event.client.drivers[sender_id][MENU_KEY].clear()

    event.client.drivers[sender_id][DELETE_KEY].append(help_msg.id)

    menu_buttons = get_menu_buttons()
    menu_title = "📚 **Menu Principal**"
    return await event.respond(menu_title, buttons=menu_buttons)
