import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import REDES_SOCIAIS
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^social_media$'))
@with_stack_and_cleanup()
async def handle_social(event: Any):
    """
    Handles the callback query for the 'social_media' pattern and provides the
    response with buttons for further navigation. Deletes the event after processing
    and logs the handling details for debugging purposes.

    :param event: The callback query event resulting from the user interaction.
    :type event: Any
    :return: Does not return anything but performs actions such as responding
             with buttons and logging the event details.
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(REDES_SOCIAIS, buttons=go_back())

    await event.delete()
