#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Libraries
from typing import NoReturn, Dict

# 3rd-Party Libraries
import flet as ft

# Local Libraries
from pages.login import login_layout
from pages.otpauth import otpauth_layout
from pages.menu import menu_layout
from pages.chat import chat_layout
from pages.profile import profile_layout

def view_handler(page: ft.Page) -> Dict[str, ft.View]:
    """
    Function to return views map

    :params: page = Flet Page Layout
    :return: Views map
    """
    return {
        "/login": ft.View(
            padding=0,
            spacing=0,
            route="/login",
            controls=login_layout(page),
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            bgcolor="#1a2631"
        ),
        "/otpauth": ft.View(
            padding=0,
            spacing=0,
            route="/otpauth",
            controls=otpauth_layout(page),
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            bgcolor="#1a2631"
        ),
        "/menu": ft.View(
            padding=0,
            spacing=0,
            route="/menu",
            controls=menu_layout(page),
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            bgcolor="#1a2631"
        ),
        "/chat": ft.View(
            padding=0,
            spacing=0,
            route="/chat",
            controls=chat_layout(page),
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            bgcolor="#1a2631"
        ),
        "/profile": ft.View(
            padding=0,
            spacing=0,
            route="/profile",
            controls=profile_layout(page),
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            bgcolor="#1a2631"
        )
    }