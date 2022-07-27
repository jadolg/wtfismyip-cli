from setuptools import setup

setup(
    name="wtfismyip",
    description='Get your fucking IP address',
    author='Jorge Alberto Díaz Orozco (Akiel)',
    author_email='diazorozcoj@gmail.com',
    version="1.0.0",
    scripts=["wtfismyip", ],
    install_requires=["requests", "rich", ]
)
