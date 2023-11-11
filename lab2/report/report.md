---
## Front matter
title: "Лабораторная работа № 2"
subtitle: "Дисциплина: Информационная безопасность"
author: "Сулицкий Богдан Романович"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: false
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---


# Цель работы

Целью данной работы является получение практических навыков работы в консоли с атрибутами файлов, закрепление теоретических основ дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux.

# Выполнение лабораторной работы

1. Я создал учетную запись пользователя guest и задал пароль(@fig:001).

![Создание и настройка пароля учетной записи](./image/img1.png){#fig:001}


2. Я вошёл в систему от имени пользователя guest(@fig:002).

![Вход в новосозданную учетную запись](./image/img2.png){#fig:002}

3. Я определил директорию, в которой нахожусь, после чего перешел в домашнюю папку польщователя guest(@fig:003).

![Проверка текущей директории](./image/img3.png){#fig:003}

4. Я уточнил имя пользователя(@fig:004).

![Проверка имени пользователя](./image/img4.png){#fig:004}

5. Я уточнил имя пользователя, его группу, а также группы, куда входит пользователя(@fig:005).

![Проверка данных пользователя](./image/img5.png){#fig:005}

6. Я просмотрел файл /etc/passwd(@fig:006).

![Содержимое файла passwd с ключевым словом guest](./image/img6.png){#fig:006}

7. Я определил существующие в системе директории(@fig:007).

![Содержимое директории](./image/img7.png){#fig:007}

8. Я проверил, какие расширенные атрибуты установлены на поддиректориях текущего пользователя, находящихся в директории /home(@fig:008).

![Проверка расширенных атрибутов директории](./image/img8.png){#fig:008}

9. Я создал в домашней директории поддиректорию dir1 и вывел права доступа и расширенные атрибуты(@fig:009).

![Создание поддиректории и проверка прав доступа и атрибутов](./image/img9.png){#fig:009}

10. Я снял с директории dir1 все атрибуты(@fig:010).

![Снятие всех прав доступа и атрибутов с поддиректории](./image/img10.png){#fig:010}

11. Я попытался создать в поддиректории dir1 файл file1(@fig:011).

![Создание файла file1 в поддиректории dir1](./image/img11.png){#fig:011}

Поскольку я не обладаю правами, я не могу создать файл, вследствие чего получил ошибку Permission Denied.

12. Я заполнил таблицу установленных прав и разрешённых действий(@fig:012).

![Таблица 2.1 - «Установленные права и разрешённые действия»](./image/img12.png){#fig:012 width=80%}

13. Я заполнил таблицу минимальных прав для совершения операций(@fig:013).

![Таблица 2.2 - «Минимальные права для совершения операций»](./image/img13.png){#fig:013}

# Выводы

В ходе проделанной работы были получены практические навыки работы в консоли с атрибутами файлов, а также были закреплены теоретические основы дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux.

# Список литературы{.unnumbered}

[1] https://esystem.rudn.ru/pluginfile.php/2090273/mod_resource/content/6/002-lab_discret_attr.pdf