import os
import shutil

import flet as ft
from src.viewer import (
    main
)




if __name__ == "__main__":

    upload_tmp_dir = './tmp'

    if os.path.exists(upload_tmp_dir):
        shutil.rmtree(upload_tmp_dir)

    if not os.path.exists(upload_tmp_dir):
        os.mkdir(upload_tmp_dir)
    

    ft.app(target=main.compare_app, upload_dir = upload_tmp_dir, assets_dir = './assets')