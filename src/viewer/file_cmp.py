import flet as ft 
from src.viewer.select_window import select_file_diag 

def file_cmp_page(page: ft.page):
    page.controls.pop()

    page, file_selector = select_file_diag(page)
    

    info_text = ft.Container(
        content = ft.Text("Select two files to start comparation!", size=16, weight = ft.FontWeight.BOLD),
        alignment = ft.alignment.center_left,
    )

    file_cmp_compnent = ft.Row([
        ft.Container(
            content = ft.ElevatedButton(
                text = "select file (left)",  
                icon="file_copy_rounded",
                width=180,
                on_click= lambda _: file_selector.pick_files(allow_multiple = False)
            ),
            alignment=ft.alignment.center_left,
        ),

        ft.Container(
            content = ft.ElevatedButton(
                text = "select file (right)", 
                icon="file_copy_rounded",
                on_click= lambda _: file_selector.pick_files(allow_multiple = False),
                width=180,
            ),
            alignment=ft.alignment.center_right,
        ),
    ])

    page.add(
        info_text,
        file_cmp_compnent,
    )

    page.update()