import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.buttons import adoption_menu
from aumigodelivrosbot.plugins.helpers.messages import CONTATO_ADOCAO

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='/adotar'))
@with_stack_and_cleanup()
async def handle_adoption(event: Any):
    """
    Handles the adoption request when the '/adotar' callback query pattern is triggered.
    The function fetches the sender's information, logs the relevant activity,
    and responds with adoption-related information and a menu.

    :param event: The CallbackQuery event is triggered when a user interacts with the defined command.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(CONTATO_ADOCAO, buttons=adoption_menu())

    await event.delete()