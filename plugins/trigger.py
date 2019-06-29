# coding utf-8

from slackbot.bot import respond_to

@respond_to('ON|On|on')
def reply_on(message):
    message.reply("switch ON")


@respond_to('(OFF|Off|off)')
def reply_off(message, arg):
    message.reply("switch OFF")

'''
@respond_to('(temp|temperture)')
def temp_check(message, arg):
    message.reply("checking temperature...")
'''
