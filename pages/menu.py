#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Menu page

# Standard Libraries
import random
import json
from typing import List, Dict, Any

# 3rd-party Libraries
import flet as ft

# Local libraries
from pages.libs.pfp import ProfilePicture 
from pages.libs.chatDialog import ChatDialog

def menu_layout(page: ft.Page) -> List[Any]:
    """
    layout function for menu page

    :params: page : page layout
    :return: list of controls
    """

    # Menu cotrols
    menu_controls = [
        # Menu Drawer
        page.menu_drawer,

        # App bar
        ft.AppBar(
            center_title=False,
            bgcolor="#1a2631",
            title=ft.Row(
                spacing=25,
                controls=[
                    ft.Text(
                        value="Fletgram", 
                        size=25, 
                        weight="bold", 
                        color="#ffffff"
                    )
                ]
            ),
            actions=[
                ft.IconButton(
                    content=ft.Icon(
                        name="verified_user", 
                        size=25, 
                        color="#ffffff"
                    )
                ),
                ft.IconButton(
                    content=ft.Icon(
                        name="search", 
                        size=25, 
                        color="#ffffff"
                    )
                )
            ]
        ),

        # Story section
        story_bar := ft.Container(
            width=page.width,
            content=ft.Row(
                spacing=15,
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    # These 2 text boxes will be used for spacing between
                    # start and end of the row
                    ft.Text(
                        value=""
                    ),
                    ft.Text(
                        value=""
                    )
                ]
            )
        ),

        # Chat Dialogs
        chat_dialogs := ft.Tabs(
            width=page.width,
            height=page.height,
            selected_index=0,
            scrollable=False,
            animation_duration=300,
            label_color="#52b4ff",
            divider_color="#330e151b",
            indicator_color="#52b4ff",
            unselected_label_color="#888e94",
            overlay_color="#330e151b",
            tabs=[],
        ),

        # Story floating button
        ft.FloatingActionButton(
            on_click=lambda _: None, 
            bgcolor="#52b4ff",
            content=ft.Icon(
                name="photo_camera", 
                color="#ffffff", 
                size=25
            ), 
            shape=ft.RoundedRectangleBorder(
                radius=100
            )
        )
    ]

    # Add the menu drawer to page
    page.drawer = page.menu_drawer

    # Add chat folders to menu
    for folder in page.database["folders"]:
        chat_dialogs.tabs.append(
            ft.Tab(
                text=folder,
                content=ft.Container(
                    content=ft.ListView(
                        expand=True, 
                        spacing=0, 
                        padding=0, 
                        auto_scroll=False,
                        controls=[]
                    )
                )
            )
        )

    # Load chat dialogs from database
    with open("./data/chats.json", "r") as file:
        chats: List[Dict[str, Any]] = json.load(file)

    # Add chat dialogs to it's chat folder
    for chat_folder in chat_dialogs.tabs:
        for chat in chats:
            # Get chat details from chat messages
            try:
                with open(f"./data/messages/{chat["id"]}.json") as file:
                    temp_data: Dict[str, str] = json.load(file)[-1]
                    last_mesg: str = temp_data["message"]
                    last_role: str = temp_data["role"]
                    last_time: str = temp_data["time"]
            
            # Leave history empty
            except FileNotFoundError:
                last_mesg: str = "Chat history deleted"
                last_role: str = "empty"
                last_time: str = ""
                  
            if chat["folder"] == chat_folder.text:
                chat_folder.content.content.controls.append(
                    ChatDialog(
                        profile=chat["profile"],
                        name=chat["name"],
                        message=last_mesg,
                        time=last_time,
                        seen=True if last_role == "self" else True if last_role == "empty" else False,
                        count=0 if last_role == "empty" else chat["count"],
                        pinned=chat["pinned"],
                        muted=chat["muted"],
                        chat_id=chat["id"],
                        phone_number=chat["phone_number"],
                        username=chat["username"],
                        birth=chat["birth"],
                        status=chat["status"],
                        bio=chat["bio"],
                        has_story=chat["has_story"],
                        channel=chat["channel"],
                        story_seen=chat["story_seen"],
                        page=page
                    ).build()
                )
                # Add divider between each chat dialogs
                chat_folder.content.content.controls.append(
                    ft.Divider(
                        color="#990e141a",
                        height=0.7,
                        thickness=0.7
                    )
                )
                # Add chat to story bar if it has story
                if chat["has_story"]:
                    story_bar.content.controls.insert(
                        1,
                        ProfilePicture(
                            profile=chat["profile"],
                            has_story=chat["has_story"],
                            size=55,
                            seen=chat["story_seen"]
                        ).with_name(
                            name=chat["name"]
                        )
                    )

    # Return menu controls
    return menu_controls
