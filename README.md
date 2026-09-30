\# QA Automation Project



&#x20;Проект по автоматизации тестирования веб-приложений на Python.



\## Цель проекта



Проект демонстрирует базовую структуру автоматизированных тестов для QA-инженера:



\- UI-тестирование веб-страниц через Selenium;

\- API-тестирование через Requests;

\- запуск тестов с помощью pytest;

\- использование фикстур для управления браузером;

\- разделение тестов на UI- и API-наборы;

\- маркировка smoke- и API-тестов;

\- формирование HTML- и JUnit XML-отчётов;

\- работа с виртуальным окружением Python;

\- хранение проекта в Git.



\## Что реализовано



\### UI-тесты



UI-тесты используют Selenium WebDriver и Chrome.



Проверяется:



\- загрузка страницы `example.com`;

\- корректность заголовка страницы;

\- наличие заголовка `h1`;

\- соответствие текста ожидаемому значению.



\### API-тесты



API-тесты используют библиотеку Requests и сервис `httpbin.org`.



Проверяется:



\- успешный GET-запрос;

\- HTTP-статус `200`;

\- передача query-параметра;

\- наличие JSON-поля `headers`;

\- корректность обработки ответа сервера.



\### Pytest



Pytest используется для:



\- обнаружения и запуска тестов;

\- создания фикстуры браузера;

\- группировки тестов по маркерам;

\- подробного вывода результатов;

\- формирования HTML-отчётов;

\- формирования JUnit XML-отчётов.



\## Структура проекта



```text

qa\_project/

├── tests/

│   ├── api/

│   │   └── test\_api.py

│   └── ui/

│       └── test\_example.py

├── conftest.py

├── pytest.ini

├── requirements.txt

├── .gitignore

└── README.md

```



\## Используемые технологии



\- Python 3.14+

\- pytest

\- Selenium WebDriver

\- Requests

\- Google Chrome

\- Git

\- GitHub



\## Установка



Клонируйте репозиторий:



```bash

git clone \[https://github.com/SiarheiBudanov/qa-automation-python.git](https://github.com/SiarheiBudanov/qa-automation-python.git)

cd qa-automation-python

```



Создайте виртуальное окружение:



```bash

python -m venv .venv

```



Активируйте его в Windows:



```bash

.venv\\Scripts\\activate

```



Установите зависимости:



```bash

python -m pip install -r requirements.txt

```



\## Запуск тестов



Запустить все тесты:



```bash

python -m pytest -v -p no:cacheprovider

```



Запустить только UI-тесты:



```bash

python -m pytest tests\\ui -v -p no:cacheprovider

```



Запустить только API-тесты:



```bash

python -m pytest -m api -v -p no:cacheprovider

```



Запустить smoke-тесты:



```bash

python -m pytest -m smoke -v -p no:cacheprovider

```



\## Отчёты



Создать HTML-отчёт:



```bash

python -m pytest -v -p no:cacheprovider \\

&#x20; --html=reports/report.html \\

&#x20; --self-contained-html

```



Создать JUnit XML-отчёт:



```bash

python -m pytest -v -p no:cacheprovider \\

&#x20; --junitxml=reports/test-results.xml

```



\## Результат последнего запуска



Последний запуск завершился успешно:



```text

4 passed in 9.39s

```



\## Назначение проекта



Проект создан для демонстрации практических навыков:



\- Python-автоматизации;

\- UI-тестирования;

\- API-тестирования;

\- работы с pytest;

\- подготовки тестового проекта к CI/CD;

\- использования Git и GitHub.



\## Дальнейшее развитие



Планируемые улучшения:



\- добавление Page Object Model;

\- добавление конфигурации окружений;

\- параметризация тестовых данных;

\- автоматические скриншоты при падении тестов;

\- запуск тестов в headless-режиме;

\- добавление GitHub Actions;

\- тестирование нескольких браузеров;

\- расширение API-проверок;

\- добавление логирования.

