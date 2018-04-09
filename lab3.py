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
    if(len(tasks) <= 0):
        update.message.reply_text("Nothing to do, here!")
    else:
        update.message.reply_text(tasks)


# /newTask
def new(bot, update, args):

    toAdd=""

    for el in args:
        toAdd=toAdd+" "+el

    if toAdd not in tasks:
        tasks.append(toAdd)
        update.message.reply_text("Task correctly added")
    else:
        update.message.reply_text("Task is already present in the list")

# /remove
def remove(bot, update, args):
    toRemove = ""

    for el in args:
        toRemove = toAdd + " " + el

    if toRemove in tasks:
        tasks.remove(toRemove)
        update.message.reply_text("Task correctly removed")
    else:
        update.message.reply_text("Task not present in task list")

# /removeAll
def removeAll(bot, update):
    # send the message back
    tasks.clear()
    update.message.reply_text("Every task has been deleted")


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

    # / removeTask < task to remove >
    dp.add_handler(CommandHandler("removeTask", remove, pass_args=True))

    # / removeAllTasks < substring to use  to remove all  the  tasks that contain it >
    dp.add_handler(CommandHandler("removeAllTasks", removeAll))


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