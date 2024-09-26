import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = 'Generador Contrasenas'
    titulo = ft.Text('Generador de Contrasena', size=32, weight=ft.FontWeight.BOLD)

    def generate_password(lenght, use_uppercase, use_numbers, use_symbols):
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        return ''.join(random.choice(characters) for _ in range(lenght))
    
    def update_password(e):
        password_field.value = generate_password(
            int(length_slider.value),
            uppercase_switch.value,
            numbers_switch.value,
            symbols_switch.value
        )
        page.update()

    def copy_to_clipboard(e):
        page.set_clipboard(password_field.value)
        snack_bar = ft.SnackBar(ft.Text('Contrasena copiada al portapapeles'))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    password_field = ft.TextField(
        read_only=True,
        width=400,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )

    length_slider = ft.Slider(min=8, max=32, divisions=24, label='{value}', value=12, on_change=update_password)

    generate_button = ft.ElevatedButton('Generar contrasena', on_click=update_password, icon=ft.icons.REFRESH)
    uppercase_switch = ft.Switch(label='Incluir mayusculas', value=True, on_change=update_password)
    numbers_switch = ft.Switch(label='Incluir numeros', value=True, on_change=update_password)
    symbols_switch = ft.Switch(label='Incluir simbolos', value=True, on_change=update_password)

    copy_button = ft.ElevatedButton(
        'Copiar al portapapeles',
        on_click=copy_to_clipboard,
        icon=ft.icons.COPY
    )

    page.add(titulo, 
             ft.Text('Longitud de la constrasena:'),
             length_slider,
             uppercase_switch,
             numbers_switch,
             symbols_switch,
             password_field, 
             ft.Row([generate_button, copy_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
             )

ft.app(target=main)