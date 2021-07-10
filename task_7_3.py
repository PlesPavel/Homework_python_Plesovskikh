import os
import shutil

def exception(dir_name):
    try:
        os.mkdir(dir_name)
    except:
        pass
def create():
    exception('my_project')
    exception('my_project\\settings')
    exception('my_project\\mainapp')
    exception('my_project\\authapp')
    exception('my_project\\mainapp\\templates')
    exception('my_project\\mainapp\\templates\\mainapp')
    exception('my_project\\authapp\\templates')
    exception('my_project\\authapp\\templates\\authapp')

    for dir in os.listdir('my_project'):
        open('my_project\\' + dir + '\\__init__.py', 'w')

    open('my_project\\settings\\dev.py', 'w').close()
    open('my_project\\settings\\prod.py', 'w').close()

    for dir in ['mainapp', 'authapp']:
        open('my_project\\' + dir + '\\models.py', 'w').close()
        open('my_project\\' + dir + '\\views.py', 'w').close()

    for dir in ['mainapp', 'authapp']:
        open('my_project\\' + dir + '\\templates\\' + dir + '\\base.html', 'w').close()
        open('my_project\\' + dir + '\\templates\\' + dir + '\\index.html', 'w').close()

shutil.copytree('my_project\\mainapp\\templates\\mainapp', 'my_project\\templates\\mainapp')
shutil.copytree('my_project\\authapp\\templates\\authapp', 'my_project\\templates\\authapp')
