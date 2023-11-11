---
## Front matter
title: "Лабораторная работа № 4"
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

Целью данной лабораторной работы является получение практических навыков работы в консоли с расширенными
атрибутами файлов.

# Выполнение лабораторной работы

1. Я определил расширенные атрибуты файла «file1» от имени пользователя guest. Далее я установил на «file1» права, разрешающие чтение и запись для владельца файла. После я попробовал установить на файл расширенный атрибут «a» от имени пользователя guest(@fig:001).

![Создание и редактирование атрибутов файла](./image/img1.png){#fig:001}

В ответ я получил отказ от выполнения операции.

2. Я повысил свои права с помощью команды su и попробовал установить расширенный атрибут a на файл «file1» от имени суперпользователя и проверил правильность установления атрибута(@fig:002).

![Редактирование атрибутов файла с правами root-пользователя](./image/img2.png){#fig:002}

3. Выполните дозапись в файл «file1» слово «test», после этого выполнил чтение файла командой « cat» чтобы убедиться, что слово test было успешно записано в «file1»(@fig:003).

![Дозапись и вывод содержимого файла](./image/img3.png){#fig:003}

4. Я попробовал стереть имеющуюся в файле «file1» информацию, переименовать файл и установить на файл «file1» права, например, запрещающие чтение и запись для владельца файла(@fig:004).

![Отказ в доступа на совершение определенных операций](./image/img4.png){#fig:004}

Однако в ответ я получил отказ от выполнения операции.

5. Я снял расширенный атрибут «a» с файла и повторил операции, которые мне ранее не удавалось выполнить(@fig:005).

![Cовершение определенных операций без атрибута «a»](./image/img5.png){#fig:005}

Все команды были успешно выполнены.

6. Я повторил свои действия по шагам, заменив атрибут «a» атрибутом «i»(@fig:006).

![Попытки совершения определнных операций с атрибутом «i»](./image/img6.png){#fig:006}

И получил отказ при любой попытке выполнить любую операцию.

# Выводы 

В ходе проделанной работы были получены практические навыки работы в консоли с атрибутами файлов.

# Список литературы{.unnumbered}

[1] (https://esystem.rudn.ru/pluginfile.php/2090277/mod_resource/content/3/004-lab_discret_extattr.pdf)