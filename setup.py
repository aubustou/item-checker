from setuptools import setup

setup(
    name="item-checker",
    version="0.1",
    description="Check items presence or absence with help of RFIDs",
    author="aubustou",
    author_email="survivalfr@yahoo.fr",
    install_requires=[
        "pycairo>=1.21.0",
        "PyGObject>=3.42.2",
        "python-mercuryapi @ git+https://github.com/gotthardp/python-mercuryapi.git@master",
    ],
    entry_points={
        "console_scripts": [
            "item-checker = item_checker.main:main",
        ],
    },
)
