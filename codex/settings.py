# Импорты
from pathlib import Path

# Определение базовой директории проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ
SECRET_KEY = 'django-insecure-%$!t113h%)xqvrt+t8_a(rl0rcpc)opv2q^e8ah=ofy1c*mn)^'

# Режим отладки
DEBUG = True

# Разрешенные хосты
ALLOWED_HOSTS = ["*"]

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'apps.yu',
]

# Промежуточное ПО
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корневой URL-конфигурации
ROOT_URLCONF = 'codex.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение
WSGI_APPLICATION = 'codex.wsgi.application'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Настройки валидации паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Языковая кодировка
LANGUAGE_CODE = "ru-RU"

# Часовой пояс
TIME_ZONE = "Europe/Moscow"

# Использование часового пояса
USE_TZ = True

# Использование международизации
USE_I18N = True

# URL для статических файлов
STATIC_URL = '/static/'

# Директории для статических файлов
STATICFILES_DIRS = [BASE_DIR]

# Настройки электронной почты SMTP
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aroniapharm@gmail.com'
EMAIL_HOST_PASSWORD = 'sflnaavfhlnqjphu'

# Настройки Celery для очереди задач
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

# Поле для автоинкремента
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
