import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import VOLUNTARIADO
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/voluntario'))
@with_stack_and_cleanup()
async def handle_voluntary(event: Any):
    """
    Handles the '/voluntario' NewMessage event and processes user interactions.
    The function retrieves and logs sender details, responds with
    a predefined message and buttons, and deletes event messages
    to maintain a clean chat interface.

    :param event: The NewMessage event instance is triggered when the '/voluntario'
                  command is issued.
    :type event: Any

    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(VOLUNTARIADO, buttons=go_back())

    await event.delete()
