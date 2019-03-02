import bot, nltk


def punkt_install():
	nltk.download('punkt')


if __name__ == "__main__":
	punkt_install()
    bot.app.run()