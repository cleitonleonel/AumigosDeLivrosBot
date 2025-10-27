import logging
from typing import Any
from telethon import events, Button
from smartbot.utils.handler import ClientHandler
from smartbot.utils.menu import (
    with_stack_and_cleanup,
    MENU_KEY,
    DELETE_KEY
)

logging.basicConfig(level=logging.INFO)

client = ClientHandler()


@client.on(events.NewMessage(pattern='/start'))
@with_stack_and_cleanup()
async def handle_start(event: Any):
    """
    Handles the `/start` command by sending a greeting message.

    :param event: The event is triggered by the `/start` command.
    """

    sender = await event.get_sender()
    sender_id = sender.id
    logging.info(f"Start Handler Triggered by User ID: {sender_id}")
    logging.info(f"Event Client Instance: {event.client}")
    event.client.drivers[sender_id][MENU_KEY].clear()

    welcome_message = (
        "🐶✨ **Bem-vindo ao Aumigos de Livros!** ✨🐾\n\n"
        "Oi, au-migo! 🐕 Sou o assistente virtual do **Instituto Aumigos de Livros**, "
        "um projeto que une o amor pelos **livros 📚** e pelos **animais 🐾**.\n\n"
        "Aqui você pode:\n"
        "🐾 Conhecer nossos projetos e campanhas solidárias\n"
        "📚 Apoiar o Instituto com doações e parcerias\n"
        "💛 Descobrir histórias inspiradoras de leitura e adoção\n\n"
        "Junte-se à nossa matilha de leitores e faça parte dessa causa! 🐕💫\n\n"
        "👉 Toque no botão abaixo para começar!"
    )

    main_button = Button.text("📚 Menu Principal", resize=True)
    main_img = "src/media/evento_2.png"
    welcome_msg = await event.respond(welcome_message, buttons=main_button, file=main_img)
    event.client.drivers[sender_id][DELETE_KEY].append(welcome_msg.id)
