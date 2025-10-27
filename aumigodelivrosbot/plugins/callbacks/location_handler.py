import logging
from telethon import events
from typing import Any
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.plugins.helpers.buttons import go_back

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^location$'))
@with_stack_and_cleanup()
async def handle_location(event: Any):
    """
    Handles incoming callback queries with a pattern matching '^location$'.

    This function deletes the originating event, logs activity for debugging
    and information purposes, and sends a location message to the user with
    specific latitude and longitude coordinates.

    :param event: The callback query event being processed.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await event.client.send_location(
        sender_id,
        caption="🗺 **__Como chegar até nós__** 👆",
        lat=-20.32066277406623,
        long=-40.33500475909385,
        buttons=go_back()
    )

    await event.delete()