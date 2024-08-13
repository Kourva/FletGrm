#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Login page

# Standard Libraries
import time
import json
from typing import Any, List, Dict, NoReturn

# 3rd-party Libraries
import flet as ft
from flet_core.event_handler import ControlEvent

# Local Libraries
from pages.libs.loginControls import DialButton

def login_layout(page: ft.Page) -> List[Any]:
    """
    layout function for login page

    :params: page : page layout
    :return: list of controls
    """
    
    def open_otp_page(e: ControlEvent) -> NoReturn:
        """
        Helper function to open OTP page

        :params: Control event
        :return: None
        """
        # Change submit button's Icon to Loading ring
        # and update the control
        e.control.content = ft.ProgressRing(
            value=None, 
            color="#ffffff",
            height=25,
            width=25
        )
        e.control.update()

        # Register phone number in database
        page.database["phone_number"] = phone_input.value
        
        # Fake sleep for 1 second and go to next page
        time.sleep(1)
        page.go("/otpauth")

    def select_country(name: str, code: str, flag_icon: str) -> NoReturn:
        """
        Helper function to update country list based on
        selected country

        :params:
            name      : Country name
            code      : Country code
            flag_icon : URL of country flag
        
        :return: None
        """
        # Change the country name
        country_name.value = name
        # Change the phone number input and focus it
        phone_input.value = code
        phone_input.focus()

        # Change the flag input and it's size
        country_flag.value = flag_icon
        country_flag.size = 20

        # Update control and close bottom sheet
        country_flag.update()
        country_name.update()
        phone_input.update()
        page.close(country_bottom_sheet)

    def open_bottom_sheet() -> NoReturn:
        """
        Helper function to open country bottom sheet

        :params: None
        :return: None
        """

        # Open the bottom sheet
        page.open(country_bottom_sheet)

        # Add countries to bottom sheet
        if len(
            target := country_bottom_sheet.content.content.controls
        ) == 0:
            for country in countries:
                target.append(
                    ft.ListTile(
                        dense=True,
                        leading=ft.Text(
                            value=country["flag"], 
                            size=20
                        ),
                        title=ft.Text(
                            value=f"{country["name"]} ({country["code"]})"
                        ),
                        trailing=ft.Text(
                            value=country["dial_code"], 
                            size=15, 
                            color="#489ddf"
                        ),
                        on_click=lambda _, country=country: select_country(
                            name=country["name"], 
                            code=country["dial_code"][1:], 
                            flag_icon=country["flag"]
                        )
                    )
                )
            # Update the bottom sheet
            country_bottom_sheet.update()

    # Load County database
    with open("./data/countries.json", "r") as data:
        countries: List[Dict[str, str]] = json.load(data)

    # Initialize a bottom sheet for country selection
    country_bottom_sheet: ft.BottomSheet = ft.BottomSheet(
        enable_drag=True,
        show_drag_handle=True,
        content=ft.Container(
            padding=10,
            content=ft.ListView(
                height=page.height,
                width=page.width,
                controls=[]
            )
        ),
        on_dismiss=lambda e: page.close(e.control)
    )

    # Return the controls
    return [
        # Expanded divider
        ft.Text(
            value="", 
            expand=True
        ),

        # Main container for controls
        ft.Container(
            padding=40,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                expand=1,
                spacing=10,
                controls=[
                    ft.Text(
                        value="Your phone number",
                        size=23,
                        weight="bold",
                        width=page.width,
                        text_align="center"
                    ),
                    ft.Container(
                        padding=10,
                        content=ft.Text(
                            value=(
                                "Please confirm your country code"
                                " and enter your phone number."
                            ),
                            size=16,
                            width=page.width,
                            text_align="center",
                            color="#888e94"
                        )
                    ),
                    ft.Text(
                        value=""
                    ),

                    # Button to open country bottom sheet 
                    ft.TextButton(
                        height=50,
                        width=page.width,
                        style=ft.ButtonStyle(
                            side=ft.BorderSide(
                                width=1,
                                color="#66888e94"
                            ),
                            shape=ft.RoundedRectangleBorder(
                                radius=7
                            ),
                            padding=0,
                            bgcolor="#00000000"
                        ),
                        on_click=lambda _: open_bottom_sheet(),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                ft.Text(
                                    value=""
                                ),
                                country_flag := ft.Text(
                                    value=" ",
                                    size=0
                                ),
                                country_name := ft.Text(
                                    value="Country",
                                    size=18,
                                    color="#888e94"
                                ),
                                ft.Text(
                                    value="", 
                                    expand=True
                                ),
                                ft.IconButton(
                                    icon="arrow_forward_ios", 
                                    icon_size=18, 
                                    icon_color="#888e94", 
                                    on_click=lambda _: open_bottom_sheet()
                                ),
                                ft.Text(
                                    value=""
                                )
                            ]
                        )
                    ),
                    ft.Text(
                        value="", 
                        height=0
                    ),

                    # Phone number input
                    phone_input := ft.TextField(
                        value="",
                        autofocus=True,
                        border_radius=7,
                        border_color="#66888e94",
                        focused_border_color="#477cb3",
                        height=50,
                        width=page.width,
                        text_size=18,
                        read_only=True,
                        label="Phone Number",
                        label_style=ft.TextStyle(
                            color="#888e94",
                            size=18
                        ),
                        prefix=ft.Row(
                            width=18,
                            controls=[
                                ft.Text(
                                    value="+",
                                    size=18
                                )
                            ]
                        )
                    ),

                    # Sync checkbox
                    ft.Checkbox(
                        value=True,
                        label="Sync Contacts",
                        splash_radius=7,
                        label_style=ft.TextStyle(
                            color="#ffffff",
                            size=17
                        )
                    )
                ]
            )
        ),
        
        # Submit button
        ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.IconButton(
                    height=60,
                    width=60,
                    icon_size=25,
                    content=ft.Icon(
                        name="arrow_forward", 
                        color="#ffffff"
                    ),
                    style=ft.ButtonStyle(
                        padding=0,
                        bgcolor="#489ddf",
                        shape=ft.RoundedRectangleBorder(
                            radius=100
                        )
                    ),
                    on_click=lambda e: open_otp_page(e)
                ),
                ft.Text(
                    value=""
                )
            ]
        ),
        ft.Text(""),

        # Number keyboard  
        ft.Container(
            padding=0,
            content=ft.Column(
                width=page.width,
                spacing=4,
                controls=[
                    ft.Row(
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            DialButton(
                                number="1", 
                                text=None, 
                                page=page, 
                                phone_input=phone_input
                            ).build(),
                            DialButton(
                                number="2", 
                                text="ABC",
                                page=page, 
                                phone_input=phone_input
                            ).build(),
                            DialButton(
                                number="3", 
                                text="DEF",
                                page=page, 
                                phone_input=phone_input
                            ).build()
                        ]
                    ),
                    ft.Row(
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            DialButton(
                                number="4", 
                                text="GHI",
                                page=page,
                                phone_input=phone_input
                            ).build(),
                            DialButton(
                                number="5", 
                                text="JKL",
                                page=page,
                                phone_input=phone_input
                            ).build(),
                            DialButton(
                                number="6", 
                                text="MNO",
                                page=page,
                                phone_input=phone_input
                            ).build(),
                        ]
                    ),
                    ft.Row(
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            DialButton(
                                number="7", 
                                text="PQRS",
                                page=page,
                                phone_input=phone_input
                            ).build(),
                            DialButton(
                                number="8", 
                                text="TUV",
                                page=page,
                                phone_input=phone_input
                            ).build(),
                            DialButton(
                                number="9", 
                                text="WXYZ",
                                page=page,
                                phone_input=phone_input
                            ).build(),
                        ]
                    ),
                    ft.Row(
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("", width=page.width/3.3),
                            DialButton(
                                number="0", 
                                text="+",
                                page=page, 
                                phone_input=phone_input
                            ).build(),
                            DialButton.icon_only(
                                icon_name="backspace_outlined", 
                                page=page,
                                phone_input=phone_input
                            ),
                        ]
                    )
                ]
            )
        ),
        ft.Text("")
    ]
