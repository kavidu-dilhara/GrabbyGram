from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='grabbygram',
    version='0.0.1',
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
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Python 3.12.0',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
'       Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Linux :: Ubuntu',
        'Operating System :: POSIX :: Linux :: Fedora',
        'Operating System :: POSIX :: Linux :: CentOS',
    ],
    keywords='telegram downloader media python scrapping bulk bulkdownload',
    project_urls={
        'Bug Reports': 'https://github.com/kavidu-dilhara/GrabbyGram/issues',
        'Source': 'https://github.com/kavidu-dilhara/GrabbyGram',
    },
)
