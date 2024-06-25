from telegram.ext import Updater, MessageHandler, Filters

# Ваш токен, полученный от BotFather
TOKEN = '7088612669:AAE5euMjd1V9fj4jkN8yj3TrroHykWxWEn8'

def respond_to_viktorian(update, context):
    # Получаем текст сообщения
    message_text = update.message.text.lower()
    
    # Проверяем, содержит ли сообщение слово "Викториан"
    if 'викториан' in message_text:
        # Отправляем ответное сообщение
        update.message.reply_text('К вашим услугам!')

def main():
    # Создаем Updater и передаем ему токен вашего бота
    updater = Updater(TOKEN, use_context=True)
    
    # Получаем диспетчера для регистрации обработчиков
    dp = updater.dispatcher
    
    # Создаем обработчик сообщений, который будет реагировать на все текстовые сообщения
    text_handler = MessageHandler(Filters.text & (~Filters.command), respond_to_viktorian)
    
    # Регистрируем обработчик в диспетчере
    dp.add_handler(text_handler)
    
    # Запускаем бота
    updater.start_polling()
    
    # Останавливаем бота при завершении работы
    updater.idle()

if __name__ == '__main__':
    main()
