#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard Libraries
import time
from typing import NoReturn, Self, Union

# 3rd-party Libraries
import flet as ft
from flet_core.event_handler import ControlEvent

class DialButton:
    """
    Dial button for login page
    """
    def __init__(self: Self,
                 number: str,
                 text: Union[None, str],
                 page: ft.Page,
                 phone_input: ft.TextField) -> NoReturn:

        self.number: str = number
        self.text: str = text or "   "
        self.page: ft.Page = page
        self.phone_input: ft.TextField = phone_input

    def build(self: Self) -> ft.TextButton:
        """
        Main method for custom control 

        :params: Self
        :return: Text Button
        """
        def insert_digit(phone_input: ft.TextField,
                         number: str) -> NoReturn:
            """
            Inner helper function to insert digit to input

            :params: 
                phone_input: Input field
                number     : digit
            :return: None
            """
            # Add digit to input and update control
            phone_input.value += str(number)
            phone_input.update()

        return ft.TextButton(
            # Number row (e.g. "2 ABC")
            height=50,
            width=self.page.width/3.3,
            on_click=lambda _: insert_digit(
                phone_input=self.phone_input, 
                number=self.number
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(
                    radius=7
                ),
                padding=0,
                bgcolor="#242e3c"
            ),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        value=""
                    ),
                    ft.Text(
                        value=self.number, 
                        size=25, 
                        color="#ffffff"
                    ),
                    ft.Text(
                        value=self.text, 
                        size=18, 
                        color="#888e94"
                    ),
                    ft.Text(
                        value=""
                    )
                ]
            )
        )

    @staticmethod
    def icon_only(icon_name: str,
                  page: ft.Page,
                  phone_input: ft.TextField) -> ft.TextButton:
        """
        Static method to return only button with Icon (backspace 
        icon in dial button)

        :params:
            icon_name   : Name of the icon
            page        : Page layout
            phone_input : Text field

        :return: Text Button

        """
        def delete_digit(phone_input: ft.TextField) -> NoReturn:
            """
            Inner helper function to delete digit from
            input field

            :params: phone_input : Input text field

            :return: None
            """
            # Delete digit and update control
            phone_input.value = phone_input.value[:-1]
            phone_input.update()

        # Return custom control
        return ft.TextButton(
            height=50,
            width=page.width/3.3,
            content=ft.Icon(
                name=icon_name, 
                color="#ffffff"
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(
                    radius=7
                ),
                padding=0,
                bgcolor="#242e3c"
            ),
            on_click=lambda _: delete_digit(
                phone_input=phone_input
            )
        )


class OTPButton:
    """
    Custom control for OTP dial buttons
    """
    def __init__(self: Self, 
                 *phone_inputs: ft.TextButton,
                 number: str,
                 text: Union[None, str], 
                 page: ft.Page) -> NoReturn:

        self.number: str = number
        self.text: str = text or "   "
        self.page: ft.Page = page
        self.phone_inputs: ft.TextButton = phone_inputs

    def build(self: Self) -> ft.TextButton:
        """
        Main method to return custom control

        :params: Self
        :return: Text Button
        """
        def insert_digit(e: ControlEvent) -> None:
            """
            Inner helper function to insert digit to button input

            :params: Control Event
            :return: None
            """
            # Add digit to input, if it's empty
            for idx, control in enumerate(self.phone_inputs, start=1):
                if (otp_input:=control.content.value) == " ":
                    control.content = ft.Text(
                        value=self.number,
                        size=20,
                        color="#ffffff"
                    )
                    control.style.side[""].color = "#489ddf"
                    control.update()

                    # If all inputs are filled, go to menu page
                    if idx == 5:
                        # Do a fake sleep
                        time.sleep(0.5)

                        # Change color of inputs to green with animation
                        for control in self.phone_inputs:
                            control.style.side[""].color = "#34b118"
                            control.update()
                            time.sleep(0.1)

                        # Sleep for 1 second and go to menu
                        time.sleep(1)
                        self.page.go("/menu")

                    # Exit the function
                    return None

        # Return the OTP Button
        return ft.TextButton(
            height=50,
            width=self.page.width/3.3,
            on_click=lambda e: insert_digit(e),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        value=""
                    ),
                    ft.Text(
                        value=self.number, 
                        size=25, 
                        color="#ffffff"
                    ),
                    ft.Text(
                        value=self.text, 
                        size=18, 
                        color="#888e94"
                    ),
                    ft.Text(
                        value=""
                    )
                ]
            ),
            style=ft.ButtonStyle(
                padding=0,
                bgcolor="#242e3c",
                shape=ft.RoundedRectangleBorder(
                    radius=7
                )
            )
        )


class OTP:
    """
    OTP input custom layout
    """
    def __init__(self: Self) -> NoReturn:
        pass

    def build(self: Self) -> ft.TextButton:
        """
        Main method to return custom controls

        :params: Self
        :return: Text Button
        """
        # Return the custom control
        return ft.TextButton(
            height=45,
            width=45,
            content=ft.Text(
                value=" ", 
                size=20, 
                color="#ffffff"
            ),
            style=ft.ButtonStyle(
                padding=0,
                bgcolor="#00000000",
                side=ft.BorderSide(
                    width=1,
                    color="#66888e94"
                ),
                shape=ft.RoundedRectangleBorder(
                    radius=7
                )
            )
        )