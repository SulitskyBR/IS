---
## Front matter
lang: ru-RU
title: Лабораторная работа № 6
author:
  - Сулицкий Богдан Романович
group:
  - НФИбд-02-20, 1032201388
date: 2023, Москва

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
---

## Цель работы

Целью данной лабораторной работы является развитие навыков администрирования ОС Linux и получение первого практического знакомства с технологией SELinux

## Ход работы

![Getenforce, sestatus и service status](./image/img1.png){#fig:001 width=30%}

![Apache в списке процессов и состояния переключателей](./image/img2.png){#fig:002 width=25%}

## Ход работы

![Статистика по политике](./image/img3.png){#fig:003 width=30%}

![Проверка данных /var/www/ и /var/www/html](./image/img4.png){#fig:004 width=50%}

## Ход работы


![Содержимое файла test.html](./image/img5.png){#fig:005 width=50%}

![Проверка контектса файла](./image/img6.png){#fig:006 width=50%}

## Ход работы

![Отображение файла в браузере 1](./image/img7.png){#fig:007 width=25%}

## Ход работы

![Изменение контекста файла test.html 1](./image/img8.png){#fig:008 width=50%}

![Отображение файла в браузере 2](./image/img9.png){#fig:009 width=25%}

## Ход работы

![Просмотр информации о файле test.html и вывод log-файлов](./image/img10.png){#fig:010 width=50%}

![Изменения порта 1](./image/img11.png){#fig:011 width=50%}

## Ход работы

![Перезапуск веб-сервера 1](./image/img12.png){#fig:012 width=50%}

![Access_log и error_log](./image/img13.png){#fig:013 width=50%}

## Ход работы

![Привязка порта и проверка списка портов](./image/img14.png){#fig:014 width=50%}

![Перезапуск веб-сервера 2](./image/img15.png){#fig:015 width=50%}

## Ход работы

![Изменение контекста файла test.html 2](./image/img16.png){#fig:016 width=50%}

![Отображение файла в браузере 3](./image/img17.png){#fig:017  width=25%}

## Ход работы

![Изменения порта 2](./image/img18.png){#fig:018 width=50%}

![Удаление привязки порта и удаление файла test.html](./image/img19.png){#fig:019 width=50%}


## Вывод

В ходе проделанной лабораторной работы я развил своий навыки администрирования ОС Linux и получил первое практическое знакомствое с технологией SELinux