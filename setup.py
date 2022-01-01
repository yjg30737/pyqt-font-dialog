from setuptools import setup, find_packages

setup(
    name='pyqt_font_dialog',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Font dialog made with PyQt',
    url='https://github.com/yjg30737/pyqt-font-dialog.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)