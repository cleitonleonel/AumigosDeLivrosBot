from telethon.tl.types import BotCommand

ADMIN_COMMANDS = [
    BotCommand(
        command="restart",
        description='Limpar cache de usuários e reiniciar o bot.'
    ),
    BotCommand(
        command="notifications",
        description='Enviar mensagem ou notificação para todos os usuários.'
    )
]

DEFAULT_COMMANDS = [
    BotCommand(
        command="start",
        description='Iniciar ou reiniciar uma conversa com o bot.'
    ),
    BotCommand(
        command="doar",
        description='Doar livros.'
    ),
    BotCommand(
        command="comprar",
        description='Comprar livros.'
    ),
    BotCommand(
        command="voluntario",
        description='Ser voluntário.'
    ),
    BotCommand(
        command="eventos",
        description='Próximos eventos.'
    ),
    BotCommand(
        command="contato",
        description='Contato e localização.'
    ),
    BotCommand(
        command="adotar",
        description='Adoção de animais.'
    ),
    BotCommand(
        command="ajuda",
        description='Ver ajuda e FAQ.'
    )

]
