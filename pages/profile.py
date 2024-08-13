#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Profile page

# Standard Libraries
import random
import json
from typing import NoReturn, List, Dict, Any

# 3rd-party Libraries
import flet as ft

# Local Libraries
from pages.libs.pfp import ProfilePicture
from pages.libs.message import Message

def profile_layout(page: ft.Page) -> List[Any]:
    """
    layout function for menu page

    :params: page : page layout
    :return: list of controls
    """

    def random_scheme() -> Dict[str, str]:
        """
        Helper function to return random color palette

        :params: None
        :return: Random palette
        """
        # Open palettes database
        with open("./data/profile_palette.json", "r") as file:
            palettes: Dict[str, List[Dict[str, str]]] = json.load(file)

        # Return random palette
        return random.choice(
            palettes[random.choice(["normal", "premium"])]
        )

    # Initialize the palette and database
    palette: Dict[str, str] = random_scheme()
    db: Dict[str, Any] = page.database["chat"]

    # Profile menu controls
    profile_controls = [
        # App bar
        ft.AppBar(
            center_title=False,
            bgcolor=palette["app_bar"],
            leading=ft.IconButton(
                icon="arrow_back", 
                icon_size=25, 
                icon_color="#ffffff", 
                on_click=lambda _: page.go(page.database["last_page"])
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
                    items=[]
                )
            ]
        ),
        # Profile section
        ft.Stack(
            height=205 if db["channel"] else 115,
            controls=[
                ft.Container(
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=10,
                        color="#44000000",
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.SOLID,
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=palette["gradient"],
                    ),
                    height=85,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="", 
                                height=1
                            ),
                            # Profile picture
                            ft.Row(
                                spacing=20,
                                controls=[
                                    ft.Text(
                                        value=""
                                    ),
                                    ProfilePicture(
                                        profile=db["profile"],
                                        has_story=db["has_story"],
                                        size=55,
                                        bgcolor=palette["app_bar"]
                                    ).build(),
                                    ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Text(
                                                value=db["name"], 
                                                size=22, 
                                                color="#ffffff", 
                                                weight="bold"
                                            ),
                                            ft.Text(
                                                value=db["status"], 
                                                size=16, 
                                                color="#888e94"
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ),
                # Chat icon button
                ft.IconButton(
                    width=60,
                    height=60,
                    icon="chat_outlined", 
                    icon_color="#ffffff", 
                    icon_size=25,
                    right=25,
                    top=55,
                    style=ft.ButtonStyle(
                        bgcolor=palette["button"],
                        shadow_color="#000000"    
                    ),
                    on_click=lambda _:page.go("/chat")
                ),
                # Channel info row if user has channel else nothing
                ft.Row(
                    left=22,
                    top=100,
                    controls=[
                        ft.Text(
                            value="Channel", 
                            size=18, 
                            weight="bold",
                            color=palette["channel_label"]
                        ),
                        ft.ElevatedButton(
                            text=db["channel"]["subscribers"],
                            height=20,
                            bgcolor=palette["subscribers_bg"],
                            color=palette["subscribers_fg"],
                            style=ft.ButtonStyle(
                                padding=ft.Padding(10, 0, 10, 0),
                            )
                        ),
                    ]
                ) if page.database["chat"]["channel"] else ft.Text(
                    value="", 
                    height=0
                ),
                
                # Channel dialog if user has channel else nothing
                ft.ListTile(
                    left=0,
                    top=130,
                    on_click=lambda _:None,
                    width=page.width,
                    leading=ProfilePicture(
                        profile=None,
                        has_story=False,
                        size=50
                    ).build(),
                    title=ft.Row(
                        controls=[
                            ft.Text(
                                value=db["channel"]["name"]
                            ),
                            ft.Text(
                                value="", 
                                expand=True
                            ),
                            ft.Text(
                                value=db["channel"]["last_time"], 
                                color="#aaaaaa", 
                                size=14
                            )
                        ]
                    ),
                    subtitle=ft.Text(
                        value=db["channel"]["last_message"], 
                        max_lines=2, 
                        overflow=ft.TextOverflow.ELLIPSIS, 
                        color="#888888"
                    )
                ) if db["channel"] else ft.Text(
                    value="", 
                    height=0
                )
            ]
        ),
        # Divider if user has channel else None
        ft.Divider(
            thickness=12,
            height=12,
            color="#10171e"
        ) if db["channel"] else ft.Text(
            value="", 
            height=0
        ),

        # Account info container
        ft.Container(
            padding=ft.Padding(5, 0, 5, 0),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Text(
                        value=""
                    ),
                    ft.Row(
                        spacing=15,
                        controls=[
                            ft.Text(
                                value=""
                            ),
                            ft.Text(
                                value="Info", 
                                size=18, 
                                weight="bold", 
                                color=palette["info"]
                            ),
                        ]
                    ),
                    # User's Phone number information
                    ft.ListTile(
                        dense=True,
                        title=ft.Text(
                            value=f"+{db["phone_number"]}" if db["phone_number"] else "Hidden", 
                            size=18, 
                            color="#ffffff"
                        ),
                        subtitle=ft.Text(
                            value="Mobile", 
                            size=15, 
                            color="#999999"
                        )
                    ),
                    # User's bio information, otherwise None
                    ft.ListTile(
                        dense=True,
                        title=ft.Text(
                            value=db["bio"], 
                            size=18, 
                            color="#ffffff", 
                            max_lines=2, 
                            overflow=ft.TextOverflow.ELLIPSIS
                        ),
                        subtitle=ft.Text(
                            value="Bio", 
                            size=15,
                            color="#999999"
                        )
                    ) if db["bio"] else ft.Text(
                        value="", 
                        height=0
                    ),
                    # User's Username, otherwise None
                    ft.ListTile(
                        dense=True,
                        title=ft.Text(
                            value=f"@{db["username"]}", 
                            size=18, 
                            color="#ffffff", 
                            max_lines=1, 
                            overflow=ft.TextOverflow.ELLIPSIS
                        ),
                        subtitle=ft.Text(
                            value="Username", 
                            size=15, 
                            color="#999999"
                        ),
                        trailing=ft.IconButton(
                            icon="qr_code", 
                            icon_color=palette["qrcode"]
                        )
                    ) if db["username"] else ft.Text(
                        value="", 
                        height=0
                    ),
                    # User's birthday, otherwise None
                    ft.ListTile(
                        dense=True,
                        title=ft.Text(
                            value=db["birth"], 
                            size=18, 
                            color="#ffffff",
                        ),
                        subtitle=ft.Text(
                            value="Date of Birth", 
                            size=15, 
                            color="#999999"
                        )
                    ) if db["birth"] else ft.Text(
                        value="", 
                        height=0
                    ),
                    # Notification section
                    ft.ListTile(
                        dense=True,
                        title=ft.Text(
                            value="Notifications", 
                            size=18, 
                            color="#ffffff"
                        ),
                        subtitle=ft.Text(
                            value="On", 
                            size=15, 
                            color="#999999"
                        ),
                        trailing=ft.CupertinoSwitch(
                            label="",
                            active_color=palette["switch_active"],
                            thumb_color=palette["switch_thumb"],
                            track_color=palette["switch_track"],
                            value=True,
                        )
                    )
                ]
            )
        ),
        ft.Divider(
            thickness=12,
            height=12,
            color="#10171e"
        )
    ]

    # Return profile controls
    return profile_controls