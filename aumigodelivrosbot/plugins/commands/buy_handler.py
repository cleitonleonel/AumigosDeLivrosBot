import logging
from typing import Any
from telethon import events
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import COMPRAR_LIVROS
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/comprar'))
@with_stack_and_cleanup()
async def handle_buy(event: Any):
    """
    Handles the `/comprar` command to respond with book purchase information.

    :param event: The event object representing an incoming `/comprar` message.
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