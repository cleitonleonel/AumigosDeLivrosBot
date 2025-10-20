import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import PROXIMOS_EVENTOS
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/eventos'))
@with_stack_and_cleanup()
async def handle_events(event: Any):
    """
    Handles the '/eventos' command in the chat and responds with upcoming events
    information along with navigation options.

    This coroutine listens for a specific command from a user, processes the sender's
    information, logs the event, sends a predefined response with buttons, and ensures
    cleanup by deleting the command message afterward.

    :param event: The NewMessage event is triggered by the '/eventos' command.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(PROXIMOS_EVENTOS, buttons=go_back())

    await event.delete()
