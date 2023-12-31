---
## Front matter
lang: ru-RU
title: Лабораторная работа № 2
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

Целью данной работы является получение практических навыков работы в консоли с атрибутами файлов, закрепление теоретических основ дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux.

## Ход работы

Создание учетной записи

![Создание и настройка пароля учетной записи](./image/img1.png){#fig:001 width=45%}

![Вход в новосозданную учетную запись](./image/img2.png){#fig:002 width=25%}


## Ход работы

Проверка состояния системы

![Проверка текущей директории](./image/img3.png){#fig:003 width=45%}

![Проверка имени пользователя](./image/img4.png){#fig:004 width=35%}

## Ход работы

![Проверка данных пользователя](./image/img5.png){#fig:005 width=85%}

![Содержимое файла passwd с ключевым словом guest](./image/img6.png){#fig:006 width=55%}

![Проверка расширенных атрибутов директории](./image/img8.png){#fig:008 width=60%}

## Ход работы

Операции с поддиректорией

![Создание поддиректории и проверка прав доступа и атрибутов](./image/img9.png){#fig:009 width=45%}

![Снятие всех прав доступа и атрибутов с поддиректории](./image/img10.png){#fig:010 width=45%}

![Создание файла file1 в поддиректории dir1](./image/img11.png){#fig:011 width=45%}


## Ход работы

![Таблица 2.1 - «Установленные права и разрешённые действия»](./image/img12.png){#fig:012 width=60%}

![Таблица 2.2 - «Минимальные права для совершения операций»](./image/img13.png){#fig:013 width=60%}

## Результаты

В ходе проделанной работы были получены практические навыки работы в консоли с атрибутами файлов, а также были закреплены теоретические основы дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux.
