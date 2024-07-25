from setuptools import setup, find_packages

setup(
    name="snake_game",
    version="0.1",
    description="A simple Snake game implemented using Pygame.",
    author="Ch. Varun Kumar",
    author_email="varuncvk13@gmail.com",
    url="https://github.com/varunchithiraala/Snake-Game.git",
    packages=find_packages(),
    install_requires=[
        'pygame',  # Pygame is required to run the game
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'snakegame=snakegame:main',  # Entry point to run the game
        ],
    },
)
