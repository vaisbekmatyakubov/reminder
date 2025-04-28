import asyncio
from telegram import Bot
import schedule
import time
from datetime import datetime
import pytz

# Настройки бота
BOT_TOKEN = '7792591272:AAEEgPZHTuUlnSLEnYp7sDSPLxdVWCtIwcc'
CHAT_ID = '-1002346016617'

# Инициализация бота
bot = Bot(token=BOT_TOKEN)

# Функция отправки сообщения
async def send_message():
    try:
        await bot.send_message(chat_id=CHAT_ID, text='Прошу предоставить ежедневный отчет о проделанной работе. https://docs.google.com/spreadsheets/d/1sg9iaJn9u0eustTZARVDGbsQEBgbvy2b5ZofFS_ATVM/edit?usp=sharing')
        print(f"Сообщение успешно отправлено в {datetime.now(pytz.timezone('Asia/Tashkent'))}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

# Функция для вызова асинхронной функции в schedule
def run_async_task():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message())

# Планировщик задачи
def schedule_message():
    # Устанавливаем часовую зону Ташкента (UTC+5)
    tashkent_tz = pytz.timezone('Asia/Tashkent')

    # Планируем отправку каждый день в 16:57 по Ташкентскому времени
    schedule.every().day.at("17:10").do(run_async_task).tag('daily_message')

# Основной цикл
def main():
    schedule_message()

    while True:
        # Проверяем расписание
        schedule.run_pending()
        time.sleep(60)  # Проверяем каждую минуту

if __name__ == '__main__':
    main()