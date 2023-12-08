from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='grabbygram',
    version='0.0.3',
    author='Kavidu Dilhara',
    author_email='contact@kavidudilhara.eu.org',
    description='A Python package for downloading media from Telegram',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kavidu-dilhara/GrabbyGram',
    packages=find_packages(),
    install_requires=[
        'telethon',
        'tqdm',
        'python-dotenv',
        'pyfiglet'
    ],
    entry_points={
        'console_scripts': [
            'grabbygram = grabbygram.grabbygram:main'
        ]
    },
classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords='Python Telegram  downloader  script  bot  API requests URL  media  chat  messages download  automation',
    project_urls={
        'Bug Reports': 'https://github.com/kavidu-dilhara/GrabbyGram/issues',
        'Source': 'https://github.com/kavidu-dilhara/GrabbyGram',
    },
)
