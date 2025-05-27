from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
from config import TOKEN
import handlers

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", handlers.start))
app.add_handler(MessageHandler(filters.Regex("🗓 Узнать расписание / Записаться"), handlers.send_schedule_link))
app.add_handler(MessageHandler(filters.Regex("💰 Цены абонементов"), handlers.send_prices))
app.add_handler(MessageHandler(filters.Regex("🎒 Что взять с собой?"), handlers.send_what_to_bring))
app.add_handler(MessageHandler(filters.Regex("🗺 Как дойти?"), handlers.send_location))
app.add_handler(MessageHandler(filters.Regex("🌸 Направления"), handlers.send_directions))
app.add_handler(MessageHandler(filters.Regex("📞 Позвать менеджера"), handlers.call_manager))
app.add_handler(MessageHandler(filters.Regex("🌿 Рекомендации"), handlers.send_recommendations))


print("🚀 Бот запускается... ждём запросов")
app.run_polling()
