from sys import argv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

tasks = []

# define a command handler. Command handlers usually take two arguments:
# bot and update
def start(bot, update):
    update.message.reply_text("Welcome to AmITaskList222843_bot!")


# /showTasks
def show(bot, update):
    if len(tasks) <= 0:
        update.message.reply_text("Nothing to do, here!")
    else:
        update.message.reply_text(tasks)


# /newTask
def new(bot, update, args):

    toAdd = ""

    for el in args:
        toAdd = toAdd+" "+el

    if toAdd not in tasks:
        tasks.add(toAdd)
        update.message.reply_text(" The new task was successfully added to the list!")
    else:
        update.message.reply_text("Task is already present in the list")


# /remove
def remove(bot, update, args):

    to_remove = ""

    for el in args:
        to_remove = to_remove + " " + el

    if to_remove in tasks:
        tasks.remove(to_remove)
        update.message.reply_text("The task was successfully deleted!")
    else:
        update.message.reply_text("The task you specified is not in the list!")


# /removeAll
def removeAll(bot, update):
    # send the message back
    if len(tasks) <=0:
        update.message.reply_text("I did not find any task to delete!")

    else:
        tasks.clear()
        update.message.reply_text("Every task has been deleted")


# error
def error(bot, update):
    # simulate typing from the bot
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    update.message.reply_text("I am sorry, but I cannot do that")


def main():
    """
    The AmIBot will implement the ex3-lab2)
    """
    # create the EventHandler and pass it your bot's token
    updater = Updater("597694260:AAEDiSFhXrCpofa4B1pzwBEnquBMicx1g5g")

    # get the dispatcher to register handlers
    dp = updater.dispatcher

    # add the command handler for the "/start" command
    dp.add_handler(CommandHandler("start", start))

    # / showTasks
    dp.add_handler(CommandHandler("showTasks", show))

    # /newTask < task to add >
    dp.add_handler(CommandHandler("newTask", new, pass_args=True))

    # /removeTask < task to remove >
    dp.add_handler(CommandHandler("removeTask", remove, pass_args=True))

    # /removeAllTasks < substring to use  to remove all  the  tasks that contain it >
    dp.add_handler(CommandHandler("removeAllTasks", removeAll))

    # error
    dp.add_handler(MessageHandler(Filters.text, error))


    # start the bot
    updater.start_polling()

    # run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    filename = argv[1]
    file = open(filename, "r")

    tasks.extend(file.read().split("\n"))
    file.close()

    main()