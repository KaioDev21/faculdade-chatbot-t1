import random

from nltk.chat.util import Chat, reflections

listaJogos = {
    "The Legend of Zelda: Breath of the Wild": ["Ação-aventura", "Mundo aberto", "Fantasia"],
    "Red Dead Redemption 2": ["Ação-aventura", "Mundo aberto", "Velho Oeste"],
    "The Witcher 3: Wild Hunt": ["RPG", "Mundo aberto", "Fantasia"],
    "God of War": ["Ação-aventura", "Mundo aberto", "Mitologia"],
    "Minecraft": ["Sandbox", "Construção", "Aventura"],
    "Grand Theft Auto V": ["Ação-aventura", "Mundo aberto", "Crime"],
    "Dark Souls III": ["RPG", "Ação", "Fantasia"],
    "Horizon Zero Dawn": ["Ação-aventura", "Mundo aberto", "Ficção científica"],
    "Cyberpunk 2077": ["RPG", "Mundo aberto", "Ficção científica"],
    "Assassin's Creed Valhalla": ["Ação-aventura", "Mundo aberto", "Histórico"],
    "Among Us": ["Multijogador", "Social", "Mistério"],
    "Valorant": ["FPS", "Multijogador", "Competitivo"],
    "League of Legends": ["MOBA", "Multijogador", "Competitivo"],
    "Fortnite": ["Battle Royale", "Multijogador", "Construção"],
    "Call of Duty: Warzone": ["Battle Royale", "FPS", "Multijogador"],
    "Apex Legends": ["Battle Royale", "FPS", "Multijogador"],
    "Overwatch": ["FPS", "Multijogador", "Competitivo"],
    "Super Mario Odyssey": ["Plataforma", "Aventura", "Fantasia"],
    "Animal Crossing: New Horizons": ["Simulação", "Mundo aberto", "Social"],
}

def get_generos_jogo(jogo):
    keys = list(listaJogos.keys())
    for key in keys:
        if key.lower() == jogo.lower():
            return listaJogos[key]
    return None

def recomendar_jogo_por_genero(genero):
    print(f"Recomendando jogo do gênero: {genero}")
    jogos_recomendados = []
    for jogo, generos in listaJogos.items():
        if genero.lower() in [g.lower() for g in generos]:
            jogos_recomendados.append(jogo)
    if jogos_recomendados:
        return random.choice(jogos_recomendados)
    else:
        return False

def recomendar_jogo():
    randInt = random.randint(0, len(listaJogos) - 1)
    jogo = list(listaJogos.keys())[randInt]
    return jogo

pares = [
    (r"oi|olá|bom dia|boa tarde|boa noite|opa", [
        "Olá! Como posso ajudar?",
        "Oi tudo bem?",
    ]),
    (r"qual é o seu nome?", [
        "Meu nome é GameBot."
    ]),
    (r"qual é a sua função?| o que você faz?", [
        "Eu sou um chatbot que ajuda a escolher jogos da sua preferência.",
        "Posso recomendar jogos com base nos seus gostos e interesses."
    ]),
    (r"quais são os gêneros de jogos que você conhece?", [
        "Eu conheço muitos gêneros de jogos, como ação, aventura, RPG, FPS, estratégia, simulação, entre outros."
    ]),
    (r"meu nome é (.*), baseado em meu nome, me indique um jogo", [
        recomendar_jogo()+". Você gostaria de uma recomendação personalizada com base em seus gostos, %1?",
    ]),
    (r"me fale mais sobre o jogo (.*)| conte mais sobre o jogo (.*)| qual é o gênero do jogo (.*)?", [
        "__JOGO__%1",
    ]),
    (r"sim, me recomende um jogo de (.*)", [
        "__GENERO__%1",
    ]),
    (r"me recomende um jogo de (.*)", [
        "__GENERO__%1",
    ]),
    (r"tchau|adeus|até mais", [
        "Tchau! Foi bom conversar com você.", 
        "Adeus! Tenha um ótimo dia!"
    ]),
    (r"(.*)", [
        "Desculpe, não entendi.", 
        "Tendi nada kkk"
    ]),
]

reflections = {
    "eu": "você",
    "meu": "seu",
    "meus": "seus",
    "minha": "sua",
    "minhas": "suas",
    "me": "você",
    "você": "eu",
    "seu": "meu",
    "sua": "minha",
    "fui": "foi",
    "estou": "está",
}

chatbot = Chat(pares, reflections)

def iniciar_chat():
    print("Início da conversa")
    while True:
        entrada = input("Você: ")

        if entrada.lower() in ["tchau", "adeus", "até mais"]:
            print("ChatBot: Tchau! Foi bom conversar com você.")
            break
        resposta = chatbot.respond(entrada)

        if resposta and resposta.startswith("__GENERO__"):
            genero = resposta.replace("__GENERO__", "", 1).strip()
            jogo = recomendar_jogo_por_genero(genero)
            if jogo:
                resposta = f"Eu recomendo o jogo '{jogo}'."
            else:
                resposta = "Não tenho nenhum jogo com esse gênero"
        
        if resposta and resposta.startswith("__JOGO__"):
            jogo = resposta.replace("__JOGO__", "", 1).strip()
            generos = get_generos_jogo(jogo)
            if generos:
                resposta = f"O jogo '{jogo}' pertence aos gêneros: {', '.join(generos)}."
            else:
                resposta = "Não tenho informações sobre esse jogo."

        print("ChatBot:", resposta)

iniciar_chat()



#eu testei  esse codigo na aula de algoritmo e ele tava dando erro de loop porque o NLTK sempre que nao achava solucao jogava em None, e fica em loop eu fiz uma puta alteracao que ta funcionando vou colocar aqui em baixo
#tive ajuda do nosso amigo tio claudio para algumas coisas.

import random
from nltk.chat.util import Chat, reflections

listaJogos = {
    "The Legend of Zelda: Breath of the Wild": {
        "generos": ["Ação-aventura", "Mundo aberto", "Fantasia"],
        "desenvolvedor": "Nintendo",
        "dificuldade": "Médio",
    },
    "Red Dead Redemption 2": {
        "generos": ["Ação-aventura", "Mundo aberto", "Velho Oeste"],
        "desenvolvedor": "Rockstar Games",
        "dificuldade": "Médio",
    },
    "The Witcher 3: Wild Hunt": {
        "generos": ["RPG", "Mundo aberto", "Fantasia"],
        "desenvolvedor": "CD Projekt Red",
        "dificuldade": "Médio",
    },
    "God of War": {
        "generos": ["Ação-aventura", "Mundo aberto", "Mitologia"],
        "desenvolvedor": "Santa Monica Studio",
        "dificuldade": "Médio",
    },
    "Minecraft": {
        "generos": ["Sandbox", "Construção", "Aventura"],
        "desenvolvedor": "Mojang Studios",
        "dificuldade": "Fácil",
    },
    "Grand Theft Auto V": {
        "generos": ["Ação-aventura", "Mundo aberto", "Crime"],
        "desenvolvedor": "Rockstar Games",
        "dificuldade": "Médio",
    },
    "Dark Souls III": {
        "generos": ["RPG", "Ação", "Fantasia"],
        "desenvolvedor": "FromSoftware",
        "dificuldade": "Muito Difícil",
    },
    "Horizon Zero Dawn": {
        "generos": ["Ação-aventura", "Mundo aberto", "Ficção científica"],
        "desenvolvedor": "Guerrilla Games",
        "dificuldade": "Médio",
    },
    "Cyberpunk 2077": {
        "generos": ["RPG", "Mundo aberto", "Ficção científica"],
        "desenvolvedor": "CD Projekt Red",
        "dificuldade": "Médio",
    },
    "Assassin's Creed Valhalla": {
        "generos": ["Ação-aventura", "Mundo aberto", "Histórico"],
        "desenvolvedor": "Ubisoft",
        "dificuldade": "Médio",
    },
    "Among Us": {
        "generos": ["Multijogador", "Social", "Mistério"],
        "desenvolvedor": "Innersloth",
        "dificuldade": "Fácil",
    },
    "Valorant": {
        "generos": ["FPS", "Multijogador", "Competitivo"],
        "desenvolvedor": "Riot Games",
        "dificuldade": "Difícil",
    },
    "League of Legends": {
        "generos": ["MOBA", "Multijogador", "Competitivo"],
        "desenvolvedor": "Riot Games",
        "dificuldade": "Difícil",
    },
    "Fortnite": {
        "generos": ["Battle Royale", "Multijogador", "Construção"],
        "desenvolvedor": "Epic Games",
        "dificuldade": "Médio",
    },
    "Call of Duty: Warzone": {
        "generos": ["Battle Royale", "FPS", "Multijogador"],
        "desenvolvedor": "Infinity Ward",
        "dificuldade": "Difícil",
    },
    "Apex Legends": {
        "generos": ["Battle Royale", "FPS", "Multijogador"],
        "desenvolvedor": "Respawn Entertainment",
        "dificuldade": "Difícil",
    },
    "Overwatch": {
        "generos": ["FPS", "Multijogador", "Competitivo"],
        "desenvolvedor": "Blizzard Entertainment",
        "dificuldade": "Médio",
    },
    "Super Mario Odyssey": {
        "generos": ["Plataforma", "Aventura", "Fantasia"],
        "desenvolvedor": "Nintendo",
        "dificuldade": "Fácil",
    },
    "Animal Crossing: New Horizons": {
        "generos": ["Simulação", "Mundo aberto", "Social"],
        "desenvolvedor": "Nintendo",
        "dificuldade": "Fácil",
    },
}


def _encontrar_jogo(nome):
    for key in listaJogos:
        if key.lower() == nome.lower().strip():
            return key
    return None


def get_info_jogo(nome):
    key = _encontrar_jogo(nome)
    return listaJogos[key] if key else None


def get_generos_jogo(nome):
    info = get_info_jogo(nome)
    return info["generos"] if info else None


def get_desenvolvedor_jogo(nome):
    info = get_info_jogo(nome)
    return info["desenvolvedor"] if info else None


def get_dificuldade_jogo(nome):
    info = get_info_jogo(nome)
    return info["dificuldade"] if info else None


def recomendar_jogo_por_genero(genero):
    jogos_recomendados = [
        jogo for jogo, info in listaJogos.items()
        if genero.lower() in [g.lower() for g in info["generos"]]
    ]
    return random.choice(jogos_recomendados) if jogos_recomendados else None

def recomendar_jogo():
    return random.choice(list(listaJogos.keys()))


pares = [
    (
        r"oi|olá|ola|bom dia|boa tarde|boa noite|opa|hey|e aí|eai",
        [
            "Olá! Como posso ajudar?",
            "Oi, tudo bem?",
        ],
    ),
    (
        r"qual [eé] o seu nome|como voce se chama|quem [eé] você|tudo bem.*(e voce|e vc)",
        [
            "Meu nome é GameBot!",
            "Estou bem! Sou o GameBot, seu assistente de jogos.",
        ],
    ),
    (
        r"qual [eé] a sua função|o que voce faz|para que (voce serve|serve voce)",
        [
            "Sou um chatbot para recomendação de jogos! Posso sugerir títulos por gênero, "
            "informar o desenvolvedor, a dificuldade e muito mais.",
        ],
    ),
    (
        r"quais (são os |)(gêneros|generos)( que você conhece|)",
        [
            "Conheço gêneros como: Ação-aventura, RPG, FPS, MOBA, Battle Royale, "
            "Sandbox, Simulação, Plataforma, Multijogador e outros.",
        ],
    ),
    (
        r"(?:me recomende|recomende|me indique|indique|quero|sugira) (?:um |)jogo de (.*)",
        ["__GENERO__%1"],
    ),
    (
        r"me recomende um jogo|recomende um jogo|me indica um jogo|qual jogo (eu|devo) jogar",
        ["__ALEATORIO__"],
    ),
   
    (r"me fale sobre o jogo (.*)", ["__INFO__%1"]),
    (r"me fale mais sobre o jogo (.*)", ["__INFO__%1"]),
    (r"conte sobre o jogo (.*)", ["__INFO__%1"]),
    (r"conte mais sobre o jogo (.*)", ["__INFO__%1"]),
    (r"informações sobre (.*)", ["__INFO__%1"]),
    (r"infos do jogo (.*)", ["__INFO__%1"]),
    (r"info do jogo (.*)", ["__INFO__%1"]),

    (r"qual o desenvolvedor do jogo (.*)", ["__DEV__%1"]),
    (r"qual o desenvolvedor de (.*)", ["__DEV__%1"]),
    (r"qual a empresa do jogo (.*)", ["__DEV__%1"]),
    (r"qual o nome da empresa do jogo (.*)", ["__DEV__%1"]),
    (r"quem fez o jogo (.*)", ["__DEV__%1"]),
    (r"quem criou o jogo (.*)", ["__DEV__%1"]),
    (r"quem desenvolveu o jogo (.*)", ["__DEV__%1"]),

 
    (r"qual a dificuldade do jogo (.*)", ["__DIFIC__%1"]),
    (r"qual a dificuldade de (.*)", ["__DIFIC__%1"]),
    (r"qual o nível de dificuldade do jogo (.*)", ["__DIFIC__%1"]),
    (r"qual o nível de dificuldade de (.*)", ["__DIFIC__%1"]),

  
    (r"qual o gênero do jogo (.*)", ["__GENERO_JOGO__%1"]),
    (r"qual é o gênero do jogo (.*)", ["__GENERO_JOGO__%1"]),
    (r"que gênero é o jogo (.*)", ["__GENERO_JOGO__%1"]),
    (r"que gênero é (.*)", ["__GENERO_JOGO__%1"]),
    (
        r"tchau|adeus|até mais|até logo|xau",
        [
            "Tchau! Foi bom conversar com você.",
            "Adeus! Boas partidas!",
        ],
    ),
    (
        r"(.*)",
        [
            "Desculpe, não entendi. Tente perguntar sobre um jogo ou pedir uma recomendação!",
            "Hmm, não entendi. Tente: 'me recomende um jogo de RPG' ou 'qual o desenvolvedor de Minecraft'.",
        ],
    ),
]

reflections_pt = {
    "eu": "você",
    "meu": "seu",
    "meus": "seus",
    "minha": "sua",
    "minhas": "suas",
    "me": "você",
    "você": "eu",
    "seu": "meu",
    "sua": "minha",
    "fui": "foi",
    "estou": "está",
}

chatbot = Chat(pares, reflections_pt)

def _limpar_grupos(texto):
    limpo = texto.replace("None", "").strip()
    return limpo


def processar_resposta(resposta):

    if resposta is None:
        return "Desculpe, não entendi. Tente perguntar sobre um jogo ou pedir uma recomendação!"

    if resposta.startswith("__ALEATORIO__"):
        return f"Que tal '{recomendar_jogo()}'?"

    if resposta.startswith("__GENERO__"):
        genero = _limpar_grupos(resposta.replace("__GENERO__", "", 1))
        jogo = recomendar_jogo_por_genero(genero)
        if jogo:
            return f"Eu recomendo o jogo '{jogo}'!"
        return f"Não tenho nenhum jogo do gênero '{genero}' na minha lista."

    if resposta.startswith("__INFO__"):
        nome = _limpar_grupos(resposta.replace("__INFO__", "", 1))
        info = get_info_jogo(nome)
        if info:
            key = _encontrar_jogo(nome)
            return (
                f"'{key}':\n"
                f"  Gêneros: {', '.join(info['generos'])}\n"
                f"  Desenvolvedor: {info['desenvolvedor']}\n"
                f"  Dificuldade: {info['dificuldade']}"
            )
        return f"Não tenho informações sobre o jogo '{nome}'. Verifique se escreveu o nome completo e correto."

    if resposta.startswith("__DEV__"):
        nome = _limpar_grupos(resposta.replace("__DEV__", "", 1))
        dev = get_desenvolvedor_jogo(nome)
        if dev:
            key = _encontrar_jogo(nome)
            return f"O jogo '{key}' foi desenvolvido por {dev}."
        return f"Não encontrei o desenvolvedor do jogo '{nome}'. Verifique se escreveu o nome completo e correto."

    if resposta.startswith("__DIFIC__"):
        nome = _limpar_grupos(resposta.replace("__DIFIC__", "", 1))
        dif = get_dificuldade_jogo(nome)
        if dif:
            key = _encontrar_jogo(nome)
            return f"A dificuldade de '{key}' é: {dif}."
        return f"Não encontrei a dificuldade do jogo '{nome}'. Verifique se escreveu o nome completo e correto."

    if resposta.startswith("__GENERO_JOGO__"):
        nome = _limpar_grupos(resposta.replace("__GENERO_JOGO__", "", 1))
        generos = get_generos_jogo(nome)
        if generos:
            key = _encontrar_jogo(nome)
            return f"O jogo '{key}' pertence aos gêneros: {', '.join(generos)}."
        return f"Não encontrei informações sobre o jogo '{nome}'. Verifique se escreveu o nome completo e correto."

    return resposta


def iniciar_chat():
    print("=" * 50)
    print("  Bem-vindo ao GameBot!")
    print("  Digite 'tchau' para sair.")
    print("=" * 50)

    while True:
        try:
            entrada = input("\nVocê: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGameBot: Até mais!")
            break

        if not entrada:
            continue

        if entrada.lower() in ["tchau", "adeus", "até mais", "xau"]:
            print("GameBot: Tchau! Foi bom conversar com você.")
            break

        resposta_raw = chatbot.respond(entrada)
        resposta = processar_resposta(resposta_raw)
        print(f"GameBot: {resposta}")


if __name__ == "__main__":
    iniciar_chat()

