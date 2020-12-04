# SmartApp Framework

**SmartApp Framework** - это Python-фреймворк, который позволяет создавать смартапы для виртуальных ассистентов Салют. 


## Оглавление
   * [Конфигурация](#Конфигурация)
     * [Фреймворк и смартапы](#Фреймворк-и-смартапы)
     * [Инструменты фреймворка](#Инструменты-фреймворка)
     * [Рекомендованные требования](#Рекомендованные-требования)
   * [Настройка фреймворка](#Настройка-фреймворка)
     * [Установка проекта](#Установка-проекта)
     * [Создание проекта](#Создание-проекта)
     * [Тестирование онлайн](#Тестирование-онлайн) 
     * [Тестирование офлайн](#Тестирование-офлайн)    
   * [Документация и поддержка](#Документация-и-поддержка)

____

# Конфигурация

## Фреймворк и смартапы

Смартап - это приложение для виртуального ассистента Салют. С помощью смартапов пользователи могут вызвать такси, узнать погоду, управлять устройствами умного дома, записаться в салон красоты и совершить прочие действия, которые можно доверить ассистенту. 

Виртуальный ассистент понимает текущие намерения пользователя и для каждой его реплики подбирает соответствующий запрос на выполнение ([интент](https://developer.sberdevices.ru/docs/ru/platform_services/nlu_guidelines/intents_overview)). Поведение смартапа для различных интентов описывается с помощью сценариев. Интенты и сценарии связываются через смартапы, написанные на SmartApp Framework. 


## Инструменты фреймворка

Фреймворк содержит следующие инструменты:

* инструменты для создания сценариев;
* решения для автоматического тестирования;
* демо-приложение для просмотра примеров реализации; 
* готовые механизмы для слот-филлинга и извлечения сущностей из текста. 


## Рекомендованные требования

* Linux, Mac OS или Windows (необходима установка [Conda](https://docs.conda.io/en/latest/)).
* 512 МБ свободной памяти.
* Python 3.6.8 - 3.7.9.

____



# Настройка фреймворка


## Установка проекта

Для установки проекта выполните в терминале следующую команду:

```bash
python3 -m pip install git+https://github.com/sberdevices/smart_app_framework@main
```

## Создание проекта

Для создания проекта выполните в терминале следующую команду:
```bash
python3 -m smart_kit create_app <YOUR_APP_NAME>
```
После этого в текущей директории появится каталог с проектом. Он уже содержит в себе всё необходимое для запуска минимального приложения, включая базовый сценарий hello_scenario. Описание сценариев и форм можно найти в `<YOUR_APP_NAME>/static/references/`.


## Тестирование онлайн

Для тестирования онлайн вам понадобится мобильное приложение "СБЕР Салют" или собственное устройство, на котором будет запускаться смартап. Для такого тестирования:

1. Запустите в терминале dev сервер:

```bash
python3 manage.py run_app
```

2. Передайте в интернет порт. Для этого потребуется внешний IP-адрес. Если у вас его нет, воспользуйтесь специальными сервисами (например, Ngrok).
3. Зарегистрируйтесь в кабинете разработчика - [SmartAppStudio](https://smartapp-studio.sberdevices.ru/login).
4. Создайте в [SmartAppStudio](https://smartapp-studio.sberdevices.ru/login) свой смартап. 
5. Перейдите в настройки смартапа и укажите в поле "Настройки вебхука" адрес вашего сервера. Сохраните изменения.
6. Запустите свой смартап с помощью фразы "Запусти <имя приложения>". 

В терминале должны появиться записи о входящем сообщении, а ассистент ответит приветствием согласно сценарию hello_scenario.


## Тестирование офлайн

Ниже представлен пример команды для терминала при тестировании офлайн и пример ответа, который выводится на экране: 
```console
localhost:~$ python <YOUR_APP_NAME>/manage.py local_testing
Текущий сценарий: hello_scenario
Привет! Введите help или ? для вызова списка команд.
> set intent run_app // смена интента на другой. По умолчанию имя сценария совпадает с именем интента
intent = run_app
> Привет
pronounceText: Как тебя зовут?
```
____

# Документация и поддержка

Вы можете ознакомиться с подробной документацией по работе со SmartApp Framework в [справочнике разработчика](https://developer.sberdevices.ru/docs/ru/developer_tools/framework/overview.md).

C вопросами и предложениями пишите нам по адресу: developer@sberdevices.ru 
