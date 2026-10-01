\# QA Automation Python



&#x20;Проект по автоматизации тестирования веб-страниц и REST API с использованием Python.



Проект создан для практического перехода от ручного тестирования к автоматизации. В процессе разработки были последовательно настроены Python-окружение, pytest, Selenium, API-тестирование, Page Object Model, JSON Schema validation, логирование, отчётность и GitHub Actions.



Проект завершён как учебный QA Automation-проект с локальным запуском и CI-проверками в Chrome, Firefox и Edge.



\## Цели проекта



Основные цели:



\- создать рабочий проект автоматизации на Python;

\- научиться запускать тесты через pytest;

\- автоматизировать UI-проверки Selenium;

\- автоматизировать REST API-проверки;

\- использовать fixtures и параметризацию;

\- разделить тестовую логику и работу с приложением;

\- настроить отчёты и screenshots;

\- запускать проверки автоматически через GitHub Actions.



\## Исходная версия проекта



Работа началась с минимального Selenium-проекта:



\- Python virtual environment;

\- pytest;

\- Selenium WebDriver;

\- один UI-тест для `example.com`;

\- проверка title страницы;

\- проверка содержимого страницы;

\- fixture для создания браузера;

\- первый запуск тестов локально.



Первоначально тест проверял наличие элемента `h1`. После изменения содержимого `example.com` проверка была адаптирована к актуальному тексту страницы:



```python

assert "This domain is for use in documentation examples" in body\_text

```



На этом этапе были также настроены screenshots при падении тестов.




\## Этапы разработки



\### Этап 1. Настройка окружения



Были выполнены следующие действия:



1\. создан проект `qa-automation-python`;

2\. создано виртуальное окружение `.venv`;

3\. установлен Python;

4\. установлены pytest и Selenium;

5\. создан первый UI-тест;

6\. настроен запуск тестов через `python -m pytest`;

7\. добавлен `pytest.ini`;

8\. поиск тестов ограничен каталогом `tests`.



Финальная конфигурация pytest:



```ini

\[pytest]

testpaths =

&#x20;   tests

addopts = -v --strict-markers

markers =

&#x20;   ui: browser-based UI tests

&#x20;   api: API tests

```



Параметр `testpaths` нужен для того, чтобы pytest искал тесты только в проекте и не пытался сканировать системные каталоги Windows.



\### Этап 2. Первый UI-тест



Первый тест проверял заголовок страницы:



```python

def test\_example\_title(driver):

&#x20;   driver.get("\[https://example.com](https://example.com)")



&#x20;   assert driver.title == "Example Domain"

```



После этого был добавлен тест содержимого страницы.



В процессе разработки была исправлена проблема, при которой Selenium не находил `h1`. Причина заключалась не в pytest, а в изменившемся содержимом учебной страницы.



\### Этап 3. Screenshots при падении



Для диагностики ошибок добавлены автоматические screenshots.



При падении UI-теста screenshot сохраняется в:



```text

reports/screenshots/

```



Пример имени файла:



```text

tests\_ui\_test\_example.py\_test\_example\_page\_content.png

```



Generated screenshots не являются исходным кодом и не добавляются в Git.



\### Этап 4. Параметризация



Добавлена параметризация UI-тестов:



```python

@pytest.mark.parametrize(

&#x20;   "url, expected\_title",

&#x20;   \[

&#x20;       ("\[https://example.com](https://example.com)", "Example Domain"),

&#x20;       ("\[https://example.org](https://example.org)", "Example Domain"),

&#x20;   ],

)

def test\_example\_pages\_title(driver, url, expected\_title):

&#x20;   driver.get(url)



&#x20;   assert driver.title == expected\_title

```



Один тест проверяет несколько URL без копирования тестового кода.



\### Этап 5. Page Object Model



Добавлен Page Object:



```text

pages/example\_page.py

```



Page Object содержит:



\- URL страницы;

\- локаторы;

\- открытие страницы;

\- ожидание загрузки;

\- получение title;

\- получение текста body;

\- проверку текущего URL;

\- проверку ожидаемого содержимого.



Пример использования:



```python

page = ExamplePage(driver).open()



assert page.title == "Example Domain"

assert page.has\_expected\_content()

```



Page Object отделяет действия браузера от проверок теста и уменьшает дублирование кода.



\### Этап 6. API-тестирование



Добавлены API-тесты API-тесты используют библиотеку Requests и сервис httpbin.org.



Используемые учебные API:



\- httpbin;

\- JSONPlaceholder.



Проверяются:



\- GET-запрос;

\- HTTP-заголовки;

\- получение списка posts;

\- получение отдельного post;

\- создание post;

\- запрос несуществующего post;

\- отправка невалидных данных.

\- корректность обработки ответа сервера.

\- передача query-параметра;

\- наличие JSON-поля headers;



Все запросы выполняются с timeout:



```python

timeout=10

```



Это предотвращает бесконечное ожидание ответа внешнего API.



\### Этап 7. API-клиент



Для posts API создан отдельный клиент:



```text

clients/posts\_api.py

```



Клиент содержит методы:



```python

get\_posts()

get\_post(post\_id)

create\_post(payload)

```



Также добавлены:



\- `requests.Session`;

\- общий метод `\_request`;

\- логирование request и response;

\- проверка JSON Schema;

\- закрытие API-сессии.



Пример использования:



```python

response = posts\_api.get\_post(1)



assert response.status\_code == 200

```



\### Этап 8. Pytest fixtures



В `conftest.py` созданы общие fixtures:



```python

driver

posts\_api

```



`driver` отвечает за:



\- запуск браузера;

\- настройку headless-режима;

\- выбор браузера;

\- закрытие браузера.



`posts\_api` отвечает за:



\- создание API-клиента;

\- передачу клиента в тест;

\- закрытие HTTP-сессии после теста.



\### Этап 9. Негативные API-тесты



Добавлены проверки:



```python

def test\_get\_non\_existing\_post(posts\_api):

&#x20;   response = posts\_api.get\_post(9999)



&#x20;   assert response.status\_code == 404

```



Также добавлена параметризация невалидных payload:



```python

@pytest.mark.parametrize(

&#x20;   "payload",

&#x20;   \[

&#x20;       {},

&#x20;       {"title": ""},

&#x20;       {"body": ""},

&#x20;       {"userId": "invalid"},

&#x20;       {"title": None, "body": None, "userId": None},

&#x20;   ],

)

def test\_create\_post\_invalid\_payload(posts\_api, payload):

&#x20;   response = posts\_api.create\_post(payload)



&#x20;   assert response.status\_code in (201, 400, 422)

```



JSONPlaceholder является учебным fake API, поэтому некоторые некорректные payload могут быть приняты с кодом `201`. Эти тесты демонстрируют отправку различных данных, но не заменяют полноценную проверку бизнес-валидации реального приложения.



\### Этап 10. JSON Schema validation



Добавлена зависимость:



```text

jsonschema

```



Создана схема:



```text

schemas/post\_schema.py

```



Схема проверяет:



\- наличие `userId`;

\- наличие `id`;

\- наличие `title`;

\- наличие `body`;

\- типы полей;

\- минимальные значения идентификаторов;

\- отсутствие неожиданных полей.



Пример схемы:



```python

POST\_SCHEMA = {

&#x20;   "$schema": "\[https://json-schema.org/draft/2020-12/schema](https://json-schema.org/draft/2020-12/schema)",

&#x20;   "type": "object",

&#x20;   "required": \["userId", "id", "title", "body"],

&#x20;   "properties": {

&#x20;       "userId": {

&#x20;           "type": "integer",

&#x20;           "minimum": 1,

&#x20;       },

&#x20;       "id": {

&#x20;           "type": "integer",

&#x20;           "minimum": 1,

&#x20;       },

&#x20;       "title": {

&#x20;           "type": "string",

&#x20;       },

&#x20;       "body": {

&#x20;           "type": "string",

&#x20;       },

&#x20;   },

&#x20;   "additionalProperties": False,

}

```



Проверка выполняется через:



```python

posts\_api.validate\_response\_schema(

&#x20;   response,

&#x20;   POST\_SCHEMA,

)

```



\### Этап 11. Логирование



Добавлено логирование API-запросов:



```text

HTTP request: GET \[https://jsonplaceholder.typicode.com/posts/1](https://jsonplaceholder.typicode.com/posts/1)

HTTP response: 200 \[https://jsonplaceholder.typicode.com/posts/1](https://jsonplaceholder.typicode.com/posts/1)

```



Базовый формат логов:



```text

%(asctime)s %(levelname)s %(name)s: %(message)s

```



Посмотреть логи локально:



```bat

python -m pytest tests\\api -v -s -p no:cacheprovider

```



\### Этап 12. Конфигурация окружений



Добавлена конфигурация:



```text

config/settings.py

```



Окружение выбирается переменной:



```text

TEST\_ENV

```



Пример:



```python

ENVIRONMENT = os.getenv("TEST\_ENV", "dev")

```



Доступные значения:



```text

dev

stage

```



Запуск в Windows CMD:



```bat

set TEST\_ENV=dev

python -m pytest tests\\api -v -p no:cacheprovider

```



Запуск в PowerShell:



```powershell

$env:TEST\_ENV="dev"

python -m pytest tests\\api -v -p no:cacheprovider

```



В текущем проекте `dev` и `stage` используют учебный URL. В реальном проекте они должны указывать на разные серверы.



\### Этап 13. Headless-режим



В CI браузеры запускаются без графического интерфейса.



Для Chrome и Edge используются параметры:



```text

\--headless=new

\--no-sandbox

\--disable-dev-shm-usage

```



Для Firefox:



```text

\-headless

```



Также используется:



```python

options.page\_load\_strategy = "eager"

```



Это уменьшает вероятность зависания загрузки страницы в CI.



Для браузера устанавливается ограничение:



```python

browser.set\_page\_load\_timeout(30)

```



\### Этап 14. Кроссбраузерный запуск



В проекте реализован выбор браузера через переменную:



```text

BROWSER

```



Поддерживаются:



```text

chrome

firefox

edge

```



Локальный запуск Chrome:



```bat

set BROWSER=chrome

python -m pytest tests\\ui -v -p no:cacheprovider

```



Локальный запуск Firefox:



```bat

set BROWSER=firefox

python -m pytest tests\\ui -v -p no:cacheprovider

```



Локальный запуск Edge:



```bat

set BROWSER=edge

python -m pytest tests\\ui -v -p no:cacheprovider

```



В GitHub Actions используется matrix:



```yaml

matrix:

&#x20; browser:

&#x20;   - chrome

&#x20;   - firefox

&#x20;   - edge

```



Для каждого браузера создаётся отдельный job:



```text

Tests - chrome

Tests - firefox

Tests - edge

```



\### Этап 15. GitHub Actions



Workflow находится в:



```text

.github/workflows/ui-tests.yml

```



Он запускается при:



\- push в `main`;

\- pull request в `main`.



Workflow выполняет:



1\. checkout репозитория;

2\. установку Python;

3\. установку зависимостей;

4\. установку браузера;

5\. запуск API-тестов;

6\. запуск UI-тестов;

7\. генерацию отчётов;

8\. сохранение artifacts.



Для каждого браузера создаются отдельные файлы:



```text

test-results-chrome.xml

test-results-firefox.xml

test-results-edge.xml

```



```text

report-chrome.html

report-firefox.html

report-edge.html

```



\### Этап 16. Отчёты



В проекте используются:



\- HTML report;

\- JUnit XML;

\- Allure results;

\- screenshots при падении.



Локальная генерация HTML и JUnit XML:



```bat

python -m pytest tests ^

&#x20; --junitxml=test-results.xml ^

&#x20; --html=report.html ^

&#x20; --self-contained-html ^

&#x20; -p no:cacheprovider

```



В Windows CMD символ `^` используется для переноса команды. Можно выполнить одной строкой:



```bat

python -m pytest tests --junitxml=test-results.xml --html=report.html --self-contained-html -p no:cacheprovider

```



Генерация Allure results:



```bat

python -m pytest tests --alluredir=allure-results -p no:cacheprovider

```



Для просмотра Allure отчёта локально при установленном Allure Commandline:



```bat

allure serve allure-results

```



Generated reports и `allure-results/` не добавляются в Git.



\## Структура проекта



```text

qa-automation-python/

├── .github/

│   └── workflows/

│       └── ui-tests.yml

├── clients/

│   ├── \_\_init\_\_.py

│   └── posts\_api.py

├── config/

│   ├── \_\_init\_\_.py

│   └── settings.py

├── pages/

│   ├── \_\_init\_\_.py

│   └── example\_page.py

├── schemas/

│   ├── \_\_init\_\_.py

│   └── post\_schema.py

├── tests/

│   ├── api/

│   │   ├── test\_api.py

│   │   ├── test\_posts.py

│   │   ├── test\_schema.py

│   │   └── test\_validation.py

│   └── ui/

│       └── test\_example.py

├── conftest.py

├── pytest.ini

├── requirements.txt

├── .gitignore

└── README.md

```



Generated files:



```text

report.html

test-results.xml

allure-results/

allure-report/

reports/

.pytest\_cache/

```



не являются исходным кодом проекта и должны игнорироваться Git.



\## Установка



Клонировать репозиторий:



```bash

git clone \[https://github.com/SiarheiBudanov/qa-automation-python.git](https://github.com/SiarheiBudanov/qa-automation-python.git)

cd qa-automation-python

```



Создать виртуальное окружение:



```bat

python -m venv .venv

```



Активировать окружение:



```bat

.venv\\Scripts\\activate

```



Обновить pip:



```bat

python -m pip install --upgrade pip

```



Установить зависимости:



```bat

python -m pip install -r requirements.txt

```



\## Запуск тестов



Все тесты:



```bat

python -m pytest tests -v -p no:cacheprovider

```



Только UI:



```bat

python -m pytest tests\\ui -v -p no:cacheprovider

```



Только API:



```bat

python -m pytest tests\\api -v -p no:cacheprovider

```



Только UI по marker:



```bat

python -m pytest -m ui -v -p no:cacheprovider

```



Только API по marker:



```bat

python -m pytest -m api -v -p no:cacheprovider

```



Запуск с логами:



```bat

python -m pytest tests\\api -v -s -p no:cacheprovider

```



\## Проверка результатов



Для проверки проекта локально:



```bat

python -m pytest tests -v -p no:cacheprovider

```



Ожидаемый результат:



```text

passed

```



API-набор в процессе разработки достиг:



```text

13 passed

```



Финальное количество тестов зависит от текущего состава schema-тестов и дополнительных UI-проверок. Поэтому основной критерий — отсутствие ошибок и успешный полный запуск, а не жёстко заданное число тестов.



\## Последний подтверждённый CI-результат



Последний успешный workflow:



```text

Ignore generated Allure results #18

```



Commit:



```text

679c538

```



Статус:



```text

Success

```



Выполнены успешно:



```text

Tests - chrome

Tests - firefox

Tests - edge

```



Созданы artifacts:



```text

reports-chrome

reports-firefox

reports-edge

```



Каждый artifact содержит отчёты соответствующего браузера.



Предупреждения о Node.js 20 и будущей миграции `ubuntu-latest` не повлияли на успешность тестов. Это предупреждения GitHub Actions runner и используемых actions, а не ошибки Python-кода.



\## Реализованные улучшения



Завершены следующие пункты:



\- добавлен Page Object Model;

\- добавлена параметризация тестовых данных;

\- добавлены автоматические screenshots при падении;

\- настроен headless-режим;

\- добавлено логирование API-запросов;

\- добавлена базовая конфигурация окружений;

\- расширены API-проверки;

\- добавлены негативные сценарии;

\- добавлены проверки невалидных данных;

\- добавлена JSON Schema validation;

\- добавлен запуск в Chrome, Firefox и Edge;

\- добавлен GitHub Actions matrix;

\- добавлены HTML и JUnit XML отчёты;

\- добавлен Allure results;

\- добавлены отдельные CI artifacts для браузеров.



\## Ограничения проекта



Проект является учебным.



Ограничения:



\- `example.com` используется как демонстрационная страница;

\- JSONPlaceholder является fake API;

\- `dev` и `stage` пока используют учебный URL;

\- негативные проверки JSONPlaceholder не отражают полноценную бизнес-валидацию настоящего backend;

\- Allure results создаются в CI, а полноценный Allure HTML не публикуется отдельной страницей;

\- нет тестовой базы данных и проверки данных на уровне SQL;

\- нет авторизации и работы с секретами.



Эти ограничения осознанны и не мешают демонстрации базовых навыков автоматизации.



\## Критерии завершения



Проект считается завершённым, потому что:



\- UI-тесты запускаются локально;

\- API-тесты запускаются локально;

\- JSON-ответы проверяются по схеме;

\- API-запросы логируются;

\- браузер выбирается через конфигурацию;

\- Chrome, Firefox и Edge запускаются в CI;

\- CI выполняется автоматически после push;

\- отчёты сохраняются как artifacts;

\- screenshots создаются при падении;

\- рабочая ветка `main` синхронизирована с GitHub;

\- README описывает архитектуру, запуск, этапы и итог.



\## Итог



Проект демонстрирует полный базовый цикл автоматизации:



```text

Python environment

→ pytest

→ Selenium UI tests

→ screenshots

→ parametrization

→ Page Object Model

→ API tests

→ API client

→ negative scenarios

→ JSON Schema

→ logging

→ environment configuration

→ cross-browser execution

→ HTML/JUnit/Allure reports

→ GitHub Actions

→ CI artifacts

```



Проект завершён в рамках учебной цели и может использоваться как портфолио-пример для демонстрации базовых навыков QA Automation на Python.

