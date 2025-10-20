import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import COMPRAR_LIVROS
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^buy_books$'))
@with_stack_and_cleanup()
async def handle_buy(event: Any):
    """
    Handles the callback query event triggered with the pattern '^buy_books$'.

    This function is triggered when a user interacts with a specific callback
    button indicated by the pattern '^buy_books$'. It handles deleting the
    triggering message, logs relevant information for debugging and tracking
    purposes, and sends a response message with appropriate buttons. Finally,
    the triggering message is deleted again for cleanup.

    :param event: The callback query event contains information about the
        query, including the user who triggered it and the client instance.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(COMPRAR_LIVROS, buttons=go_back())

    await event.delete()
