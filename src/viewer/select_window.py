import flet as ft
from flet import (
    FilePickerResultEvent,
    FilePickerUploadFile,
)


def select_file_diag(org_page):

    def pick_files_result(e: FilePickerResultEvent):
        upload_files()

    
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)

    def upload_files():
        uf = []
        if pick_files_dialog.result is not None and pick_files_dialog.result.files is not None:
            for f in pick_files_dialog.result.files:
                uf.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=org_page.get_upload_url(f.name, 600),
                    )
                )
            pick_files_dialog.upload(uf)

    org_page.overlay.append(pick_files_dialog)
    return org_page, pick_files_dialog



