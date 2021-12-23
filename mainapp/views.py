from django.shortcuts import render


# возвращает результат рендеринга html файла, указываем относительный путь от папки templates
# удерживая клавишу Ctrl появляется рука можем посмотреть файл
def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'page_title': 'продукты'
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-800-495-5555',
            'email': 'info@geekshop.ru',
            'address': 'Ленинский проспект, дом 2',
        },
        {
            'city': 'Санкт-Петербург',
            'phone': '+7-812-800-4444',
            'email': 'hello@geekshop.ru',
            'address': 'ул., Айвазовского, дом 10',
        },
        {
            'city': 'Красноярск',
            'phone': '+7-800-800-3333',
            'email': 'menendger@geekshop.ru',
            'address': 'ул, Ленина, дом 1',
        },
    ]

    context = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)
