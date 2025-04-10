#(©)CodeXBotz




from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# List of playful responses
responses = [
    "Why don't we keep our clothes on and just dance?",
    "I'm all for fun, but let's keep it classy!",
    "How about we just enjoy some virtual snacks instead?",
    "Let's save the undressing for the beach!",
]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I’m your playful bot. Type something fun!')

def respond_to_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    
    # Check for specific trigger words
    if 'undress' in text:
        response = random.choice(responses)
        update.message.reply_text(response)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("7548885134:AAGeAqHvzDuflKMm-aS15luBwCAHGfef-xQ")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_to_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
