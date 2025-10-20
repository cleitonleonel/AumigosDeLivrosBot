import logging
from typing import Any
from telethon import events
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.messages import COMO_AJUDAR
from aumigodelivrosbot.plugins.helpers.buttons import donation_buttons

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/ajuda'))
@with_stack_and_cleanup()
async def handle_help(event: Any):
    """
    Handles the /help command, providing users with information about how they can receive
    assistance and interact with the bot. Deletes the command message after processing
    and responds with a predefined help text and a set of donation-related buttons.

    This handler logs details about the user interacting with the command, including
    their unique User ID, and ensures messages are appropriately cleaned up.

    :param event: Incoming event containing message details and context (such as the sender
                  and client instance)
    :type event: Any
    :returns: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.respond(COMO_AJUDAR, buttons=donation_buttons())

    await event.delete()