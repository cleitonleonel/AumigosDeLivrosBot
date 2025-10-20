import uuid
import logging
from typing import Any
from decimal import Decimal
from telethon import events
from telethon.tl.custom.message import Message
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import with_stack_and_cleanup
from aumigodelivrosbot.services.pix_service import create_qrcode_pix

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.CallbackQuery(pattern='^donate_pix$'))
@with_stack_and_cleanup()
async def handle_donate_pix(event: Any):
    """
    Handles the callback query when the user selects the "donate_books" option.
    This function listens for callback query events that match the specified
    pattern. It processes the event, logs related information, and sends a
    response to the user with specified buttons.

    :param event: The callback event is triggered by the user.
    :type event: Any
    :return: None
    """
    sender = await event.get_sender()
    sender_id = sender.id

    await event.delete()

    logging.info(f"[Donate Handler] by User ID: {sender_id}")
    logging.debug(f"Event Client Instance: {event.client}")

    await generate_pix_qr(
        event,
        "aumigodelivros@gmail.com",
        amount=Decimal('0.00'),
        logo_path="src/media/aumigo_de_livros.png"
    )

    await event.delete()


async def generate_pix_qr(
        event: Message,
        pix_key: str,
        amount: Decimal,
        logo_path: str | None = None,
        extension: str = '.png'
):
    """ Generates a Pix QR code and sends it to the user.

    :param pix_key: The Pix key to be used in the QR code.
    :param amount: The amount to be included in the QR code.
    :param logo_path: Optional path to a logo image to be included in the QR code.
    :param extension: The file extension of the logo image, if provided.
    :param event: The event that triggered this function.
    """

    sender = await event.get_sender()
    sender_id = sender.id
    logging.info(f"Generate Pix Triggered by User ID: {sender_id}")

    config_dict = {
        "receiver": "InstitutoAumigosdeLivros",
        "city": "Vitória",
        "key": pix_key,
        "identification": f"PYPIX{uuid.uuid4().hex[:4]}",
        "zipcode": "29010361",
        "description": "Doação Livre / QRCODE - PYPIX",
        "amount": amount,
        "logo": logo_path if logo_path else None,
        "filename": f"qrcode{extension}"
    }

    pix_string, pix_qrcode = create_qrcode_pix(config_dict)
    await event.respond("✅ QR Code gerado com sucesso!")

    await event.client.send_file(
        sender_id,
        file=pix_qrcode,
        caption=f'\n\n__{pix_string}__'
    )