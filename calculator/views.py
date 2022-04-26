from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    number = int(request.GET.get("servings", 1))
    cook = DATA['omlet']
    txt = 'Ответ: <br>'
    for id in cook:
        txt = txt + str(id) + ': ' + str(round(number * float(cook[id]),2)) + '<br>'
    return HttpResponse(txt)

def pasta(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    number = int(request.GET.get("servings", 1))
    cook = DATA['pasta']
    txt = 'Ответ: <br>'
    for id in cook:
        txt = txt + str(id) + ': ' + str(round(number * float(cook[id]), 2)) + '<br>'
    return HttpResponse(txt)


def buter(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    number = int(request.GET.get("servings", 1))
    cook = DATA['buter']
    txt = 'Ответ: <br>'
    for id in cook:
        txt = txt + str(id) + ': ' + str(round(number * float(cook[id]),2)) + '<br>'
    return HttpResponse(txt)
