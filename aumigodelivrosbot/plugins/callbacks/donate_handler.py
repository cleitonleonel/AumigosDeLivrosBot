import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import DOAR_LIVROS
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^donate_books$'))
@with_stack_and_cleanup()
async def handle_donate(event: Any):
    """
    Handles the callback query when the user selects the "donate_books" option.
    This function listens for callback query events that match the specified
    pattern. It processes the event, logs related information, and sends a
    response to the user with specified buttons.

    :param event: The callback event is triggered by the user.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(DOAR_LIVROS, buttons=go_back())

    await event.delete()
