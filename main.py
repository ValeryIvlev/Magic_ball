import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
still = 'да'

while still.lower() == 'да':
    faq = input(f'Задай мне свой вопрос!')
    print(random.choice(answers))
    still = input("Есть еще вопросы? введи да/нет")
    if not still.lower() == 'да':
        break


