#coding:utf-8
from cx_Freeze import setup, Executable

setup(
    name = "Typing Increaser",
    version = "1.0",
    description = "Increase your typing speed and accuracy",
    executables = [Executable('typingtest.py')]
)