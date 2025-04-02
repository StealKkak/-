import whois
import random
from itertools import product
import asyncio
import discord_webhook

webhook = "https://discord.com/api/webhooks/1356815142616301681/h1GHvTRCGhHIidR48e5JTQStJaQG9IPXfxCqT2ZENMv210WnV-nYsOcEKjDNgSPfUTbx"

async def check_domain(domain):
    try:
        w = whois.query(domain)
        print(domain)
        return False if w.registrant else True
    except:
        return True
    
async def main():
    start = "aaa"
    end = "zzz"

    started = False
    for chars in product("abcdefghijklmnopqrstuvwxyz", repeat=3):
        domain = "".join(chars) + ".kr"
        if not started:
            if domain[:-3] == start:
                started = True
            else:
                continue

        if domain[:-3] > end:
            break

        if await check_domain(domain):
            wh = discord_webhook.DiscordWebhook(url=webhook, content=domain)
            wh.execute()

asyncio.run(main())