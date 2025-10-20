import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import REDES_SOCIAIS
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/contato'))
@with_stack_and_cleanup()
async def handle_contact(event: Any):
    """
    Handles the '/contato' command of a new message event. This function is invoked
    as a decorator callback when the specified command pattern matches an incoming
    message. It retrieves the sender information, deletes the incoming message, logs
    the action, responds with predefined social media links and buttons for further
    navigation, and then deletes the response message.

    :param event: The incoming NewMessage event that triggered this handler.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(REDES_SOCIAIS, buttons=go_back())

    await event.delete()
