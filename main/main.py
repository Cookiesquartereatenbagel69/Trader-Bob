from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1420902394337951861/Jpi8_V6ZpkZgnaa9yDegMaljq633bqsXiAtwHygTMMGiQjSNMjkUX4yzXtxZyJEg5XKs")

# Create an embed object
embed = DiscordEmbed(
    title="Trader Bob",
    description="This is an embedded message sent from a Python script.",
    color='03b2f8'
)

# Add the embed to the webhook and execute
webhook.add_embed(embed)
response = webhook.execute()
