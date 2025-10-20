import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import COMO_AJUDAR
from aumigodelivrosbot.plugins.helpers.buttons import donation_buttons

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^how_to_help$'))
@with_stack_and_cleanup()
async def handle_help(event: Any):
    """
    Handles the callback query with the specific pattern '^how_to_help$'.

    This asynchronous function manages the callback query event triggered when a user interacts
    with a particular button or pattern. It deletes the original event, logs relevant information,
    and sends a response to the user with predefined content and buttons. The function ensures that
    cleanup is executed after processing.

    :param event: An instance of CallbackQuery denoting the event triggered by a user action.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(COMO_AJUDAR, buttons=donation_buttons())

    await event.delete()
