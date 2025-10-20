import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import HISTORIA_ONG
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^know_organization$'))
@with_stack_and_cleanup()
async def handle_organization(event: Any):
    """
    Handles the "know_organization" callback query event and responds with the organization's
    information along with a button to go back. Deletes the original event after handling
    it to ensure it does not persist.

    :param event: The CallbackQuery event instance is triggered by the client.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(HISTORIA_ONG, buttons=go_back())

    await event.delete()
