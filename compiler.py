import subprocess

def compile_ui(ui_files, py_files):
    for ui_file, py_file in zip(ui_files, py_files):
        command = f"python -m PyQt5.uic.pyuic -x {ui_file} -o {py_file}"
        subprocess.run(command, shell=True)

if __name__ == "__main__":

    ui_files = ["./UI/UI_mainwidget.ui", "./UI/UI_category.ui", "./UI/UI_list.ui",
                "./UI/UI_board_read.ui","./UI/UI_board_write.ui", "./UI/UI_server.ui",
                "./UI/UI_warning.ui"]

    py_files = ["./UI/UI_mainwidget.py", "./UI/UI_category.py", "./UI/UI_list.py",
                "./UI/UI_board_read.py", "./UI/UI_board_write.py", "./UI/UI_server.py",
                "./UI/UI_warning.py"]

    compile_ui(ui_files, py_files) # 여러 파일 컴파일
# import os
# import sys
#
# if __name__ == '__main__':
#     os.system(f"pyrcc5 ../src_img/my_qrc.qrc -o my_qrc_rc.py")
#
#     uis = ['main_widget_damagochi_ver2', '']
#     for ui in uis:
#         # os.system(f'python  -m PyQt5.uic.pyuic --from-imports -x {ui}.ui -o ui_class_{ui}.py')
#         os.system(f'python  -m PyQt5.uic.pyuic --import-from=code.front.ui -x {ui}.ui -o ui_class_{ui}.py')