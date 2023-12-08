from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import InputPeerEmpty
from tqdm import tqdm
import os
from dotenv import load_dotenv
import pyfiglet

# Function to handle login
def login():
    if not os.path.isfile('.env'):
        api_id = input("Enter your API ID: ")
        api_hash = input("Enter your API Hash: ")
        with open('.env', 'w') as env_file:
            env_file.write(f"API_ID={api_id}\nAPI_HASH={api_hash}\n")
    else:
        with open('.env', 'r') as env_file:
            env_vars = env_file.read().splitlines()
        api_id = env_vars[0].split('=')[1]
        api_hash = env_vars[1].split('=')[1]

    with TelegramClient('client', api_id, api_hash) as client:
        client.send_message('me', 'Login Successfully')
        print(client.download_profile_photo('me'))

# Function to get chats
def get_chat():
    load_dotenv()
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')

    with TelegramClient('client', api_id, api_hash) as client:
        result = client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=500,
            hash=0,
        ))

        for chat in result.chats:
            print(f"Chat ID: {chat.id}\nTitle: {chat.title}")
            if hasattr(chat, 'username') and chat.username:
                print(f"Username: @{chat.username}")
            if hasattr(chat, 'participants_count'):
                print(f"Participants Count: {chat.participants_count}")
            print("=" * 30)

# Function to download group media
def download_group():
    load_dotenv()
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')

    with TelegramClient('client', api_id, api_hash) as client:
        result = client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=999999999,
            hash=0,
        ))

        title = input("Enter the group title: ")

        for chat in result.chats:
            if chat.title == title:
                download_media(chat, client, title)

# Function to download channel media
def download_channel():
    load_dotenv()
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')

    with TelegramClient('client', api_id, api_hash) as client:
        result = client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=99999999,
            hash=0,
        ))

        title = input("Enter the channel title: ")

        channel = client(GetFullChannelRequest(title))
        print(channel.full_chat)

        download_media(channel.full_chat, client, title)

# Function to download media for a group or channel
def download_media(group, cl, name):
    messages = cl.get_messages(group, limit=999999999)

    for message in tqdm(messages):
        message.download_media('./' + name + '/')

# Function to print ASCII art title with color
def print_colored_ascii_art(message, color_code):
    colored_ascii_art = f"{color_code}{pyfiglet.figlet_format(message)}\033[0m"
    print(colored_ascii_art)

# Main function
def main():
    # Blue color ANSI escape code: \033[1;34m
    blue_color_code = "\033[1;34m"
    print_colored_ascii_art("GrabbyGram", blue_color_code)
    print("\n")
    print("\t\033[101m\033[1;77m  >>  Script By kavidu dilhara << \033[0m")    
    print("\t\033[1;96m 😼__www.kavidudilhara.eu.org__ \033[1;77m \033[0m")
    print("\n")
    while True:
        print("\nOptions:")
        print("1. Login")
        print("2. Get Chat")
        print("3. Download Group")
        print("4. Download Channel")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            login()
        elif choice == '2':
            get_chat()
        elif choice == '3':
            download_group()
        elif choice == '4':
            download_channel()
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
