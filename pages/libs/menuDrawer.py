#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Libraries
from typing import NoReturn, Self, Dict

# 3rd-party Libraries
import flet as ft

# Local Libraries
from pages.libs.pfp import ProfilePicture

class MenuDrawer:
    """
    Menu drawer class
    """
    def __init__(self: Self, page: ft.Page):
        self.page: ft.page = page

    def build(self):
        """
        Main method to return navigation drawer control

        :params: Self
        :reutnr: ft.NavigationDrawer
        """

        def handle_accounts() -> NoReturn:
            """
            Helper function to open and close account container

            :params: None
            :return: None
            """
            # Close container
            if accounts_show_button.icon == "keyboard_arrow_up":
                profile_container.controls.pop(
                    1
                )
                accounts_show_button.icon = "keyboard_arrow_down"
            # Open container
            else:
                profile_container.controls.insert(
                    1,
                    accounts_container
                )
                accounts_show_button.icon = "keyboard_arrow_up"
            
            # Update the container and button
            profile_container.update()
            accounts_show_button.update()

        def goto_my_profile() -> NoReturn:
            """
            Helper function to open user's profile

            :params: None
            :return: None
            """
            # Updte database
            db : Dict[str, Any] = self.page.database
            db["chat"]["id"] = db["id"]
            db["chat"]["profile"] = db["profile"]
            db["chat"]["name"] = db["name"]
            db["chat"]["phone_number"] = db["phone_number"]
            db["chat"]["username"] = db["username"]
            db["chat"]["birth"] = db["birth"]
            db["chat"]["status"] = db["status"]
            db["chat"]["bio"] = db["bio"]
            db["chat"]["has_story"] = db["has_story"]
            db["chat"]["channel"] = db["channel"]
            db["chat"]["story_seen"] = False

            # Register last page and open profile
            self.page.database["last_page"] = "/menu"
            self.page.go("/profile")

        # Initialize the database
        db: Dict[str, Any] = self.page.database

        # Navigation drawer control
        nav_control: ft.NavigationDrawer = ft.NavigationDrawer(
            bgcolor="#151e27",
            controls=[
                # Profile section
                profile_container := ft.ListView(
                    expand=1,
                    spacing=3, 
                    padding=0,
                    auto_scroll=False,
                    controls=[
                        profile_section := ft.Container(
                            margin=0,
                            padding=0,
                            height=150,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.bottom_center,
                                colors=["#001a2631", "#253646"],
                            ),
                            # Profile photo section
                            content=ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Text(
                                        value="", 
                                        height=12
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value=" "
                                            ),
                                            ProfilePicture(
                                                profile=db["profile"],
                                                has_story=db["has_story"],
                                                size=70
                                            ).build(),
                                            ft.Text(
                                                value="", 
                                                expand=True),
                                            ft.Column(
                                                alignment=ft.MainAxisAlignment.START,
                                                controls=[
                                                    theme_icon := ft.IconButton(
                                                        icon="sunny", 
                                                        icon_size=25, 
                                                        icon_color="#ffffff"
                                                    )
                                                ]
                                            ),
                                            ft.Text(
                                                value=""
                                            )
                                        ]
                                    ),
                                    ft.Text(
                                        value=""
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="  "
                                            ),
                                            ft.Column(
                                                spacing=3,
                                                controls=[
                                                    ft.Text(
                                                        value=db["name"], 
                                                        color="#ffffff"
                                                    ),
                                                    ft.Text(
                                                        value=f"+{db["phone_number"]}",
                                                        color="#888e94"
                                                    )
                                                ]
                                            ),
                                            ft.Text(
                                                value="", 
                                                expand=True
                                            ),
                                            accounts_show_button := ft.IconButton(
                                                icon="keyboard_arrow_up", 
                                                icon_size=25, 
                                                icon_color="#ffffff", 
                                                on_click=lambda _:handle_accounts()
                                            )       
                                        ]
                                    )
                                ]
                            )
                        ),
                        ft.ListTile(
                            on_click=lambda _: goto_my_profile(),
                            dense=True,
                            leading=ft.Icon(
                                name="account_circle_outlined", 
                                color="#888e94", 
                                size=27
                            ),
                            title=ft.Text(
                                value="My Profile", 
                                color="#ffffff", 
                                size=16, 
                                weight="bold"
                            )
                        ),
                        ft.ListTile(
                            on_click=lambda _: None,
                            dense=True,
                            leading=ft.Icon(
                                name="account_balance_wallet_outlined", 
                                color="#888e94", 
                                size=27
                            ),
                            title=ft.Text(
                                value="Wallet", 
                                color="#ffffff", 
                                size=16, 
                                weight="bold"
                            )
                        ),
                        # Divider
                        ft.Divider(
                            color="#ee0e141a",
                            height=0.7,
                            thickness=0.7
                        ),
                        ft.ListTile(
                            on_click=lambda _: None,
                            dense=True,
                            leading=ft.Icon(
                                name="group_outlined", 
                                color="#888e94", 
                                size=27
                            ),
                            title=ft.Text(
                                value="New Group", 
                                color="#ffffff", 
                                size=16, 
                                weight="bold"
                            )
                        ),
                        ft.ListTile(
                            on_click=lambda _: None,
                            dense=True,
                            leading=ft.Icon(
                                name="person_outlined", 
                                color="#888e94",
                                size=27
                            ),
                            title=ft.Text(
                                value="Contacts", 
                                color="#ffffff", 
                                size=16,
                                weight="bold"
                            )
                        ),
                        ft.ListTile(
                            on_click=lambda _: None,
                            dense=True,
                            leading=ft.Icon(
                                name="call_outlined",
                                color="#888e94",
                                size=27
                            ),
                            title=ft.Text(
                                value="Calls", 
                                color="#ffffff",
                                size=16,
                                weight="bold"
                            )
                        ),
                        ft.ListTile(
                            on_click=lambda _: None,
                            dense=True,
                            leading=ft.Icon(
                                name="settings_accessibility_outlined",
                                color="#888e94",
                                size=27
                            ),
                            title=ft.Text(
                                value="People Nearby", 
                                color="#ffffff", 
                                size=16, 
                                weight="bold"
                            )
                        ),
                        ft.ListTile(
                            on_click=lambda _: None,
                            dense=True,
                            leading=ft.Icon(
                                name="bookmark_outline",
                                color="#888e94",
                                size=27
                            ),
                            title=ft.Text(
                                value="Saved Messages",
                                color="#ffffff",
                                size=16,
                                weight="bold"
                            )
                        ),
                        ft.ListTile(
                            on_click=lambda _:None,
                            dense=True,
                            leading=ft.Icon(
                                name="settings_outlined", 
                                color="#888e94", 
                                size=27
                            ),
                            title=ft.Text(
                                value="Settings", 
                                color="#ffffff", 
                                size=16, 
                                weight="bold"
                            )
                        ),
                        ft.Divider(
                            color="#ee0e141a",
                            height=0.7,
                            thickness=0.7
                        ),
                        ft.ListTile(
                            on_click=lambda _: None,
                            dense=True,
                            leading=ft.Icon(
                                name="person_add_outlined",
                                color="#888e94",
                                size=27
                            ),
                            title=ft.Text(
                                value="Invite Friends",
                                color="#ffffff",
                                size=16,
                                weight="bold"
                            )
                        ),
                        ft.ListTile(
                            on_click=lambda _: None,
                            dense=True,
                            leading=ft.Icon(
                                name="help_outlined", 
                                color="#888e94", 
                                size=27
                            ),
                            title=ft.Text(
                                value="Telegram Features",
                                color="#ffffff",
                                size=16,
                                weight="bold"
                            )
                        )
                    ]
                )
            ]
        )

        # Account section include account and add button
        accounts_container = ft.Container(
            padding=0,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.ListTile(
                        on_click=lambda _: None,
                        dense=True,
                        leading=ft.Icon(
                            name="add", 
                            color="#888e94", 
                            size=27
                        ),
                        title=ft.Text(
                            value="Add Account", 
                            color="#ffffff", 
                            size=16, 
                            weight="bold"
                        )
                    ),
                    ft.Divider(
                        color="#ee0e141a",
                        height=0.7,
                        thickness=0.7
                    )
                ]
            )
        )

        # Add accounts to account section
        for account in db["logged_accounts"][::-1]:
            accounts_container.content.controls.insert(
                0,
                ft.ListTile(
                    dense=True,
                    on_click=lambda _: None,
                    leading=ProfilePicture(
                        profile=account["profile"],
                        has_story=False,
                        size=35
                    ).build(),
                    title=ft.Text(
                        value=account["name"],
                        color="#ffffff", 
                        size=16, 
                        weight="bold"
                    ),
                    trailing=ft.TextButton(
                        content=ft.Text(
                            value=account["unread"],
                            color="#ffffff",
                            size=16
                        ),
                        height=25,
                        width=20 + (5 * len(account["unread"])),
                        style=ft.ButtonStyle(
                            side=ft.BorderSide(
                                width=0,
                                color="#00000000"
                            ),
                            shape=ft.RoundedRectangleBorder(
                                radius=100
                            ),
                            padding=0,
                            bgcolor="#52b4ff"
                        )
                    ) if account["unread"] else None
                )
            )

        # Try to add accounts to container if container is empty
        try:
            profile_container.controls.index(
                accounts_container
            )
        except ValueError:
            profile_container.controls.insert(
                1,
                accounts_container
            )

        # Return navigation drawer
        return nav_control