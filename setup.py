from setuptools import setup

setup(
    name='brak-hooks',
    version='1',
    py_modules=['brak_hooks'],
    author='Bartek Brak',
    author_email='bartek.rychlicki@gmail.com',
    # 3.9.5 introduced checking VIRTUAL_ENV
    install_requires=['isort>=3.9.5']
)
