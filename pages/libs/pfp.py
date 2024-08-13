#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Libraries
import random
from typing import NoReturn, Self, Dict, Union, Optional, List

# 3rd-party Libraries
import flet as ft

class ProfilePicture:
    """
    Custom profile picture control
    """
    def __init__(self: Self,
                 profile: Union[None, str],
                 has_story: bool,
                 size: Optional[int] = 45,
                 name: Optional[str] = "U",
                 seen: Optional[bool] = True,
                 bgcolor: Optional[str] = "#17212b") -> NoReturn:

        self.profile: Union[None, str] = profile
        self.has_story: bool = has_story
        self.size: int = size
        self.name: str = name
        self.seen: bool = seen
        self.bgcolor: str = bgcolor

    def random_gradient(self: Self) -> List[str]:
        """
        helper method to return random gradient

        :params: Self
        :return: List of colors
        """
        pallete: List[List[str]] = [
            ["#0cb27e", "#0a9cca"] if self.seen else ["#55888e94"],
            # ...
        ]
        return random.choice(pallete)

    def build(self) -> ft.Container:
        """
        Main method to return profile picture control

        :params: Self
        :return: ft.Container
        """
        # Profile picture container
        return ft.Container(
            content=ft.Container(
                alignment=ft.alignment.Alignment(0, 0),
                # Profile picture image
                content=ft.Image(
                    src=self.profile,
                    border_radius=100
                ) if self.profile else ft.Text(
                    value=self.name[0], 
                    size=30, 
                    width=self.size,  
                    text_align="center",
                    color="#ffffff"
                ),
                border_radius=100,
                border=ft.border.all(
                    width=2, 
                    color=self.bgcolor
                ) if self.has_story else None,
            ),
            border_radius=100,

            # Story gradient color
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=self.random_gradient(),
                rotation=45,
            ),
            padding=2 if self.has_story else 0,
            width=self.size,
            height=self.size
        )

    def with_name(self: Self, name: str) -> ft.Column:
        """
        Method to return profile picture with name under it

        :params:
            self: Self
            name: Name

        :return: ft.Column
        """
        return ft.Column(
            spacing=1,
            controls=[
                ft.Container(
                    content=ft.Container(
                        alignment=ft.alignment.Alignment(0, 0),
                        content=ft.Image(
                            src=self.profile,
                            border_radius=100
                        ) if self.profile else ft.Text(
                            value=name[0], 
                            size=30, 
                            width=self.size,  
                            text_align="center"
                        ),
                        border_radius=100,
                        border=ft.border.all(
                            width=3, 
                            color="#17212b"
                        )
                    ),
                    border_radius=100,

                    # Story gradient color
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=self.random_gradient(),
                        rotation=45,
                    ) if self.has_story else None,
                    padding=1.5,
                    width=self.size,
                    height=self.size
                ),
                ft.Text(
                    value=name, 
                    width=self.size, 
                    text_align="center", 
                    max_lines=1, 
                    overflow=ft.TextOverflow.ELLIPSIS
                )
            ]
        )