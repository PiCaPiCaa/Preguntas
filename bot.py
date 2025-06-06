from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

TOKEN = "8169148924:AAHIq_fmqG_FiZ8_ckLa26v80dqXh9WWt2k"

# Lista de preguntas
preguntas = [
    "¿Alguna vez has tenido sexo con un desconocido?",
    "¿Qué te gusta más de tu pareja?",
    "¿Cuál es tu fantasía más loca?",
    "¿Qué es lo más romántico que has hecho?",
"¿Qué te gusta más de tu pareja? 😍",
"¿Qué fue lo primero que pensaste de mí cuando nos conocimos? 🤔",
"¿Cuál es tu mayor miedo en nuestra relación? 😟",
"¿Qué te hace sentir más cerca de mí aunque estemos lejos? 🧡",
"¿Cuál ha sido el momento más bonito que hemos vivido por videollamada? 📱",
"¿Te imaginabas que llegaríamos a estar juntos tanto tiempo sin vernos? 🗓️",
"¿Te gustaría vivir conmigo algún día? 🏡",
"¿Qué es lo que más te atrae de mí mentalmente? 🧠",
"¿Qué parte de nuestras conversaciones te encanta más? 💬",
"¿Qué canción te recuerda a mí? 🎶",
"¿Qué piensas justo antes de dormir cuando piensas en mí? 🌙",
"¿Qué harías el primer día que nos veamos? 🛬",
"¿Hay algo que no te hayas atrevido a decirme aún? 🙊",
"¿Te sientes cómodo/a contándome todo? 🤗",
"¿Qué fue lo que más te gustó de mí cuando empezamos a hablar? 💞",
"¿Qué sueño te gustaría cumplir conmigo? ✨",
"¿Qué palabra crees que me define mejor? 📝",
"¿Te has imaginado cómo será nuestro primer beso? 💋",
"¿Crees que somos compatibles a largo plazo? 🔐",
"¿Qué detalles míos te hacen sonreír sin darte cuenta? 😊",
"¿Hay algo que te gustaría que hiciéramos más juntos, aunque sea a distancia? 💻",
"¿Qué es lo más loco que harías por mí? 🤪",
"¿Te has sentido celoso/a alguna vez en nuestra relación? 😅",
"¿Qué tipo de fotos mías te gustan más? 📸",
"¿Has soñado conmigo alguna vez? 🌌",
"¿Qué lugar te gustaría visitar conmigo? ✈️",
"¿Cuál es tu mayor fantasía conmigo? 🔥",
"¿Te gustaría dormir abrazados cada noche si viviéramos juntos? 🛏️",
"¿Qué parte de tu cuerpo crees que me gustaría más? 👀",
"¿Qué parte de mi cuerpo imaginas como la más sensual? 💃",
"¿Qué prenda te gustaría que usara para ti? 👗",
"¿Te excita hablar conmigo por mensajes? 💌",
"¿Te gustaría que tuviéramos una videollamada íntima alguna vez? 🎥😏",
"¿Con qué frecuencia piensas en mí de forma sexual? 😳",
"¿Qué es lo más atrevido que me has querido decir y no te atreviste? 🙈",
"¿Cuál es tu posición sexual favorita (aunque no hayamos hecho nada aún)? 🛋️",
"¿Te gustaría que hiciéramos juegos eróticos a distancia? 🎲🔥",
"¿Prefieres sexo romántico o más salvaje? 🌹🐾",
"¿Has tenido fantasías sexuales conmigo? 💭",
"¿Qué te gustaría que hiciera por ti si estuviéramos juntos esta noche? 🌃",
"¿Qué parte del día sientes más deseo por mí? ⏰",
"¿Qué palabra te parece más sexy cuando te la digo? 💋",
"¿Te gusta cuando te hablo con picardía? 😈",
"¿Qué audio mío te ha encendido más? 🎧",
"¿Te gustaría mandarnos cartas o mensajes picantes por correo? 📬🔥",
"¿Alguna vez te has tocado pensando en mí? 🙃",
"¿Qué harías si estuviéramos solos en una habitación durante una hora? ⏳",
"¿Cómo crees que reaccionarías al verme desnudo/a por primera vez? 😯",
"¿Te gustaría que tuviéramos un código secreto para cosas íntimas? 🕵️‍♂️",
"¿Con qué frecuencia te gustaría tener sexo si estuviéramos juntos? 🧡",
"¿Qué olor te imaginas que tengo? 👃",
"¿Qué te gustaría probar conmigo cuando estemos juntos por primera vez? 💥",
"¿Qué parte de mi cuerpo imaginas tocando primero? 🤲",
"¿Qué te excita más de nuestras conversaciones? 📲🔥",
"¿Te gustaría verme en ropa interior? 😳",
"¿Cuál es tu mayor deseo erótico conmigo? 🍓",
"¿Te gustaría que escribiéramos relatos eróticos juntos? ✍️",
"¿Qué apodo íntimo te gustaría que te pusiera? 🐻",
"¿Te gustaría tener una noche sin límites conmigo? 🌙🔥",
"¿Qué cosas simples te excitan más de mí? 😉",
"¿Qué zona de tu cuerpo es más sensible? 👀",
"¿Te gustaría jugar a retos sexuales por videollamada? 📹🎮",
"¿Qué juguete sexual te gustaría que usáramos a distancia? 🎁😈",
"¿Te gustaría dormir conmigo en llamada algunas noches? 📞🛌",
"¿Qué tipo de ropa crees que me quedaría mejor para seducirte? 👠",
"¿Qué te gustaría que te susurrara al oído en la cama? 🎧💓",
"¿Crees que el deseo se puede mantener con palabras? 💬🔥",
"¿Te gustaría hacer sesiones picantes de preguntas y respuestas conmigo? ❓🔥",
"¿Qué palabra te gustaría escuchar durante el sexo? 🗣️",
"¿Eres más de caricias lentas o de pasión intensa? 👐🔥",
"¿Qué significa para ti el sexo en una relación de pareja? ❤️",
"¿Qué momento íntimo te imaginas más claramente conmigo? 🌠",
"¿Te excita verme reír? 😂💘",
"¿Cuál sería el lugar más excitante para hacerlo por primera vez? 🌍🔥",
"¿Cuál es tu parte favorita de nuestros momentos íntimos a distancia? 📲💓",
"¿Qué te gustaría experimentar conmigo que nunca hayas hecho? 🔥🤯",
"¿Te gustaría grabarnos en algún momento juntos? 🎥🙈",
"¿Qué fantasía crees que podríamos cumplir la primera semana de vernos? 📅🔥",
"¿Cuál es tu mayor inseguridad física? 🪞",
"¿Qué harías si estuviéramos en una cama de hotel juntos ahora mismo? 🛏️😈",
"¿Qué piensas cuando me imaginas desnudo/a? 💭👀",
"¿Prefieres luces encendidas o apagadas al hacer el amor? 💡🌑",
"¿Qué parte de tu cuerpo te gustaría que acariciara primero? ✋",
"¿Te gusta recibir órdenes sexuales o darlas? 🎙️",
"¿Qué tipo de besos prefieres? 💋",
"¿Te gustaría tener una playlist sexual conmigo? 🎶🔥",
"¿Qué harías si te susurrara al oído lo mucho que me gustas? 🎧💓",
"¿Qué palabra o frase te enciende más? 😈",
"¿Qué tipo de fotos íntimas te gustaría que compartiéramos? 📷🙈",
"¿Qué emoji usarías para representar nuestras noches juntos? 🔥👀",
"¿Qué harías si estuviéramos solos en un jacuzzi ahora mismo? 🛁💋",
"¿Crees que nuestra conexión sexual puede ser fuerte sin contacto físico? 💌🔥",
"¿Qué tipo de lencería te gustaría que usara para ti? 🩱",
"¿Te gustaría que tuviéramos un ritual íntimo cada noche? 🌙💞",
"¿Qué hora del día crees que sería perfecta para hacer el amor conmigo? 🕓",
"¿Qué tipo de beso te gustaría recibir la primera vez que estemos frente a frente? 💑",
"¿Qué te parece más sensual: una mirada o un susurro? 👁️👂",
"¿Qué comida asociarías a una noche de pasión conmigo? 🍫🍓",
"¿Qué es lo más sexy que alguien te ha dicho (y que te gustaría que te dijera yo)? 🔥",
"¿Te gusta más provocar o que te provoquen? 😈😇",
"¿Qué te gustaría que hiciera si te tomara de la mano en la cama? ✋🛏️",
"¿Cuál es tu palabra favorita para referirte al sexo? 📖",
"¿Te gustaría tener un código secreto para el deseo? 🔐💋",
"¿Te excita la idea de una ducha juntos? 🚿😉",
"¿Qué canción te gustaría escuchar mientras hacemos el amor? 🎵🔥",
"¿Qué significa el deseo para ti? 🔥💭",
"¿Qué harías si ahora mismo estuviéramos solos en tu casa? 🏠🔥",
"¿Qué prefieres: besos en el cuello o mordiscos suaves? 💋🐾",
"¿Te excita más la voz, el cuerpo o los mensajes? 🎧👀📱",
"¿Qué frase me dirías al oído antes de hacer el amor? 💬👂",
    # Añade más preguntas aquí hasta llegar a más de 200
]

preguntas_respondidas = {}
respuestas = {}

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    preguntas_respondidas[chat_id] = []
    respuestas[chat_id] = {"Eduardo": {}, "Anabel": {}}
    update.message.reply_text("¡Bienvenido! Usa /pregunta para comenzar.")

def pregunta(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if chat_id not in preguntas_respondidas:
        preguntas_respondidas[chat_id] = []
        respuestas[chat_id] = {"Eduardo": {}, "Anabel": {}}
    
    disponibles = [p for p in preguntas if p not in preguntas_respondidas[chat_id]]
    
    if not disponibles:
        update.message.reply_text("Ya han contestado todas las preguntas. Usa /reset para empezar de nuevo.")
        return
    
    pregunta_elegida = random.choice(disponibles)
    preguntas_respondidas[chat_id].append(pregunta_elegida)
    update.message.reply_text(f"Pregunta: {pregunta_elegida}\nCada uno puede responder con /responder seguido de su respuesta.")

def responder(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    user = update.message.from_user.first_name
    response_text = " ".join(context.args)
    
    if chat_id not in preguntas_respondidas or not preguntas_respondidas[chat_id]:
        update.message.reply_text("No hay pregunta activa. Usa /pregunta para obtener una.")
        return

    pregunta_actual = preguntas_respondidas[chat_id][-1]
    respuestas[chat_id]