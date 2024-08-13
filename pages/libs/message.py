#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Libraries
from typing import NoReturn, Self, Dict

# 3rd-party Libraries
import flet as ft

class Message:
    """
    Custom message control
    """
    def __init__(self: Self,
                 message: str, 
                 time: str, 
                 role: str, 
                 seen: bool, 
                 page: ft.page) -> NoReturn:

        self.message: str = message
        self.time: str = time
        self.role: str = role
        self.seen: bool = seen
        self.page: ft.page = page

    def build(self: Self) -> ft.Row:
        """
        Main method to return custom control

        :params: Self
        :return: ft.Row
        """
        # Main row control
        main_row = ft.Row(
            # Set the alignment based on the role 
            alignment="end" if self.role == "self" else "start",
            controls=[
                ft.Container(
                    padding=10,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            "#00364f", "#0e141a"
                        ] if self.role == "partner" else [
                            "#2b5f86", "#306894"
                        ],
                    ),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=10,
                        color="#10000000",
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.SOLID,
                    ),
                    content=ft.Row(
                        alignment="space_between",
                        spacing=5,
                        wrap=True,
                        run_spacing=1,
                        width=self.page.width / 1.26 if len(self.message) > 40 else None,
                        controls=[
                            ft.Text(
                                value=self.message,
                            ),
                            status_column := ft.Column(
                                spacing=0,
                                alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.Text(
                                        value=self.time,
                                        color="#bbbbbb"
                                    )
                                ]
                            ),
                            ft.Icon(
                                name="done_all" if self.seen else "check",
                                size=16
                            )
                        ]
                    ),
                    border_radius=ft.border_radius.only(
                        7, 7, 0, 7
                    ) if self.role == "partner" else ft.border_radius.only(
                        7, 7, 7, 0
                    )
                )
            ]
        )

        # Return the message control
        return main_row