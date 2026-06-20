import flet as ft

def main(page: ft.Page):
    page.title = "My First Flet App"

    page.add(
        ft.Text("Hello Prisca! Welcome to Flet.")
    )

ft.app(target=main)