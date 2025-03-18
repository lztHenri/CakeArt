from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def process_message(message):
    message = message.lower()
    if "oi" in message or "olá" in message or "ola" in message:
        return "Olá! Em que posso ajudar?"
    
    elif "pedido" in message or "contato" in message or "sim" in message:
        return "Para realizar um pedido, entre em contato diretamente com a gente (64) 98459-0220"
    
    elif "encomenda" in message:
        return "Para encomendas, precisamos de pelo menos 3 dias de antecedência. Quer fazer um pedido?"
    
    elif "horario" in message or "funcionamento" in message:
        return "Estamos abertos de segunda a sexta das 8h às 18h e aos sábados das 8h às 12h"
    
    elif "localização" in message or "endereço" in message or "endereco" in message:
        return "Estamos localizados na Rua Tercio Campos Leao, Vila santo Antonio, N° 134 Casa 4, CEP: 75906-420"
    
    elif "sair" in message or "tchau" in message:
        return "Obrigado por entrar em contato. Até logo!"
    
    elif "instagram" in message:
        return "Siga a gente nas redes sociais @patricialorenzeto"
    
    elif "bolos" in message or "casamento" in message or "aniversário" in message or "festa" in message:
        return "Fazemos bolos diversos mas nosssa especialidade é com bolos em Pasta Americana, para casamentos, aniversários e festas em geral."
    
    elif "doces" in message:
        return "Temos uma grande variedade de doces, temos também doces a pronta-entrega, entre em contato para saber quais estão disponíveis (64) 98459-0220."
    
    elif "entrega" in message or "frete" in message or "intregas" in message:
        return "Fazemos entregas em toda cidade cobramos uma taxa de R$ 10,00. Para bairros mais afastados cobramos uma taxa R$ 15,00."   
    
    else :
        return "Desculpe, não entendi. Poderia reformular a pergunta?"
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message")
    resposta = process_message(user_message)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)