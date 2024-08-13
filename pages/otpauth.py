#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# OTPAuth page

# Standard Libraries
from typing import List, Any

# 3rd-party Libraries
import flet as ft

# Local Libraries
from pages.libs.loginControls import DialButton, OTP, OTPButton

def otpauth_layout(page: ft.Page) -> List[Any]:
    """
    layout function for otpauth page

    :params: page : page layout
    :return: list of controls
    """

    # Return page controls
    return [
        ft.Text(
            value="", 
            height=30
        ),
        # App bar actions
        ft.Row(
            spacing=0,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                ft.IconButton(
                    icon="arrow_back",
                    icon_size=25,
                    icon_color="#ffffff",
                    on_click=lambda _:page.go("/login")
                ),
            ]
        ),
        # Container for main controls
        ft.Container(
            padding=40,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                expand=1,
                spacing=10,
                controls=[
                    # OTP Image
                    ft.Row(
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                src="https://ouch-cdn2.icons8.com/wGENGulplvs__Z0a-tPvj3z3cd_LfVp_Q3KnX3Y3bYQ/rs:fit:736:736/czM6Ly9pY29uczgu/b3VjaC1wcm9kLmFz/c2V0cy9zdmcvNjEz/LzRlOGIzNTk3LTll/ZTctNDJhNS05ZDY5/LThiMTViMTRjMjJi/Zi5zdmc.png",
                                height=120,
                                width=120
                            ),
                        ]
                    ),
                    ft.Text(
                        value="Enter code",
                        size=23,
                        weight="bold",
                        width=page.width,
                        text_align="center"
                    ),
                    ft.Container(
                        padding=0,
                        content=ft.Text(
                            value=f"We've send a SMS with an activation code to your phone +{page.database["phone_number"]}",
                            size=16,
                            width=page.width,
                            text_align="center",
                            color="#888e94"
                        )
                    ),
                    ft.Text(
                        value=""
                    ),
                    # OTP digit inputs
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            phone_input1 := OTP().build(),
                            phone_input2 := OTP().build(),
                            phone_input3 := OTP().build(),
                            phone_input4 := OTP().build(),
                            phone_input5 := OTP().build(),
                        ]
                    )
                ]
            )
        ),
        ft.Text(
            value="", 
            expand=True
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextButton(
                    text="Telegram will call you in 1:25"
                )
            ]
        ),
        ft.Text(
            value=""
        ),
        # Dial butons
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
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="1", 
                                text=None, 
                                page=page
                            ).build(),
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="2", 
                                text="ABC", 
                                page=page
                                
                            ).build(),
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="3", 
                                text="DEF",
                                page=page
                                
                            ).build(),
                        ]
                    ),
                    ft.Row(
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="4", 
                                text="GHI", 
                                page=page
                                
                            ).build(),
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="5", 
                                text="JKL", 
                                page=page
                            ).build(),
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="6", 
                                text="MNO", 
                                page=page
                            ).build(),
                        ]
                    ),
                    ft.Row(
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="7", 
                                text="PQRS", 
                                page=page
                            ).build(),
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="8", 
                                text="TUV", 
                                page=page
                            ).build(),
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="9", 
                                text="WXYZ", 
                                page=page
                            ).build(),
                        ]
                    ),
                    ft.Row(
                        spacing=4,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value="", 
                                width=page.width/3.3
                            ),
                            OTPButton(
                                phone_input1,
                                phone_input2,
                                phone_input3,
                                phone_input4,
                                phone_input5,
                                number="0", 
                                text="+", 
                                page=page
                            ).build(),
                            ft.Text(
                                value="",
                                width=page.width/3.3
                            )
                        ]
                    )
                ]
            )
        ),
        ft.Text(
            value=""
        )
    ]
