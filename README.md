# Проект VERSTKA_21_2

Это учебный проект для курса "VERSTKA_21_2".

## Описание

В этом проекте реализована верстка нескольких HTML-страниц и простой Python-сервер для их отображения.

### Реализованные страницы:
*   Главная (Glavnaya.html)
*   Каталог (catalog.html)
*   Категория (category.html)
*   Контакты (contact.html)

### Python-сервер (`python_server.py`)
Простой HTTP-сервер, который:
*   Обрабатывает GET-запросы.
*   Отдает HTML-страницы из локальных файлов.
*   (В последней версии) На любой GET-запрос возвращает страницу "Контакты" (`contact.html`).

## Как запустить

1.  Убедитесь, что у вас установлен Python.
2.  Склонируйте репозиторий (если он уже на GitHub):
    ```bash
    git clone https://github.com/Doczadrot/Verstka_21_2.git
    cd Verstka_21_2
    ```
3.  Перейдите в директорию проекта: `cd c:\Users\kisil\Desktop\VERSTKA_21_2` (или куда вы его сохранили).
4.  Запустите Python-сервер:
    ```bash
    python python_server.py
    ```
5.  Откройте в браузере `http://localhost:8080`.

## Используемые технологии
*   HTML
*   CSS (возможно, Bootstrap)
*   Python (модуль `http.server`)

## Автор
*   [Твое Имя или Ник] (Doczadrot)