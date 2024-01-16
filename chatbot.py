from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from modulo_personalizado import funcion_personalizada

def entrenar_chatbot(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.spanish')

def obtener_respuesta(chatbot, pregunta):
    respuesta = chatbot.get_response(pregunta)
    return str(respuesta)

def main():
    # Crear una instancia del chatbot
    chatbot = ChatBot('MiChatBot')

    # Entrenar al chatbot con datos predefinidos
    entrenar_chatbot(chatbot)

    # Loop de conversación
    while True:
        input_usuario = input("Tú: ")
        
        if input_usuario.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if input_usuario.lower() == 'funcion personalizada':
            resultado = funcion_personalizada()
            print("ChatBot:", resultado)
        else:
            respuesta_chatbot = obtener_respuesta(chatbot, input_usuario)
            print("ChatBot:", respuesta_chatbot)

if __name__ == "__main__":
    main()
