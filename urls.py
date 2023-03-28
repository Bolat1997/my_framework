from views import Index, About, Author

# Набор привязок: путь-контроллер

routes = {
    '/': Index(),
    '/about/': About(),
    '/author/': Author(),
}