import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import PROXIMOS_EVENTOS
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^next_events$'))
@with_stack_and_cleanup()
async def handle_next_events(event: Any):
    """
    Handles the callback query with the pattern '^next_events$'.

    Deletes the triggering event, logs information about the user who triggered
    the event and responds with the next events accompanied by back navigation
    buttons.

    :param event: The callback query event triggering this handler.
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
