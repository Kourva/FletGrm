#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Chat page

# Standard Libraries
import random
import json
from typing import Any, List, Dict, NoReturn

# 3rd-party Libraries
import flet as ft

# Local Libraries
from pages.libs.pfp import ProfilePicture
from pages.libs.message import Message

def chat_layout(page: ft.Page) -> List[Any]:
    """
    layout function for login page

    :params: page : page layout
    :return: list of controls
    """

    def open_profile() -> NoReturn:
        """
        Helper function to open profile section

        :params: None
        :return: None
        """
        # Register last page info and open profile
        page.database["last_page"] = "/chat"
        page.go("/profile")

    def change_input_actions(mode: str) -> NoReturn:
        """
        Helper function to change input actions when input
        control in on focus or blur

        :parmas: mode: "focus" or "blur"
        :return: None
        """
        # If mode focus, show only send button and update page
        if mode == "focus":
            attach_buton.width = 0
            mic_button.width = 0
            send_button.width = 40
            attach_buton.icon_color="#00000000"
            mic_button.icon_color = "#00000000"
            page.update()

        # If mode is blur, remove send button and update page
        else:
            # Keep send button if text field has value
            if not message_input.value:
                attach_buton.width = 40
                mic_button.width = 40
                send_button.width = 0
                attach_buton.icon_color="#888e94"
                mic_button.icon_color = "#888e94"
                page.update()

    def send_message() -> NoReturn:
        """
        Helper function to send message

        :params: None
        :return: None
        """
        # If text field in not empty
        if (msg:=message_input.value):
            # Insert message to first index of scroll view
            # because scroll view is reversed
            chat_history.controls.insert(
                0,
                Message(
                    message=msg.strip(),
                    time="00:00 AM",
                    role="self",
                    seen=False,
                    page=page
                ).build()
            )
            # Clear text input and scroll to bottom of scroll view
            message_input.value = ""
            chat_history.scroll_to(
                offset=0,
                duration=500, 
                curve=ft.AnimationCurve.EASE_IN_OUT_CUBIC
            )
            # Remove greeting message if it's on page
            try:
                # Find the greeting message and pop it from page
                target = chat_controls.index(welcome_message)
                chat_controls.pop(target)
                chat_history.expand = True
            except (NameError, ValueError):
                pass
        # Update the page
        page.update()

    chat_controls: List[Any] = [
        # App bar
        ft.AppBar(
            center_title=False,
            bgcolor="#243140",
            leading=ft.IconButton(
                icon="arrow_back", 
                icon_size=25, 
                icon_color="#ffffff", 
                on_click=lambda _: page.go("/menu")
            ),
            # Profile section
            title=ft.Container(
                on_click=lambda _: open_profile(),
                ink=True,
                ink_color="#00000000",
                border_radius=20,
                content=ft.Row(
                    spacing=10,
                    controls=[
                        ProfilePicture(
                            profile=page.database["chat"]["profile"],
                            has_story=page.database["chat"]["has_story"],
                            size=40
                        ).build(),
                        ft.Column(
                            spacing=0,
                            controls=[
                                ft.Text(
                                    value=page.database["chat"]["name"], 
                                    size=19, 
                                    color="#ffffff", 
                                    weight="bold"
                                ),
                                ft.Text(
                                    value=page.database["chat"]["status"], 
                                    size=16,
                                    color="#888e94"
                                )
                            ]
                        )
                    ]
                )
            ),
            actions=[
                ft.IconButton(
                    content=ft.Icon(
                        name="call", 
                        size=25, 
                        color="#ffffff"
                    )
                ),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            icon="volume_off",
                            text="Mute"
                        ),
                        ft.PopupMenuItem(
                            icon="search",
                            text="Search"
                        ),
                        ft.PopupMenuItem(
                            icon="video_call",
                            text="Video Call"
                        ),
                        ft.PopupMenuItem(
                            icon="contacts",
                            text="Add to contacts"
                        ),
                        ft.PopupMenuItem(
                            icon="wallpaper",
                            text="Change Wallpaper"
                        ),
                        ft.PopupMenuItem(
                            icon="clear_all",
                            text="Clear History"
                        ),
                        ft.PopupMenuItem(
                            icon="delete",
                            text="Delete chat"
                        )
                    ]
                )
            ]
        ),
        # Chat history
        chat_history := ft.ListView(
            expand=True,
            auto_scroll=False,
            padding=10,
            spacing=5,
            reverse=True,
            controls=[]
        ),

        # Bottom app bar
        bottom_app := ft.Container(
            bgcolor="#243140",
            content=ft.Row(
                spacing=3,
                controls=[
                    # Emoji icon
                    ft.IconButton(
                        icon="sentiment_satisfied", 
                        icon_color="#888e94",
                        icon_size=30
                    ),
                    # Message input
                    message_input := ft.CupertinoTextField(
                        bgcolor="#00000000",
                        expand=True,
                        multiline=True,
                        text_size=20,
                        max_lines=3,
                        placeholder_text="Messages",
                        placeholder_style=ft.TextStyle(
                            size=20,
                            color="#888e94"
                        ),
                        border=ft.border.all(
                            width=0,
                            color="#00000000"
                        ),
                        on_focus=lambda _: change_input_actions(
                            mode="focus"
                        ),
                        on_blur=lambda _: change_input_actions(
                            mode="blur"
                        )
                    ),
                    # Input actions
                    attach_buton := ft.IconButton(
                        icon="attach_file", 
                        icon_color="#888e94", 
                        icon_size=30, 
                        width=40
                    ),
                    mic_button := ft.IconButton(
                        icon="mic_outlined", 
                        icon_color="#888e94", 
                        icon_size=30,
                        width=40
                    ),
                    send_button := ft.IconButton(
                        icon="send", 
                        icon_color="#52b4ff", 
                        icon_size=25, 
                        width=0,
                        on_click=lambda _: send_message()
                    ),
                    ft.Text("", width=2)
                ]
            )
        )
    ]
    
    # Initialize the database
    db: Dict[str, Any] = page.database["chat"]

    # Load chat history from database
    try:
        with open(
            file=f"./data/messages/{db["id"]}.json", 
            mode="r"
        ) as file:
            messages: Dict[str, Any] = json.load(file)

    except FileNotFoundError:
        messages: Dict[str, Any] = {}

    # Add messages to chat history
    if messages:
        for message in messages:
            # Add time info if role is system
            if message["role"] == "system":
                chat_history.controls.insert(
                    0, 
                    ft.Text(
                        value="", 
                        height=5
                    )
                )
                chat_history.controls.insert(
                    0,
                    ft.Row(
                        height=34,
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.Alignment(0, 0),
                                content=ft.TextButton(
                                    content=ft.Text(
                                        value=message["time"], 
                                        size=15
                                    ),
                                    style=ft.ButtonStyle(
                                        bgcolor="#09ffffff"
                                    )
                                )
                            )
                        ]
                    )
                )
                chat_history.controls.insert(
                    0, 
                    ft.Text(
                        value="", 
                        height=5
                    )
                )
            # Otherwise if role is "self" or "partner", add message
            else:
                chat_history.controls.insert(
                    0,
                    Message(
                        message=message["message"],
                        time=message["time"],
                        role=message["role"],
                        seen=message["seen"],
                        page=page
                    ).build()
                )

    # Add greeting message if there is no history
    else:
        # Hide the scroll view and add greetings
        chat_history.expand = False
        chat_controls.insert(
            -1,
            welcome_message := ft.Container(
                alignment=ft.alignment.Alignment(0, 0),
                margin=10,
                padding=16,
                expand=True,
                border_radius=10,
                content=ft.Container(
                    alignment=ft.alignment.Alignment(0, 0),
                    bgcolor="#09ffffff",
                    width=200,
                    height=220,
                    padding=20,
                    border_radius=15,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            # Header text
                            ft.Text(
                                value="No messages here yet...", 
                                text_align="center",
                                size=16,
                                weight="BOLD"
                            ),
                            # Body text
                            ft.Text(
                                value="Send a message or tap the greeting below.",
                                text_align="center",
                                size=16,
                            ),
                            # Greeting image
                            ft.Image(
                                src="https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9QVcJY8gulRcQFXICOO_0srHWlNzNkoC4ez9f1dm1aPOdGQVtdrvx9DYlKGiauuAlzIBvsYg0-2S8Nug2A3j5QMyNIA5e-2e/330x192",
                                fit=ft.ImageFit.FIT_HEIGHT,
                                height=100,
                            )
                        ]
                    )
                )
            )
        )

    # Return the control
    return chat_controls
