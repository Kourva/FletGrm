#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard Libraries
from typing import Self, Union, NoReturn, Dict

# 3rd-party Libraries
import flet as ft

# Local Libraries
from pages.libs.pfp import ProfilePicture

class ChatDialog:
    """
    Chat dialog custom control
    """
    def __init__(self: Self,
                 profile: Union[None, str],
                 name: str,
                 message: str,
                 time: str,
                 seen: bool,
                 count: int,
                 pinned: bool,
                 muted: bool,
                 chat_id: str,
                 phone_number: str,
                 username: str,
                 birth: str,
                 status: str,
                 bio: str,
                 has_story: bool,
                 channel: Union[None, Dict[str, str]],
                 story_seen: bool,
                 page: ft.Page) -> NoReturn:
        
        self.profile: Union[None, str] = profile
        self.name: str = name
        self.message: str = message
        self.time: str = time
        self.seen: bool = seen
        self.count: int = count
        self.pinned: bool = pinned
        self.muted: bool = muted
        self.chat_id: str = chat_id
        self.phone_number: str = phone_number
        self.username: str = username
        self.birth: str = birth
        self.status: str = status
        self.bio: str = bio
        self.has_story: bool = has_story 
        self.channel: Union[None, Dict[str, str]] = channel
        self.story_seen: bool = story_seen
        self.page: ft.Page = page

    def click_function(self: Self) -> NoReturn:
        """
        Helper method to register database information
        and go to chat page

        :params: Self
        :return: None
        """
        db: Dict[str, Any] = self.page.database["chat"]
        db["id"] = self.chat_id
        db["profile"] = self.profile
        db["name"] = self.name
        db["phone_number"] = self.phone_number
        db["username"] = self.username
        db["birth"] = self.birth
        db["status"] = self.status
        db["bio"] = self.bio
        db["has_story"] = self.has_story
        db["channel"] = self.channel
        db["story_seen"] = self.story_seen
        self.page.go("/chat")

    def build(self: Self) -> ft.ListTile:
        """
        Main method to return custom control

        :params: Self
        :return: ListTime control
        """
        return ft.ListTile(
            bgcolor="#1d2c38" if self.pinned else "#1a2631",
            # Profile picture
            leading=ProfilePicture(
                profile=self.profile,
                has_story=self.has_story,
                size=55,
                seen=self.story_seen,
                name=self.name
            ).build(),
            # Name, seen status and message time row
            title=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
                controls=[
                    ft.Text(
                        value=self.name,
                        size=19,
                    ),
                    ft.Icon(
                        name="volume_off" if self.muted else "",
                        size=14,
                        color="#888e94"
                    ),
                    ft.Text(
                        value="", 
                        expand=True
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        spacing=3,
                        controls=[
                            ft.Icon(
                                name="" if self.count > 0 else (
                                    "done_all" if self.seen else "check"
                                ), 
                                size=19, 
                                color="#52b4ff"
                            ),
                            ft.Text(
                                value=self.time,
                                size=15,
                                color="#888e94"
                            )
                        ]
                    )
                ]
            ),
            # Last message and count button
            subtitle=ft.Row(
                spacing=5,
                controls=[
                    ft.Text(
                        value=self.message,
                        color="#888e94",
                        width=self.page.width / 1.9,
                        no_wrap=True,
                        overflow=ft.TextOverflow.ELLIPSIS
                    ),
                    ft.Row(
                        width=50,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.Text(
                                value="", 
                                expand=True
                            ),
                            # Pin icon if dialog is pinned else message count
                            ft.Icon(
                                name="push_pin",
                                color="#888e94",
                                size=19
                            ) if self.pinned else ft.TextButton(
                                height=28,
                                width=23 + (5 * len(str(self.count))),
                                content=ft.Text(
                                    value=self.count, 
                                    color="#ffffff", 
                                    size=16
                                ),
                                style=ft.ButtonStyle(
                                    side=ft.BorderSide(
                                        width=0,
                                        color="#00000000"
                                    ),
                                    shape=ft.RoundedRectangleBorder(
                                        radius=100
                                    ),
                                    padding=0,
                                    bgcolor="#22ffffff" if self.muted else "#52b4ff"
                                ),
                            ) if self.count > 0 else ft.Text(
                                value=""
                            )
                        ]
                    )
                ]
            ),
            on_click=lambda _: self.click_function()
        )