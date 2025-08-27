#!/usr/bin/env python
"""Запуск: python manage.py shell < test2.py"""

from django.core.mail import send_mail

try:
    send_mail(
        'Тестовое письмо',
        'Это тестовое письмо, отправленное из скрипта.',
        'noreply.electronstart@gmail.com',
        ['teterukrostislav@gmail.com'],
        fail_silently=False,
    )
    print('Письмо отправлено!')
except Exception as e:
    print(f'Ошибка при отправке письма: {e}')