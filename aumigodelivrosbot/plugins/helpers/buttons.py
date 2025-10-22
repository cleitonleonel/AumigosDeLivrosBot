from smartbot.utils.buttons import (
    Button,
    build_inline_buttons
)
from telethon.tl.custom.message import Message


async def replace_button_text(
        message: 'Message',
        row: int,
        column: int,
        new_text: str
) -> list[list[Button]]:
    """
    Replaces the text of a specific inline button in a Telegram message.

    Args:
        message (Message): The Telethon Message object containing inline buttons.
        row (int): Row index of the button to be updated (0-based).
        column (int): Column index of the button to be updated (0-based).
        new_text (str): New text to display on the button.

    Raises:
        ValueError: If the message or its buttons are missing.
        IndexError: If the specified row/column is out of range.
    """

    if not message or not message.buttons:
        raise ValueError("Message or buttons not available.")

    buttons = message.buttons

    try:
        current_button = buttons[row][column]
    except IndexError:
        raise IndexError(f"Button not found at position [{row}][{column}].")

    new_button = Button.inline(new_text, current_button.data)

    buttons[row][column] = new_button

    return buttons



def go_back() -> list[list[Button]]:
    """
    Constructs a back navigation button within an inline keyboard.

    The function creates a single "Back" button labeled "🔙 Voltar"
    linked to callback data `back_menu`. The button is displayed
    in one column layout and returned as a list of lists.

    :return: A list of lists representing the inline keyboard with a back button.
    :rtype: list[list[Button]]
    """
    back_section = [
        ("🔙 Voltar", b"back_menu"),
    ]

    back_button = build_inline_buttons(
        back_section,
        cols=1
    )

    return back_button


def donation_buttons() -> list[list[Button]]:
    """
    Generates and returns a list of donation-related buttons for a user interface.

    This function creates inline buttons grouped in a specific layout, combining
    predefined Pix and bank transfer options, along with a 'go back' option. It
    returns the constructed button layout which can be used for a donation feature
    in an application.

    :return: A two-dimensional list where each nested list represents a row
        of buttons containing Button objects.
    :rtype: list[list[Button]]
    """

    pix_section = [
        ("💠 Pix", b"donate_pix")
    ]

    donate_buttons = (
        build_inline_buttons(pix_section, cols=2)
        + [[]]
        + go_back()
    )

    return donate_buttons


def get_login_buttons() -> list[list[Button]]:
    """
    Returns a list of inline buttons for the login process.

    The buttons are organized into sections for user input and utility actions.
    """
    login_section = [
        ("👤 Usuário", b"login_username"),
        ("🔑 Senha", b"login_password"),
    ]

    utility_section = [
        ("✅ Entrar", b"login_submit"),
        ("🔙 Voltar", b"back_menu"),
    ]

    login_buttons = (
            build_inline_buttons(login_section, cols=1)
            + [[]]
            + build_inline_buttons(utility_section, cols=2)
    )

    return login_buttons


def adoption_menu():
    """
    Generates the voluntary menu consisting of inline buttons for the options available
    to the user.

    :return: A list representing rows of inline buttons for user interaction.
    :rtype: list
    """
    url_form = "https://docs.google.com/forms/d/e/1FAIpQLSfBy_SEBPmBr7hlIvIvDKU8SrbYyLjeBo5YzkHLM1GBbpHXUw/viewform"
    register_buttons = (
            [[Button.url("Formulário de Inscrição", url_form)]]
            + go_back()
    )

    return register_buttons


def get_menu_buttons() -> list[list[Button]]:
    """
    Generates a structured menu layout with inline buttons categorized into multiple sections.
    These sections include options for donating books, learning more about volunteering, exploring
    the organization, staying notified with events and social media updates, registering for volunteering,
    and discovering ways to help.

    The buttons across the sections are dynamically arranged according to the specified column counts,
    providing an organized layout for user interaction.

    :return: A list of lists containing `Button` objects representing the menu structure.
    :rtype: list[list[Button]]
    """
    donate_section = [
        ("📚 Doar Livros", b"donate_books"),
    ]

    main_section = [
        ("🛒 Comprar Livros", b"buy_books"),
        ("🙋‍ Voluntariado", b"voluntary"),
    ]

    know_section = [
        ("📍 Pontos de Coleta", b"collect_points"),
        ("📖 Conhecer a ONG", b"know_organization"),
    ]

    notifier_section = [
        ("📅 Próximos Eventos", b"next_events"),
        ("🌐 Redes Sociais", b"social_media"),
    ]

    adoption_section = [
        ("🫶 Adote um Pet", b"adoption_register"),
        ("👥 Conhecer Equipe", b"know_team")
    ]

    help_section = [
        ("💝 Como Ajudar", b"how_to_help"),
    ]

    menu_buttons = (
            build_inline_buttons(donate_section, cols=1)
            + build_inline_buttons(main_section, cols=2)
            + build_inline_buttons(know_section, cols=2)
            + build_inline_buttons(notifier_section, cols=2)
            + build_inline_buttons(adoption_section, cols=2)
            + build_inline_buttons(help_section, cols=1)
    )

    return menu_buttons
