# sonar-lab-7 — статичний аналіз коду SonarQube

| Поле | Значення |
|---|---|
| Студент | Чабан Володимир, група З-41 |
| Номер у списку | 35 → варіант 5 (35 mod 10) |
| Варіант | Аналіз тексту: кількість слів, речень, середня довжина слова |
| Мова | Python 3 |
| SonarQube | Community Build 26.11 (Docker), профіль «Sonar way comprehensive» |

## Файли

- `text_analyzer.py` — виправлена програма;
- `before/text_analyzer_before.py` — початкова версія з навмисними проблемами (виключена з аналізу);
- `test_text_analyzer.py` — тести pytest (покриття 90,5 %);
- `sonar-project.properties` — налаштування аналізу;
- `screenshots/` — дашборд SonarQube до та після виправлень.

## Як запустити аналіз

```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:community
# http://localhost:9000 → My Account → Security → Generate Token
pip install -r requirements.txt
pytest --cov=text_analyzer --cov-report=xml
docker run --rm -e SONAR_HOST_URL=http://host.docker.internal:9000 -e SONAR_TOKEN=<токен> \
  -v "$PWD:/usr/src" sonarsource/sonar-scanner-cli
```

## Результат

| Метрика | До | Після |
|---|---|---|
| Bugs | 1 | 0 |
| Code Smells | 11 | 0 |
| Дублювання | 29,0 % (3 блоки) | 0,0 % |
| Cognitive Complexity | 48 | 6 |
| Рядків коду | 103 | 42 |
| Покриття | — | 90,5 % |
| Quality Gate | Failed | **Passed** |
