
![](pics/presentation.png)

## о чем говорим сегодня?

- научимся создавать ветки
- научимся откладывать изменения до лучших времен
- поговорим о каноничном workflow
- немного tips&tricks

## ветвление (branches)

### немного комманд

- `git checkout -b develop` - создать новую ветку `develop` и переключиться на нее
- `git branch` - показать все ветки
- `git checkout master` - переключиться на главную ветку
- `git merge <branch>` - слить текущую ветку с веткой `<branch>`
- `git branch -d <branch>` - удалить ветку 
 - `-D` - принудительно удалить ветку
- `git merge <branch> --squash` - при слиянии веток собрать несколько коммитов в один

### создадим ветку `develop`
`git checkout -b develop`  

и посмотрим, какие ветки у нас теперь есть:  

`git branch`

![](pics/10.png)

### внесем в эту ветку изменения
например, поменяем файл `hello.txt` и закоммитим его новое состояние

![](pics/11.png)

### таким образом, у нас есть две версии файла `hello.txt`, между которыми можно переключаться

![](pics/13.png)

### чтобы наши изменения оказались в главной ветке, их надо слить

переключившись в ветку `master`, выполним:

`git merge develop`

![](pics/14.png)

## заначки (stash)

### немного комманд
- `git stash` - _спрятать_ свои правки
- `git stash apply` - применить изменения к текущей версии
- `git stash list` - вывести список изменений
- `git stash show` - вывести последние изменния
- `git stash drop` - удалить последние изменения в списке 
- `git stash pop` - [`apply`] + [`drop`]
- `git stash clear` - очистить список изменений

допустим, в главном репозитории полным ходом идет разработка

![](pics/1.png)

мы, в свою очередь, тоже не отстаем и изо всех сил вносим изменения

![](pics/2.png)

в таком случае, при попытке получить актуальную версию кода, Git одарит нас ошибкой:

![](pics/3.png)

### что же делать? -- прятать свой ~~говно~~код!

`git stash`

![](pics/4.png)

### тепреь мы можем скачать код из главного репозитория и попробовать применить свои изменения

`git pull`

`git stash pop`

![](pics/5.png)

### путь только один -- исправлять конфликт ручками

для этого можно использовать редактор/IDE/специальные программы для решения конфликтов, аля [Meld](http://meldmerge.org/)

![](pics/8.png)

### когда конфликт разрешен, можно спокойно отправлять свой код в репозиторий

![](pics/9.png)

## git workflow

![](https://habrastorage.org/storage/4bf7e68c/49e29c35/3a01bd6b/782a1be3.png)

### главные ветки - `master` и `develop`

![](http://nvie.com/img/main-branches@2x.png)

### под каждый новый функционал - отдельную ветку `feature` от ветки `develop`
   
`git checkout -b my_feature develop`

![](http://nvie.com/img/fb@2x.png)

### если в программе обнаруживается неисправность, требующая срочных исправлений - создается ветка `hotfix` от `master`, которая потом сливается и с `master`, и с `develop`

`git checkout -b hotfix master`

`git checkout master`

`git merge --no-ff hotfix`

`git branch -d hotfix`

![](https://habrastorage.org/storage/a303d38c/6c9c561c/8bcc22f7/3f8cbad4.png)

## semantic versioning

__ТЭГ__ == __Релиз__, используется для фиксирования версий вашего ПО

### немного комманд
- `git tag <name>` - создать тэг (например, v1.3.1)
- `git push --tags` - залить все тэги в репозиторий
- `git push <tag>` - залить конкретный тэг в репозиторий


Номер версии в формате __MAJOR.MINOR.PATCH__ задается следующим образом:

1. __MAJOR__ версия - увеличивается, когда сделаны обратно несовместимые изменения API (крупные релизы)
2. __MINOR__ версия - увеличивается, когда добавляется новый функционал, не нарушющий обратной совместимости (новые фичи)
3. __PATCH__ версия - увеличивается, когда вы делаете обратно совместимые исправления (исправления, фиксы)

## tips&tricks

- если отредактировано много файлов и добавлять сразу все __НЕ хочется__, то можно использовать `git add -i`

![](pics/18.png)

- файл `.gitignore` содержит описание файлов, которые git не будет отслеживать
    - например, если мы не хотим, чтобы в репозитории хранилась папка `.idea` и  все файлы формата `dll`, то пишем:
        - `.idea/`
        - `*.dll`

![](pics/15.png)

- `git log` - посмотреть историю коммитов в проекте

![](pics/16.png)

    - `git lg` - один из альтернативных вариантов истории коммитов, более наглядный для его использования надо создать алиас:

`git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%C(bold blue)<%an>%Creset' --abbrev-commit"`

![](pics/17.png)

## ДЗ

создать в своем форке репозитория myfirstproject новую ветку, накуролесить в ней, слить с главной и отпраивть Pull Request

## всякий референс

Git

- [Git Cheat Sheet](https://www.alexkras.com/getting-started-with-git/)
- [Git useful tips](https://ericdouglas.github.io/2016/04/01/Git-Useful-Tips/)

Ветвление

- [Глава 4. Чудеса ветвления](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/ch04.html)
- [Управление ветвлением и слиянием](http://uleming.github.io/gitbook/3_%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2%D0%B5%D1%82%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC_%D0%B8_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC.html)

Заначка

- [Инструменты Git - Прибережение и очистка](https://git-scm.com/book/ru/v2/%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-Git-%D0%9F%D1%80%D0%B8%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8-%D0%BE%D1%87%D0%B8%D1%81%D1%82%D0%BA%D0%B0)
- [Git Stash](https://www.atlassian.com/git/tutorials/git-stash/)


Воркфлоу и версии

- [Семантическое Версионирование 2.0.0](http://semver.org/lang/ru)
- [Удачная модель ветвления для Git](https://habrahabr.ru/post/106912/)
