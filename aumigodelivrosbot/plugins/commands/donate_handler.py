import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import DOAR_LIVROS
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/doar'))
@with_stack_and_cleanup()
async def handle_donate(event: Any):
    """
    Handle the '/doar' command received as a new message event within a Telegram client. Once triggered,
    this asynchronous function processes the user input, retrieves sender information, logs the event,
    and sends a predefined response with interactive buttons. The response is then cleaned up to
    ensure no residual messages remain.

    The function incorporates decorator functionalities for managing Telegram events
    and performs stack cleanup for efficient resource handling post-execution.

    :param event: An instance representing the new message event received via the Telegram API.
                  Contains information about the message, its sender, and related client context.
                  Expected to be of type ``Any``.
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(DOAR_LIVROS, buttons=go_back())

    await event.delete()
