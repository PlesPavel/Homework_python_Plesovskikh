import os

def exception(dir_name):
    try:
        os.mkdir(dir_name)
    except:
        pass

exception('my_project')
exception('my_project\\settings')
exception('my_project\\mainapp')
exception('my_project\\adminapp')
exception('my_project\\authapp')
