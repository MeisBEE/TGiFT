import random
import string
import asyncio
from pyrogram import Client, compose, filters
from pyrogram import raw
from pyrogram.errors import FloodWait
import datetime

# pip install git+https://github.com/AFN4NX/pyrogram.git@dev --force-reinstall
# Original Pyrogram Repo Will Not Work.
# Make Sure You Install Pyrogram from Upper Repo and Ohter Packages if Not Installed


def timechk():
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%I:%M:%S %p")
    date_str = current_time.strftime("%d %B")
    timee = f"{time_str} - {date_str}"
    return timee


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(characters) for _ in range(length))
    return random_string


async def main():
    # Get Your API ID and HASH from > https://my.telegram.org
    # Your Account Might Ban. So Use Temp Account. I am Not Responsible for Anything.
    user = Client(
        "Biktar", api_id="24510012", api_hash="529f8133fe67483f9982ea699d7cb47b"
    )
    bot = Client(
        "Holaa11",
        api_id="24510012",
        api_hash="529f8133fe67483f9982ea699d7cb47b",
        bot_token="6620728385:AAFjNlyP2FMB90mkWwTU4YWKIBYXxpwz0UQ",
    )
    # Replace WIth Your Own API ID , Hash and Bot TOken
    clients = [user, bot]

    # ================================================================================
    @bot.on_message(
        filters.command("xstart", [".", "/"]) & filters.user(6752292635)
    )  # Change With Your Own UserID
    async def xstart(client, message):

        k = await message.reply("`Please wait!`")
        count = 0
        while True:
            try:
                giftcode = generate_random_string(27)
                count += 1
                link = f"https://t.me/giftcode/{giftcode}"

                result = await user.invoke(
                    raw.functions.payments.CheckGiftCode(slug=giftcode)
                )
                text = f"{link} {result}"
                await message.reply(text)
            except FloodWait as e:
                print(f"FloodWait Encountered, Sleeping for {e.value} Seconds")
                await asyncio.sleep(e.value)
            except Exception as e:

                print(e)
                text = f"""Checking Telegram GiftCard
Number : {count}
Code : `{giftcode}`
Error : `{e}`

Last Checked : {timechk()}
"""
                await k.edit(text)
                await asyncio.sleep(59)

    print("Ready to Check Telegram GiftCards ✅")
    await compose(clients)


asyncio.run(main())
