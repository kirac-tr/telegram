from setuptools import setup

setup(
    name='telegrambot',
    version='1.0',
    packages=['bot'],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'telegrambot = bot.main:main',
        ],
    },
)
