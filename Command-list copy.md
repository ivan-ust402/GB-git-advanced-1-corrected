1. Выбрал проект GB-Python-intro-homework-1
2. Создал папку у себя на компьютере homework1. Открыл в терминале папку 
3. Склонировал репозиторий с GitHub: 
    git clone https://github.com/ivan-ust402/GB-python-intro-homework-1.git
4. Перешел в склонированный репозиторий:
    cd GB-python-intro-homework-1
5. Проверил гит:
    git status
6. Создал непустой удаленный репозиторий на Github с тем же названием, что и локальный проект GB-git-advanced-1-corrected
7. В файле REDME.md на первой строке создал конфиктную строку Conflict line 1
8. Закоммитил изменения в удаленном репозитории
9. В локальном репозитории удалил связь с первым удаленным репозиторием:
    git remote remove origin
    git remote -v - убеждаемся что нет связей
10. Делаем привязку локального репозитория к удаленному:
    git remote add origin path, где path - путь до удаленного репозитория https://github.com/ivan-ust402/GB-git-advanced-1-corrected.git
    Проверяем связь с удаленным репозиторием:
    git remote -v
11. Делаем изменения в склонированном репозитории, например в файле README.md допишем строку    test, закоммитим 
    git add .
    git commit -m "Local conflict line added"
12. Пытаемся отправить локальные коммиты на удаленный репозиторий и получаем ошибку:
    git push -u origin main

    ! [rejected]        main -> main (fetch first)
    error: failed to push some refs to 'https://github.com/ivan-ust402/GB-git-advanced-1-corrected.git'

13. Подгружаем коммиты из удаленного репозитория 
    git fetch
14. Смотрим разницу по коммитам
    git log origin/main ^main
15. Смотрим конфликт, в чем он заключается
    git diff hash_remote_commit
16. Можно смержить, но мы попробуем, возможно git автоматически сможет решить конфликт (заведомо зная, что это не так):
    git pull origin main - выпадает ошибка
    git merge origin/main - выпадает ошибка: fatal: refusing to merge unrelated histories
    Это ошибка возникает, когда объединяются два несвязных проекта (т.е., как в нашем случае, которые не знают о существоавнии друг друга и имеют несовпадающие истории коммитов). Для решения этой проблемы используют ключ: --allow-unrelated-histories
17. Пробуем смержить с ключом --allow-unrelated-histories:
    git merge origin/main --allow-unrelated-histories
18. Предлагается решить конфликт вручную, выбираем пункт который нас устраивает.
19. Принимаем оба варианта, и фиксируем изменения
    git add .
    git commit -m "Merge remote-tracking branch 'origin/main'"
20. Отправляем изменения на удаленный репозиторий:
    git push -u origin main

