#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FletGrm : Telegram made with Flet
# Source  : https://github.com/kozyol/FletGrm

# Standard Libraries
from typing import NoReturn, Dict, Any
import json

# 3rd-party Libraries
import flet as ft

# Local Libraries
from views import view_handler
from pages.libs.menuDrawer import MenuDrawer 

def FletGrm(page: ft.Page) -> NoReturn:
    """
    Main app layout

    :params: ft.Page = Flet Page layout
    :return: None
    """
    # Page Configuration
    page.title = "FletGrm"
    page.padding = 0
    page.spacing = 0
    page.window.width=370
    page.window.height=650
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.theme.Theme(
        use_material3=True,
    )

    # Screen Manager
    def route_change(e: ft.RouteChangeEvent) -> NoReturn:
        """
        Function to handle routes between screens

        :params: e = Route Change Event
        :return: None
        """
        # Clear current view and append new view (screen content)
        page.views.clear()
        page.views.append(
            view_handler(page)[page.route]
        )
        page.update()

    def view_pop(e: ft.ViewPopEvent) -> NoReturn:
        """
        Function to pop last view in views

        :params: e = View Pop Event
        :return: None
        """
        # Pop the last view from views
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    # Initialize a database in page (for accessing data between
    # various pages in Flet )
    page.database: Dict[str, Any] = {}
    with open("./data/self.json", "r") as file:
        database: Dict[str, Any] = json.load(file)
        for key, val in database.items():
            page.database[key] = val

    # Initialize the menu drawer
    page.menu_drawer: MenuDrawer = MenuDrawer(
        page=page
    ).build()

    # Register handlers and default view
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/login")

# Run the app
if __name__ == "__main__":
    ft.app(target=FletGrm)
