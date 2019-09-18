from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response, get_most_frequent_response
from chatterbot.comparisons import levenshtein_distance
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch

bot = ChatBot('Norman',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": levenshtein_distance,
            'maximum_similarity_threshold': 0.90,
            'default_response': 'Disculpa, no te he entendido bien, mi único conocimiento es acerca de Representación del Conocimiento. ¿Puedes ser más específico?.'
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii'
    ],
    tie_breaking_method="random_response",
    read_only=True)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    "./data/basicES.yml",
    "./data/knwl-representation.yml",
    "./data/production-rules.yml",
   "./data/semantic-networks.yml",
    "./data/logicaPredicados.yml",
    "./data/frames.yml"
   )
while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
