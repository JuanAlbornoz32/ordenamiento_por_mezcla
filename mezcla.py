import flet as ft
import random

def main(page: ft.Page):
    
    def create_containers(number):
        container_list = []
        for _ in range(number):
            container_list.append(
                ft.Container(
                    content = ft.Text(value=random.randint(1, 100)),
                    alignment = ft.alignment.center,
                    width=50,
                    height=50, 
                    bgcolor=ft.colors.ORANGE,
                    border_radius=25
                )
            )
        return container_list

    row = ft.Row(controls=create_containers(10))
    page.add(row)
                    

ft.app(target=main)