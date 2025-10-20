import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import VOLUNTARIADO
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^voluntary$'))
@with_stack_and_cleanup()
async def handle_voluntary(event: Any):
    """
    Handles the callback triggered by the 'voluntary' pattern in the callback query.
    This function is decorated with `@client.on` to listen for the specified event
    pattern and reacts by sending the appropriate response message to the user.

    The handler deletes the triggering event after processing it, logs relevant
    information such as the user ID and client instance for debugging purposes,
    and sends a predefined message with a defined set of interactive buttons.

    :param event: The callback query event object.
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
