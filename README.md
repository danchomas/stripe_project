# Django Stripe API Integration

Проект реализует бэкенд для обработки платежей через Stripe API с использованием Django. Позволяет создавать товары, инициировать платежные сессии и обрабатывать результаты оплаты.

## Приложение доступно онлайн:  
[https://danchomas.pythonanywhere.com/](https://danchomas.pythonanywhere.com/item/1/)

### Тестовые данные:

- **Страница товара**: [https://danchomas.pythonanywhere.com/item/1/](https://danchomas.pythonanywhere.com/item/1/)
- **Оплата товара**: [https://danchomas.pythonanywhere.com/buy/1/](https://danchomas.pythonanywhere.com/buy/1/)

### Админ-панель:
- **URL**: [https://danchomas.pythonanywhere.com/admin/](https://danchomas.pythonanywhere.com/admin/)
- **Логин**: `admin`
- **Пароль**: `admin`

### Тестовые карты Stripe:
- **Номер**: `4242 4242 4242 4242`
- **Срок**: любая будущая дата
- **CVC**: любые 3 цифры

## Функционал

- Создание товаров через админку
- Получение HTML-страницы товара
- Создание платежной сессии для оплаты
- Страницы успешной оплаты и отмены
- Интеграция с Stripe Checkout
- Документация API через Swagger

##  Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/stripe-project.git
cd stripe_project
```

2. Создайте и активируйте виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate
```

3. Установите зависимости
```bash
pip install -r requirements.txt
```

4. Создайте файл .env по примеру
   
5. Примените миграции:
```bash
python3 manage.py migrate
```

6. Запустите сервер
```bash
python3 manage.py runserver
```

Документацию к каждому методу можно посмотреть перейдя по адресу http://localhost:8000/swagger/
