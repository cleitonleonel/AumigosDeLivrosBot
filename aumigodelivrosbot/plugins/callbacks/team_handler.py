import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import NOSSA_EQUIPE
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^know_team$'))
@with_stack_and_cleanup()
async def handle_team(event: Any):
    """
    Handles the 'know_team' callback query event for a client instance.
    This function is triggered whenever a callback query with the pattern
    '^know_team$' is received. It fetches the sender's information, logs
    debug details, deletes the original event message, and responds with
    team information.

    :param event: The callback query event being handled.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(NOSSA_EQUIPE, buttons=go_back())

    await event.delete()
