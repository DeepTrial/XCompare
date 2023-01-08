import flet as ft

from src.viewer.select_window import select_file_diag
from src.viewer.file_cmp import file_cmp_page 


def compare_app(page: ft.Page):

    page.title = 'XCompare Index Page'

    # page, file_selector = select_file_diag(page)
    

    # TODO: set this part at the center of page (top-down is broken, left-right is ok)
    welcome_compnent = ft.Column([
        ft.Container(
            content = ft.Text("Welcome to XCompare!", size=20, weight = ft.FontWeight.BOLD),
            alignment = ft.alignment.center,
        ),
        ft.Container(
            content = ft.Text("Please select a compare mode below:", size=16),
            alignment = ft.alignment.center,
        ),

        ft.Container(
            content = ft.ElevatedButton(
                text = "Compare Files",  
                icon="file_copy_rounded",
                width=180,
                on_click = lambda _: file_cmp_page(page)
                # on_click= lambda _: file_selector.pick_files(allow_multiple = False)
            ),
            alignment=ft.alignment.center,
        ),

        ft.Container(
            content = ft.ElevatedButton(
                text = "Compare Folder", 
                icon="folder_copy_rounded", 
                disabled=True,
                width=180,
            ),
            alignment=ft.alignment.center,
        ),
    ])


    page.add(
        welcome_compnent,
    )

    page.update()