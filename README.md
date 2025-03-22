# Автоматизация тестирования с помощью Selenium и Python
## Законченая работа
### Заметки по пуктам проверок:
1. Тесты храняться в папке /tests как и должны
2. Вообще проект делался на uv, но requirements.txt тоже заморозил.
3. Все работает
4. Не могу обещать что всем все будет понятно, я писал тесты как считаю нужным, но изза некоторых требований курса приходилось делать компромисы. В результате единого стиля в проекте нет.
5. тесты промаркированы
6. Этот пункт я проигнорировал, потому что не согласен с ним. Много информации в тесте является устаревшей или не соответствует лучшим практикам.
Это идет прямо против лучших практик PageObject, не знаю где авторы это взяли если честно.

### Assertions in Page Objects

Page objects themselves should never make verifications or assertions.
This is part of your test and should always be within the test’s code, never in a page object.** 

https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/#:~:text=your%20test%20code.-,Assertions%20in%20Page%20Objects,never%20in%20a%20page%20object.