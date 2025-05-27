last_bot_messages = {}
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import requests

conversation_history = {}

MAIN_MENU = [
    ["🗓 Узнать расписание / Записаться"],
    ["💰 Цены абонементов", "🎒 Что взять с собой?"],
    ["🗺 Как дойти?", "🌸 Направления"],
    ["📞 Позвать менеджера","🌿 Рекомендации"]
]

def main_menu():
    return ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот студии Charova 💖", reply_markup=main_menu())



#ЗАПИСЬ



async def send_schedule_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    # Удалить сообщение с кнопкой
    await update.message.delete()

    # Удалить предыдущий ответ бота, если есть
    if chat_id in last_bot_messages:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_bot_messages[chat_id])
        except:
            pass
    btn = InlineKeyboardMarkup([[InlineKeyboardButton("✨ Перейти", url="https://n920992.yclients.com/")]])
    sent = await update.message.reply_text("Записаться и посмотреть расписание можно тут 💗", reply_markup=btn)
    last_bot_messages[chat_id] = sent.message_id




#ЦЕНА




async def send_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    # Удалить сообщение с кнопкой
    await update.message.delete()

    # Удалить предыдущий ответ бота, если есть
    if chat_id in last_bot_messages:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_bot_messages[chat_id])
        except:
            pass
    sent = await update.message.reply_text(
        "🐝 *АБОНЕМЕНТЫ НА БАЗОВЫЕ:*\n"
        "1 — 650₽\n"
        "4 — 2400₽\n"
        "8 — 4750₽\n"
        "12 — 6850₽\n"
        "Безлимит 1 мес — 8300₽\n"
        "Безлимит 3 мес — 13550₽\n\n"
        "💗 *ИНДИВИДУАЛЬНЫЕ:*\n"
        "1 — 1650₽\n"
        "2 — 2500₽\n"
        "8 — 7600₽\n"
        "12 — 10600₽",
        parse_mode="Markdown"
    )
    last_bot_messages[chat_id] = sent.message_id


#ВЗЯТЬ С СОБОЙ 


async def send_what_to_bring(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    # Удалить сообщение с кнопкой
    await update.message.delete()

    # Удалить предыдущий ответ бота, если есть
    if chat_id in last_bot_messages:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_bot_messages[chat_id])
        except:
            pass
    sent = await update.message.reply_text(
        "🎒 Что взять с собой:\n"
        "• Носочки 🧦\n"
        "• Удобная одежда 👚\n"
        "• Тапочки 🩴\n"
        "• Полотенце 🧼",
        parse_mode="Markdown"
    )
    last_bot_messages[chat_id] = sent.message_id



#ЛОКАЦИЯ



from telegram import InlineKeyboardMarkup, InlineKeyboardButton
async def send_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("📹 Смотреть видео", url="https://t.me/charovachat/366")]
    ])
    chat_id = update.message.chat_id

    # Удалить сообщение с кнопкой
    await update.message.delete()

    # Удалить предыдущий ответ бота, если есть
    if chat_id in last_bot_messages:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_bot_messages[chat_id])
        except:
            pass
    sent = await update.message.reply_text(
        "📍 *Адрес:* ул. Достоевского 9\n\nВот как пройти к студии 💖",
        reply_markup=btn,
        parse_mode="Markdown"
    )
    last_bot_messages[chat_id] = sent.message_id

#НАПРАВЛЕНИЯ


async def send_directions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    # Удалить сообщение с кнопкой
    await update.message.delete()

    # Удалить предыдущий ответ бота, если есть
    if chat_id in last_bot_messages:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_bot_messages[chat_id])
        except:
            pass

    # Отправить новое сообщение
    sent = await update.message.reply_text(
        "🌸 НАПРАВЛЕНИЯ:\n\n"
        "• ЗДОРОВАЯ СПИНА\n" \
        "Идеальное направление для тех, кто только начинает свой путь в спорте или проходит восстановление. Подходит при грыжах, протрузиях и других особенностях позвоночника. Укрепляем мышцы кора, снимаем зажимы и возвращаем лёгкость движениям — мягко, безопасно, с заботой о теле.\n\n"
        "• ПЛАСТИКА\n" \
        "Если хочешь двигаться красиво и чувствовать своё тело как музыкальный инструмент — тебе сюда. Мы развиваем гибкость, плавность, учим слушать музыку телом и эмоцией. Осваиваем мостик и другие элементы, где важна пластичность.\n\n"
        "• ШПАГАТЫ\n" \
        "Работаем над продольными и поперечными шпагатами с умом и техникой. Тело становится гибким и сильным одновременно: мы не только тянемся, но и укрепляем ноги, чтобы результат оставался с тобой надолго. Осваиваем  акробатические элементы, основанные на шпагатах.\n\n"
        "• СИЛОВАЯ ТРЕНИРОВКА\n" \
        "Функциональное кардио и умеренная силовая нагрузка (до 2,5 кг) — для тех, кто хочет сжечь лишнее и почувствовать мышцы в действии. Тело становится подтянутым, рельефным, уходит дряблость, появляется энергия. Это путь к спортивной, сильной версии себя.",
         parse_mode="Markdown"
    )
    last_bot_messages[chat_id] = sent.message_id


#CALLLLL



async def call_manager(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Менеджер скоро свяжется 💕")
    await context.bot.send_message(
        chat_id="@charovaru",
        text=f"📞 Менеджер вызван пользователем @{update.message.from_user.username}",
        parse_mode="Markdown"
    )



#РЕКОМЕНДАЦИИ




async def send_recommendations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    # Удалить кнопку запроса
    await update.message.delete()

    # Удалить предыдущий ответ
    if chat_id in last_bot_messages:
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=last_bot_messages[chat_id])
        except:
            pass

    # Отправить новый ответ и сохранить его ID
    sent_message = await update.message.reply_text(
        "🌿 *Рекомендации после тренировки в студии CHAROVA:*\n\n"
        "1️⃣ Выпейте 200–300 мл воды, чтобы восполнить потерю жидкости.\n\n"
        "2️⃣ Лимфодренажные чаи — травяные смеси, такие как зеленый чай, имбирный чай, которые могут способствовать выведению лишней жидкости и быстрому восстановлению после тренировки.\n\n"
        "3️⃣ Сауна и баня — помогают выводить лишнюю воду из организма, расслаблять мышцы после тренировок, улучшать циркуляцию крови и кожу.\n\n"
        "4️⃣ Морская соль в ванне помогает улучшить циркуляцию крови, вывести токсины, снять усталость и усилить эффект восстановления кожи. Она полезна для расслабления мышц, улучшения обмена веществ и профилактики целлюлита.\n\n"
        "_Следуя этим рекомендациям, вы быстрее восстановитесь и улучшите результаты!_",
        parse_mode="Markdown"
    )
    last_bot_messages[chat_id] = sent_message.message_id