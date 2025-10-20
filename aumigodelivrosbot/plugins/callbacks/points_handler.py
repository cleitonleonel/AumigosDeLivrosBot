import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import PONTOS_DE_COLETA
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^collect_points$'))
@with_stack_and_cleanup()
async def handle_points(event: Any):
    """
    Handles the 'buy_books' callback query triggered by the user, interacting with the
    given callback pattern. Deletes the incoming event, logs the user's action, and
    responds with a predefined message and buttons for navigation.

    :param event: The callback query event object containing the event data.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(PONTOS_DE_COLETA, buttons=go_back())

    await event.delete()
