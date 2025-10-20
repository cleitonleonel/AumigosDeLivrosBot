import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.buttons import adoption_menu
from aumigodelivrosbot.plugins.helpers.messages import CONTATO_ADOCAO

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^adoption_register$'))
@with_stack_and_cleanup()
async def handle_adoption(event: Any):
    """
    Handles the callback query for the adoption register.

    This asynchronous function is triggered when the client receives a
    callback query event matching the pattern '^adoption_register$'.
    It retrieves the sender of the event, logs their information,
    deletes the triggering event, and sends a response with the required
    message and menu buttons.

    :param event: Represents the incoming callback query event to be processed.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    adoption_img = "src/media/adotar_1.png"
    await event.respond(CONTATO_ADOCAO, buttons=adoption_menu(), file=adoption_img)

    await event.delete()