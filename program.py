# Главная страница
def page():
    global one_btn, two_btn, three_btn, exit_btn

    # Фоновое изображение
    canvas.create_image(x / 2,
                        y / 2,
                        image=fon_path)

    # Текст
    canvas.create_text(x / 2,
                       5 * y / 20,
                       text='Выберите задание, ' + name,
                       fill='black',
                       font=(font_text, 48))

    # Кнопка "1 часть"
    one_btn = Button(root,
                     text="1 часть (тест, 1-19 задания)",
                     background=color_btn,
                     foreground="black",
                     font=(font_btn, 24, 'bold'),
                     activebackground=color_btn_act,
                     command=click_one_btn,
                     overrelief=RIDGE)
    one_btn.place(x=100 * x / 200,
                  y=9 * y / 20,
                  anchor='center')

    # Кнопка "2 часть"
    two_btn = Button(root,
                     text="2 часть (25 и 26 задачи)",
                     background=color_btn,
                     foreground="black",
                     font=(font_btn, 24, 'bold'),
                     activebackground=color_btn_act,
                     command=click_two_btn,
                     overrelief=RIDGE             )
    two_btn.place(x=100 * x / 200,
                  y=12 * y / 20,
                  anchor='center')

    # Кнопка "Тренировка"
    three_btn = Button(root,
                       text="Тренировка (определенный номер)",
                       background=color_btn,
                       foreground="black",
                       font=(font_btn, 24, 'bold'),
                       activebackground=color_btn_act,
                       command=click_three_btn,
                       overrelief=RIDGE)
    three_btn.place(x=100 * x / 200,
                    y=15 * y / 20,
                    anchor='center')

    # Кнопка "Выход"
    exit_btn = Button(root,
                      text="Выход",
                      background=color_btn,
                      foreground="black",
                      font=(font_btn, 24),
                      activebackground=color_btn_act,
                      command=command_exit,
                      overrelief=RIDGE)
    exit_btn.place(x=x / 2,
                   y=180 * y / 200,
                   anchor='center')


# Команда кнопки "Выход"
def command_exit():
    exit()


# Команда кнопки "1 часть"
def click_one_btn():
    global kind
    # Удаление
    canvas.delete(ALL)
    one_btn.destroy()
    two_btn.destroy()
    three_btn.destroy()
    exit_btn.destroy()

    # Запись вида работы в файл и переменную kind
    kind = open('work/kind.txt', 'w')
    kind.write('1')
    kind.close()
    kind_file = open('work/kind.txt', 'r')
    kind = int(kind_file.read())
    kind_file.close()

    # Работа "1 части" - 1
    nomera_one_part()


# Работа "1 части" - 1
def nomera_one_part():
    global v1, i, answers, variant

    # Выбор варианта
    v1 = random.randint(1, 52)

    # Запись варианта в файл и переменную variant
    variant = open('work/variant.txt', 'w')
    variant.write(str(v1))
    variant.close()
    variant_file = open('work/variant.txt', 'r')
    variant = int(variant_file.read())
    variant_file.close()

    # Начало отсчета времени
    Time = time.time()
    file = open('time/time.txt', 'w')
    file.write(str(int(Time)) + '\n')
    file.close()

    answers = []  # лист для ответов

    i = 1  # номер задания
    # изменение
    # Работа "1 части" - 2
    zadania_one_part()


# Работа "1 части" - 2
def zadania_one_part():
    global i, \
        ans, \
        ans_label, \
        ans_btn, \
        photo, \
        answers, \
        continue_btn, \
        back_btn, \
        number, \
        materials_btn, \
        task

    # Фоновое изображение
    canvas.create_image(x / 2,
                        y / 2,
                        image=fon_path)

    # Кнопка "Вернуться на главный экран"
    back_btn = Button(root,
                      text="Вернуться на\n главный экран",
                      background=color_btn,
                      font=(font_btn, 15, 'bold'),
                      command=command_back_btn,
                      activebackground=color_btn_act)
    back_btn.place(x=10,
                   y=10)

    # Проверка номера задания
    if i <= 19:

        # Запись номера задания в файл и переменную task
        task = open('work/task.txt', 'w')
        task.write(str(i))
        task.close()
        task_file = open('work/task.txt', 'r')
        task = int(task_file.read())
        task_file.close()

        # Заполнение пути к заданию
        v = '{}/{}/{}.png'.format(V, v1, i)  # путь к заданию

        # Текст ("Ответ:", "Задание №")
        ans_label = Label(root,
                          text='Ответ: ',
                          font=(font_btn, 25, 'bold'),
                          bg=color_fon)
        ans_label.place(x=0.9 * x,
                        y=725 * y / 1000,
                        anchor='center')
        number = Label(text='Задание №' + str(i),
                       font=(font_btn, 20, 'bold'),
                       bg=color_fon)
        number.place(x=0.9 * x,
                     y=660 * y / 1000,
                     anchor='center')

        # Поле ввода ответа
        ans = Entry(root,
                    bg=color_fon,
                    font=(font_btn, 25),
                    width=9)
        ans.place(x=0.9 * x,
                  y=800 * y / 1000,
                  anchor='center')

        # Кнопка "Отправить"
        ans_btn = Button(root,
                         text="Отправить",
                         background=color_btn,
                         foreground="black",
                         font=(font_btn, 15, 'bold'),
                         activebackground=color_btn_act,
                         command=command_ans_btn)
        ans_btn.place(x=0.9 * x,
                      y=870 * y / 1000,
                      anchor='center')

        # Задание
        photo = PhotoImage(file=v)
        canvas.create_image(x / 2,
                            y / 2,
                            image=photo)

        # Кнопка справочные материалы
        materials_btn = Button(root,
                               text='Справочные материалы',
                               font=(font_btn, 15, 'bold'),
                               command=materials,
                               activebackground=color_btn_act,
                               background=color_btn)
        materials_btn.place(x=x - 10,
                            y=10,
                            anchor='ne')

    else:

        p = 1  # номер задания
        o_y = 125 * y / 300  # координата высоты вывода ответа

        right = 0  # счетчик правильных ответов
        wrong = 0  # счетчик неправильных ответов

        # Фон ответов
        canvas.create_rectangle(125 * x / 400,
                                115 * y / 300,
                                270 * x / 400,
                                230 * y / 300,
                                fill='lightgray')

        # Вывод ответов
        while p <= len(answers) // 3:

            z = right_answers[p - 1]  # лист с правильными ответами задания p

            # Проверка правильности ответа
            if answers[p - 1] == z[v1 - 1]:
                color_answer = 'green'
                canvas.create_text(15 * x / 40,
                                   o_y,
                                   font=(font_btn, 15, 'bold'),
                                   text='№' + str(p) + ' - ' + str(answers[p - 1]),
                                   fill=color_answer,
                                   anchor='center')
                o_y += 40
                right += 1

            else:
                color_answer = 'red'
                canvas.create_text(15 * x / 40,
                                   o_y,
                                   font=(font_btn, 15, 'bold'),
                                   text='№' + str(p) + ' - ' + str(answers[p - 1]),
                                   fill=color_answer,
                                   anchor='center')
                o_y += 40
                wrong += 1

            p += 1

        o_y = 125 * y / 300

        while p <= 2 * len(answers) // 3:

            z = right_answers[p - 1]  # лист с правильными ответами задания p

            # Проверка правильности ответа
            if answers[p - 1] == z[v1 - 1]:
                color_answer = 'green'
                canvas.create_text(x / 2,
                                   o_y,
                                   font=(font_btn, 15, 'bold'),
                                   text='№' + str(p) + ' - ' + str(answers[p - 1]),
                                   fill=color_answer,
                                   anchor='center')
                o_y += 40
                right += 1

            else:
                color_answer = 'red'
                canvas.create_text(x / 2,
                                   o_y,
                                   font=(font_btn, 15, 'bold'),
                                   text='№' + str(p) + ' - ' + str(answers[p - 1]),
                                   fill=color_answer,
                                   anchor='center')
                o_y += 40
                wrong += 1

            p += 1

        o_y = 125 * y / 300

        while p <= len(answers):

            z = right_answers[p - 1]  # лист с правильными ответами задания p

            # Проверка правильности ответа
            if answers[p - 1] == z[v1 - 1]:
                color_answer = 'green'
                canvas.create_text(25 * x / 40,
                                   o_y,
                                   font=(font_btn, 15, 'bold'),
                                   text='№' + str(p) + ' - ' + str(answers[p - 1]),
                                   fill=color_answer,
                                   anchor='center')
                o_y += 40
                right += 1

            else:
                color_answer = 'red'
                canvas.create_text(25 * x / 40,
                                   o_y,
                                   font=(font_btn, 15, 'bold'),
                                   text='№' + str(p) + ' - ' + str(answers[p - 1]),
                                   fill=color_answer,
                                   anchor='center')
                o_y += 40
                wrong += 1

            p += 1

        # Конец отсчета времени
        Time = time.time()
        file = open('time/time.txt', 'a')
        file.write(str(int(Time)))
        file.close()
        file = open('time/time.txt', 'r')
        Time = list(file.read().split('\n'))
        Time = int(Time[1]) - int(Time[0])
        s = Time % 60
        m = Time % 3600 // 60
        h = Time // 3600
        s = str(s).rjust(2, '0')
        m = str(m).rjust(2, '0')
        h = str(h).rjust(2, '0')

        # Результаты и оценка
        percent = right * 100 / (right + wrong)
        mark = 2  # 2
        mark += percent >= 50  # 3
        mark += percent >= 70  # 4
        mark += percent >= 90  # 5
        if percent == 100: mark = str(mark) + '+'  # 5+

        # Запись результата в файл
        file = open('bin/users/user_' + ID + '.txt', 'r')
        user = file.read()
        number_of_works = user.count('Работа')
        file.close()
        file = open('bin/users/user_' + ID + '.txt', 'a')
        file.write(
            '\n' + str(right) + '/' + str(right + wrong) + '\n' + str(mark) + '\n\nРабота ' + str(number_of_works + 1))
        file.close()

        # Текст (конец выполнения варианта, потраченное время)
        canvas.create_text(x / 2,
                           y / 4,
                           font=(font_text, 25),
                           text='        Вы закончили делать ' + str(v1) + ' вариант\nВаша оценка: ' + str(
                               mark) + '  ( ' +
                                str(right) + ' | ' + str(wrong) + '; всего заданий ' + str(right + wrong) + ' )')
        canvas.create_text(x / 2,
                           y / 4 + 60,
                           font=(font_text, 25),
                           text='Потраченное время  ' + h + ':' + m + ':' + s)

        # Кнопка "Закончить"
        continue_btn = Button(root,
                              text="Закончить",
                              background=color_btn,
                              foreground="black",
                              font=(font_btn, 20, 'bold'),
                              activebackground=color_btn_act,
                              command=command_continue_btn)
        continue_btn.place(x=x / 2,
                           y=890 * y / 1000,
                           anchor='center')

        # Удаление кнопки "Вернуться на главный экран"
        back_btn.destroy()


# Команда кнопки "Отправить"
def command_ans_btn():
    global i, answers, ans, ans_label, ans_btn, photo, number, materials_btn

    # Следующее задание
    i += 1

    # Запись ответа
    answers.append(str(ans.get()))

    # Удаление
    canvas.delete(ALL)
    back_btn.destroy()
    ans.destroy()
    ans_btn.destroy()
    ans_label.destroy()
    materials_btn.destroy()
    number.destroy()

    # Начало выполнения заданий
    if kind == 1:
        # Работа "1 части" - 2
        zadania_one_part()
    elif kind == 2:
        # Работа "2 части" - 2
        zadania_two_part()
    else:
        # Работа "Тренировки" - 2
        zadania_trainning()


# Команда кнопки "2 часть"
def click_two_btn():
    global kind

    # Удаление
    canvas.delete(ALL)
    one_btn.destroy()
    two_btn.destroy()
    three_btn.destroy()
    exit_btn.destroy()

    # Запись вида работы в файл и переменную kind
    kind = open('work/kind.txt', 'w')
    kind.write('2')
    kind.close()
    kind_file = open('work/kind.txt', 'r')
    kind = int(kind_file.read())
    kind_file.close()

    # Работа "2 части" - 1
    nomera_two_part()


# Работа "2 части" - 1
def nomera_two_part():
    global v1, i, answers, variant

    # Выбор варианта
    v1 = random.randint(1, 52)

    # Запись номера варианта в файл и переменную variant
    variant = open('work/variant.txt', 'w')
    variant.write(str(v1))
    variant.close()
    variant_file = open('work/variant.txt', 'r')
    variant = int(variant_file.read())
    variant_file.close()

    # Начало отсчета времени
    Time = time.time()
    file = open('time/time.txt', 'w')
    file.write(str(int(Time)) + '\n')
    file.close()

    # Лист для ответов
    answers = []

    i = 25  # номер задания

    # Работа "2 части" - 2
    zadania_two_part()


# Работа "2 части" - 2
def zadania_two_part():
    global ans, ans_label, ans_btn, photo, answers, continue_btn, back_btn, materials_btn, number

    # Фоновое изображение
    fon = canvas.create_image(x / 2,
                              y / 2,
                              image=fon_path)

    # Проверка номера задания
    if i <= 26:

        # Кнопка "Вернуться на главный экран"
        back_btn = Button(root,
                          text="Вернуться на\n главный экран",
                          background=color_btn,
                          font=(font_btn, 15, 'bold'),
                          command=command_back_btn,
                          activebackground=color_btn_act)
        back_btn.place(x=10,
                       y=10)

        # Запись номера задания
        task = open('work/task.txt', 'w')
        task.write(str(i))
        task.close()

        # Кнопка "Справочные материалы"
        materials_btn = Button(root,
                               text='Справочные материалы',
                               font=(font_btn, 15, 'bold'),
                               command=materials,
                               activebackground=color_btn_act,
                               background=color_btn)
        materials_btn.place(x=x - 10,
                            y=10,
                            anchor='ne')

        # Заполнение пути к заданию
        v = '{}/{}/{}.png'.format(V, v1, i)  # путь к заданию

        # Поле ввода ответа
        ans = Entry(root,
                    bg=color_fon,
                    font=(font_btn, 25),
                    width=10)
        ans.place(x=0.9 * x,
                  y=800 * y / 1000,
                  anchor='center'
                  )

        # Текст ("Ответ: ", "Задание №")
        ans_label = Label(root,
                          text='Ответ: ',
                          font=(font_btn, 25, 'bold'),
                          bg=color_fon)
        ans_label.place(x=0.9 * x,
                        y=720 * y / 1000,
                        anchor='center'
                        )
        number = Label(root,
                       text='Задание №' + str(i),
                       font=(font_btn, 20, 'bold'),
                       bg=color_fon)
        number.place(x=0.9 * x,
                     y=660 * y / 1000,
                     anchor='center')

        # Кнопка "Отправить"
        ans_btn = Button(root,
                         text="Отправить",
                         background=color_btn,
                         foreground="black",
                         font=(font_btn, 15, 'bold'),
                         activebackground=color_btn_act,
                         command=command_ans_btn)
        ans_btn.place(x=0.9 * x,
                      y=875 * y / 1000,
                      anchor='center')

        # Задание
        photo = PhotoImage(file=v)
        canvas.create_image(x / 2,
                            y / 2,
                            image=photo)

        root.mainloop()

    else:

        p = 25  # Номер задания
        o_y = y / 3 + 35  # координата высоты вывода ответа

        right = 0  # счетчик правильных ответов
        wrong = 0  # счетчик неправильных ответов

        # Вывод ответов
        while p - 25 < len(answers):

            z = right_answers[p - 1]  # лист с правильными ответами задания p

            # Проверка правильности ответа
            if answers[p - 25] == z[v1 - 1]:
                color_answer = 'green'
                canvas.create_text(x / 2,
                                   o_y,
                                   font=(font_ans, 15),
                                   text='№' + str(p) + ' - ' + str(answers[p - 25]),
                                   fill=color_answer,
                                   anchor='center')
                o_y += 20
                right += 1

            else:
                color_answer = 'red'
                canvas.create_text(x / 2,
                                   o_y,
                                   font=(font_ans, 15),
                                   text='№' + str(p) + ' - ' + str(answers[p - 25]),
                                   fill=color_answer,
                                   anchor='center')
                o_y += 20
                wrong += 1

            p += 1

        # Окончание отсчета времени
        Time = time.time()
        file = open('time/time.txt', 'a')
        file.write(str(int(Time)))
        file.close()
        file = open('time/time.txt', 'r')
        Time = list(file.read().split('\n'))
        file.close()
        Time = int(Time[1]) - int(Time[0])
        s = Time % 60
        m = Time // 60
        h = Time // 3600
        s = str(s).rjust(2, '0')
        m = str(m).rjust(2, '0')
        h = str(h).rjust(2, '0')

        # Результаты и оценка
        percent = right * 100 / (right + wrong)
        mark = 2  # 2
        mark += percent >= 50  # 3
        mark += percent >= 70  # 4
        mark += percent >= 90  # 5
        if percent == 100: mark = str(mark) + '+'  # 5+

        # Запись результата в файл
        file = open('bin/users/user_' + ID + '.txt', 'r')
        user = file.read()
        number_of_works = user.count('Работа')
        file.close()
        file = open('bin/users/user_' + ID + '.txt', 'a')
        file.write(
            '\n' + str(right) + '/' + str(right + wrong) + '\n' + str(mark) + '\n\nРабота ' + str(number_of_works + 1))
        file.close()

        # Текст (конец варианта, время)
        canvas.create_text(x / 2,
                           y / 4,
                           font=(font_text, 25),
                           text='Вы закончили делать ' + str(v1) + ' вариант')
        canvas.create_text(x / 2,
                           y / 4 + 30,
                           font=(font_text, 25),
                           text='Ваша оценка: ' + str(mark) +
                                '  ( ' + str(right) + ' | ' + str(wrong) + '; всего заданий ' + str(
                               right + wrong) + ' )')
        canvas.create_text(x / 2,
                           y / 3,
                           font=(font_text, 20),
                           text='Потраченное время  ' + h + ':' + m + ':' + s)

        # Кнопка "Закончить"
        continue_btn = Button(root,
                              text="Закончить",
                              background=color_btn,
                              foreground="black",
                              font=(font_btn, 30, 'bold'),
                              activebackground=color_btn_act,
                              command=command_continue_btn)
        continue_btn.place(x=x / 2,
                           y=500 * y / 1000,
                           anchor='center')


# Команда кнопки "Вернуться на главный экран"
def command_back_btn():
    # Удаление
    canvas.delete(ALL)
    back_btn.destroy()
    ans.destroy()
    ans_btn.destroy()
    ans_label.destroy()
    number.destroy()
    materials_btn.destroy()

    # Главная страница
    page()


# Команда кнопки "Тренировка"
def click_three_btn():
    global choice, zadania, kind

    # Удаление
    canvas.delete(ALL)
    one_btn.destroy()
    two_btn.destroy()
    three_btn.destroy()
    exit_btn.destroy()

    # Список переменных кнопок выбора заданий
    choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
    choice_8, choice_9, choice_10, choice_11, choice_12, choice_13, choice_14, choice_25 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
    choice_15, choice_16, choice_17, choice_18, choice_19, choice_20, choice_21, choice_26 = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
    choice = [choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7,
              choice_8, choice_9, choice_10, choice_11, choice_12, choice_13, choice_14,
              choice_15, choice_16, choice_17, choice_18, choice_19,
              choice_25, choice_26]

    # Запись вида работы в файл и переменную kind
    kind = open('work/kind.txt', 'w')
    kind.write('3')
    kind.close()
    kind_file = open('work/kind.txt', 'r')
    kind = int(kind_file.read())
    kind_file.close()

    # Кнопки выбора заданий
    list_zadanii()


# Кнопки выбора заданий
def list_zadanii():
    global choice, checkbuttons, list_zadanii_btn, kolichestvo, back_btn_3

    # Фоновое изображение
    canvas.create_image(x / 2,
                        y / 2,
                        image=fon_path)

    # Текст
    canvas.create_text(40 * x / 80,
                       8 * y / 50,
                       text='Выберите задания',
                       font=(font_text, 42))
    canvas.create_text(28 * x / 80,
                       16 * y / 50,
                       text='1 часть',
                       font=(font_text, 24))
    canvas.create_text(55 * x / 80,
                       16 * y / 50,
                       text='2 часть',
                       font=(font_text, 24))
    canvas.create_text(27 * x / 40,
                       23.5 * y / 40,
                       font=(font_text, 18),
                       text='Количество вариантов')

    checkbuttons = []  # список с ссылками на кнопки заданий

    a = 0  # номер переменной кнопки (лист choice)
    v2 = 20  # координата высоты кнопок
    v3 = 5  # координата ширины кнопок
    l = 0  # номер столбца

    # Столбцы кнопок (1-16)
    while l < 4:

        for i in range(4):
            a1 = '№' + str(a + 1)  # текст кнопки
            v1 = choice[a]  # переменная кнопки

            # Кнопка
            choice_checkbutton = Checkbutton(root,
                                             text=a1,
                                             variable=v1,
                                             font=(font_btn, 20, 'bold'),
                                             bg=color_fon,
                                             activebackground=color_fon,
                                             indicatoron=True,
                                             overrelief=SUNKEN)
            checkbuttons.append(choice_checkbutton)
            choice_checkbutton.pack()
            choice_checkbutton.place(x=v3 * x / 25,
                                     y=v2 * y / 50)

            v2 += 4
            a += 1

        v2 = 20
        v3 += 2
        l += 1

    v2 = 36  # координата высоты кнопок
    v3 = 6  # координата ширины кнопок

    # Строка кнопок (17-19)
    for i in range(3):
        a1 = '№' + str(a + 1)  # текст кнопки
        v1 = choice[a]  # переменная кнопки

        # Кнопка
        choice_checkbutton = Checkbutton(root,
                                         text=a1,
                                         variable=v1,
                                         font=(font_btn, 20, 'bold'),
                                         bg=color_fon,
                                         activebackground=color_fon,
                                         indicatoron=True,
                                         overrelief=SUNKEN)
        checkbuttons.append(choice_checkbutton)
        choice_checkbutton.pack()
        choice_checkbutton.place(x=v3 * x / 25,
                                 y=v2 * y / 50)

        v3 += 2
        a += 1

    v2 = 20  # координата высоты кнопок
    v3 = 15  # координата ширины кнопок

    # Кнопки заданий 2 части (25-26)
    for i in range(2):
        a1 = '№'  # текст кнопки
        v1 = choice[a]  # переменная кнопки

        # Кнопка
        choice_checkbutton = Checkbutton(root,
                                         text=a1 + str(i + 25),
                                         variable=v1,
                                         font=(font_btn, 20, 'bold'),
                                         bg=color_fon,
                                         activebackground=color_fon,
                                         indicatoron=True,
                                         overrelief=SUNKEN)
        checkbuttons.append(choice_checkbutton)
        choice_checkbutton.pack()
        choice_checkbutton.place(x=v3 * x / 25,
                                 y=v2 * y / 50)

        v3 += 2
        a += 1

    # Кнопка "Начать"
    list_zadanii_btn = Button(root,
                              text="Начать",
                              background=color_btn,
                              foreground="black",
                              font=(font_btn, 24, 'bold'),
                              activebackground=color_btn_act,
                              command=command_list_zadanii)
    list_zadanii_btn.place(x=25 * x / 40,
                           y=30 * y / 40)

    # Поле ввода количества вариантов
    kolichestvo = Entry(root,
                        bg=color_fon,
                        font=(font_btn, 20),
                        width=7)
    kolichestvo.place(x=27 * x / 40,
                      y=26 * y / 40,
                      anchor='center')

    # Кнопка "Назад"
    back_btn_3 = Button(root,
                        text="Назад\n<===",
                        background=color_btn,
                        font=(font_btn, 15, 'bold'),
                        command=command_back_3,
                        width=5,
                        height=1,
                        activebackground=color_btn_act)
    back_btn_3.place(x=10,
                     y=10)


# Команда кнопки "Назад"
def command_back_3():
    # Удаление
    canvas.delete(ALL)
    i = 0
    while i < len(checkbuttons):
        checkbuttons[i].destroy()
        i += 1
    back_btn_3.destroy()
    list_zadanii_btn.destroy()
    kolichestvo.destroy()

    # Главная страница
    page()


# Команда кнопки "Начать" (Заполнение введенных данных)
def command_list_zadanii():
    global choice, checkbuttons, list_zadanii_btn, zadania, kolichestvo, number_of_variants, back_btn_3_1

    i = 0

    check = []  # список с флажками (значения '0'-нет или '1'-да)

    # Заполнение списка с флажками
    while i < len(choice):
        check.append(choice[i].get())
        i += 1

    # Проверка выбора заданий
    if check.count(1) == 0:
        canvas.create_text(36 * x / 100,
                           50 * y / 60,
                           text='Вы не выбрали задания!',
                           fill='red',
                           font=(font_btn, 23, 'bold'),
                           anchor='center'
                           )

    else:

        zadania = []  # список заданий

        i = 0

        # Заполнение списка заданий (используя значения из списка с флажками)
        while i < 19:
            if check[i] == 1:
                zadania.append(i + 1)
            i += 1
        if check[25 - 6] == 1:
            zadania.append(25)
        if check[26 - 6] == 1:
            zadania.append(26)

        # Проверка выбора количества вариантов
        if str(kolichestvo.get()) == '':

            canvas.create_text(68 * x / 100,
                               423 * y / 600,
                               text='Выберите, сколько вариантов\n         Вы хотите решить',
                               fill='red',
                               font=(font_btn, 20, 'bold'),
                               anchor='center'
                               )

        else:

            number_of_variants = int(kolichestvo.get())  # количество заданий

            # Проверка ненулевого выбора количества вариантов
            if number_of_variants == 0:

                canvas.create_text(68 * x / 100,
                                   423 * y / 600,
                                   text='Выберите, сколько вариантов\n         Вы хотите решить',
                                   fill='red',
                                   font=(font_btn, 20, 'bold'),
                                   anchor='center'
                                   )

            else:

                # Удаление
                canvas.delete(ALL)
                i = 0
                while i < len(checkbuttons):
                    checkbuttons[i].destroy()
                    i += 1
                list_zadanii_btn.destroy()
                kolichestvo.destroy()
                back_btn_3.destroy()

                # Работа "Тренировки" - 1
                beginning_training()


# Работа "Тренировки" - 0 (Создание списка с оценками)
def beginning_training():
    global k, marks

    k = 0  # номер варианта (пройденное количество вариантов)
    marks = []  # оценки

    # Работа "Тренировки" - 1
    variant_trenirovka()


# Работа "Тренировки" - 1 (Выбор варианта)
def variant_trenirovka():
    global k, v1, i, number_of_variants, answers, marks, continue_btn, variant

    # Фоновое изображение
    fon = canvas.create_image(x / 2,
                              y / 2,
                              image=fon_path)

    answers = []  # список ответов

    i = 0  # номер задания

    # Проверка номера варианта
    if k < number_of_variants:

        # Выбор варианта
        v1 = random.randint(1, 52)

        # Запись варианта в файл и переменную variant
        variant = open('work/variant.txt', 'w')
        variant.write(str(v1))
        variant.close()
        variant_file = open('work/variant.txt', 'r')
        variant = int(variant_file.read())
        variant_file.close()

        # Начало отсчета времени
        Time = time.time()
        file = open('time/time.txt', 'w')
        file.write(str(int(Time)) + '\n')
        file.close()

        # Работа "Тренировки" - 2
        zadania_trainning()

    else:

        l = 1

        marks_end = str(marks[0])  # строка всех оценок

        # Заполнение всех оценок в одну строку
        while l < len(marks):
            marks_end = marks_end + ', ' + str(marks[l])
            l += 1

        # Кнопка "Закончить"
        continue_btn = Button(root,
                              text="Закончить",
                              background=color_btn,
                              foreground="black",
                              font=(font_btn, 20, 'bold'),
                              activebackground=color_btn_act,
                              command=command_continue_btn)
        continue_btn.place(x=x / 2,
                           y=700 * y / 1000,
                           anchor='center')

        # Текст
        canvas.create_text(x / 2,
                           y / 3,
                           text='Вы закончили работу',
                           font=(font_text, 40))
        canvas.create_text(x / 2,
                           y / 2,
                           text='Ваши результаты: ',
                           font=(font_text, 25))
        canvas.create_text(x / 2,
                           23 * y / 40,
                           text=marks_end,
                           font=(font_text, 35))


# Команда кнопки "Закончить"
def command_continue_btn():
    global continue_btn

    # Удаление
    canvas.delete(ALL)
    continue_btn.destroy()

    # Главная страница
    page()


# Работа "Тренировки" - 2
def zadania_trainning():
    global i, k, v1, ans, ans_btn, ans_label, photo, continue_btn, answers, \
        right_answers, o_y, back_btn, back_btn_3_2, materials_btn, number, task

    # Фоновое изображение
    canvas.create_image(x / 2,
                        y / 2,
                        image=fon_path)

    # Проверка номера задания
    if i < len(zadania):

        # Кнопка "Вернуться на главный экран"
        back_btn = Button(root,
                          text="Вернуться на\n главный экран",
                          background=color_btn,
                          font=(font_btn, 15, 'bold'),
                          command=command_back_btn,
                          activebackground=color_btn_act
                          )
        back_btn.place(x=10,
                       y=10)

        # Кнопка "Справочные материалы"
        materials_btn = Button(root,
                               text='Справочные материалы',
                               font=(font_btn, 15, 'bold'),
                               command=materials,
                               activebackground=color_btn_act,
                               background=color_btn)
        materials_btn.place(x=x - 10,
                            y=10,
                            anchor='ne')

        # Заполнение пути к заданию
        number_z = zadania[i]  # номер задания

        v = '{}/{}/{}.png'.format(V, v1, number_z)  # путь к заданию

        # Запись номера задания в файл и переменную task
        task = open('work/task.txt', 'w')
        task.write(str(number_z))
        task.close()
        task_file = open('work/task.txt', 'r')
        task = int(task_file.read())
        task_file.close()

        # Поле ввода ответа
        ans = Entry(root,
                    bg=color_fon,
                    font=(font_btn, 25),
                    width=10)
        ans.place(x=0.9 * x,
                  y=800 * y / 1000,
                  anchor='center'
                  )

        # Текст
        ans_label = Label(root,
                          text='Ответ: ',
                          font=(font_btn, 25, 'bold'),
                          bg=color_fon)
        ans_label.place(x=0.9 * x,
                        y=730 * y / 1000,
                        anchor='center'
                        )
        number = Label(root,
                       text='Задание №' + str(number_z),
                       font=(font_btn, 20, 'bold'),
                       bg=color_fon)
        number.place(x=0.9 * x,
                     y=660 * y / 1000,
                     anchor='center')

        # Кнопка "Отправить"
        ans_btn = Button(root,
                         text="Отправить",
                         background=color_btn,
                         foreground="black",
                         font=(font_btn, 15, 'bold'),
                         activebackground=color_btn_act,
                         command=command_ans_btn
                         )
        ans_btn.place(x=0.9 * x,
                      y=870 * y / 1000,
                      anchor='center'
                      )

        # Задание
        photo = PhotoImage(file=v)
        canvas.create_image(x / 2,
                            y / 2,
                            image=photo)

        root.mainloop()

    else:

        # Конец отсчета времени
        Time = time.time()
        file = open('time/time.txt', 'a')
        file.write(str(int(Time)))
        file.close()
        file = open('time/time.txt', 'r')
        Time = list(file.read().split('\n'))
        file.close()
        Time = int(Time[1]) - int(Time[0])
        s = Time % 60
        m = Time % 3600 // 60
        h = Time // 3600
        s = str(s).rjust(2, '0')
        m = str(m).rjust(2, '0')
        h = str(h).rjust(2, '0')

        # Текст (конец варианта, время)
        canvas.create_text(x / 2,
                           y / 5,
                           font=(font_text, 25),
                           text='Вы закончили делать ' + str(k + 1) + ' вариант')
        canvas.create_text(x / 2,
                           y / 3,
                           font=(font_text, 25),
                           text='Потраченное время  ' + h + ':' + m + ':' + s)

        # Проверка ответов
        check()


# Команда кнопки "Вернуться на главный экран" в конце варианта "Тренировки"
def command_back_btn_3_2():
    # Удаление
    canvas.delete(ALL)
    back_btn_3_2.destroy()
    continue_btn.destroy()

    # Главная страница
    page()


# Проверка
def check():
    global right_answers, answers, zadania, marks, right, wrong, continue_btn, back_btn_3_2

    p = 1  # номер ответа
    o_y = 125 * y / 300  # координата высоты ответа
    right = 0  # счетчик правильных ответов
    wrong = 0  # счетчик неправильных ответов

    # Фон для ответов
    canvas.create_rectangle(125 * x / 400,
                            115 * y / 300,
                            270 * x / 400,
                            230 * y / 300,
                            fill='lightgray')

    # Вывод ответов
    while p <= len(answers) // 3:

        z = right_answers[zadania[p - 1] - 1]  # лист с правильными ответами задания p

        # Проверка правильности ответа
        if answers[p - 1] == z[v1 - 1]:
            color_answer = 'green'
            canvas.create_text(15 * x / 40,
                               o_y,
                               font=(font_btn, 15, 'bold'),
                               text='№' + str(p) + ' - ' + str(answers[p - 1]),
                               fill=color_answer,
                               anchor='center')
            o_y += 20
            right += 1

        else:
            color_answer = 'red'
            canvas.create_text(15 * x / 40,
                               o_y,
                               font=(font_btn, 15, 'bold'),
                               text='№' + str(p) + ' - ' + str(answers[p - 1]),
                               fill=color_answer,
                               anchor='center')
            o_y += 20
            wrong += 1

        p += 1

    o_y = 125 * y / 300

    while p <= 2 * len(answers) / 3:

        z = right_answers[zadania[p - 1] - 1]  # лист с правильными ответами задания p

        # Проверка правильности ответа
        if answers[p - 1] == z[v1 - 1]:
            color_answer = 'green'
            canvas.create_text(x / 2,
                               o_y,
                               font=(font_ans, 15, 'bold'),
                               text='№' + str(p) + ' - ' + str(answers[p - 1]),
                               fill=color_answer,
                               anchor='center')
            o_y += 20
            right += 1

        else:
            color_answer = 'red'
            canvas.create_text(x / 2,
                               o_y,
                               font=(font_btn, 15, 'bold'),
                               text='№' + str(p) + ' - ' + str(answers[p - 1]),
                               fill=color_answer,
                               anchor='center')
            o_y += 20
            wrong += 1

        p += 1

    o_y = 125 * y / 300

    while p <= len(answers):

        z = right_answers[zadania[p - 1] - 1]  # лист с правильными ответами задания p

        # Проверка правильности ответа
        if answers[p - 1] == z[v1 - 1]:
            color_answer = 'green'
            canvas.create_text(25 * x / 40,
                               o_y,
                               font=(font_btn, 15, 'bold'),
                               text='№' + str(p) + ' - ' + str(answers[p - 1]),
                               fill=color_answer,
                               anchor='center')
            o_y += 20
            right += 1

        else:
            color_answer = 'red'
            canvas.create_text(25 * x / 40,
                               o_y,
                               font=(font_btn, 15, 'bold'),
                               text='№' + str(p) + ' - ' + str(answers[p - 1]),
                               fill=color_answer,
                               anchor='center')
            o_y += 20
            wrong += 1

        p += 1

    # Кнопка "Вернуться на главный экран"
    back_btn_3_2 = Button(root,
                          text="Вернуться на главный экран",
                          background=color_btn,
                          font=(font_btn, 15, 'bold'),
                          command=command_back_btn_3_2,
                          activebackground=color_btn_act
                          )
    back_btn_3_2.place(x=x / 2,
                       y=o_y + 30 + 50,
                       anchor='center')

    # Кнопка "Следующий вариант"
    continue_btn = Button(root,
                          text="Следующий вариант",
                          background=color_btn,
                          foreground="black",
                          font=(font_btn, 15, 'bold'),
                          activebackground=color_btn_act,
                          command=command_continue_btn_traning
                          )
    continue_btn.place(x=x / 2,
                       y=o_y + 30,
                       anchor='center')

    # Результаты и оценка
    percent = right * 100 / (right + wrong)
    mark = 2  # 2
    mark += percent >= 50  # 3
    mark += percent >= 70  # 4
    mark += percent >= 90  # 5
    if percent == 100: mark = str(mark) + '+'  # 5+
    marks.append(mark)

    # Текст
    canvas.create_text(x / 2,
                       y / 4,
                       font=(font_text, 25),
                       text='Ваша оценка: ' + str(mark) + '  ( ' +
                            str(right) + ' | ' + str(wrong) + '; всего заданий ' + str(right + wrong) + ' )')

    # Запись результата в файл
    file = open('bin/users/user_' + ID + '.txt', 'r')
    user = file.read()
    number_of_works = user.count('Работа')
    file.close()
    file = open('bin/users/user_' + ID + '.txt', 'a')
    file.write(
        '\n' + str(right) + '/' + str(right + wrong) + '\n' + str(mark) + '\n\nРабота ' + str(number_of_works + 1))
    file.close()


# Команда кнопки "Следующий вариант"
def command_continue_btn_traning():
    global k

    # Увеличение номера варианта
    k += 1

    # Удаление
    canvas.delete(ALL)
    continue_btn.destroy()
    back_btn_3_2.destroy()

    # Работа "Тренировки" - 1
    variant_trenirovka()


# Кнопка "Справочные материалы"
def materials():
    global back_to_task_btn

    # Удаление
    canvas.delete(ALL)
    ans_btn.destroy()
    ans_label.destroy()
    back_btn.destroy()
    number.destroy()
    ans.destroy()
    materials_btn.destroy()

    # Фоновое изображение
    canvas.create_image(x / 2,
                        y / 2,
                        image=fon_path)

    # Справочные материалы
    materials = PhotoImage(file=r'bin/photos/materials.png')
    canvas.create_image(x / 2,
                        y / 2,
                        image=materials)

    # Кнопка "Вернуться к выполнению задания"
    back_to_task_btn = Button(root,
                              text="Вернуться к выполнению задания",
                              background=color_btn,
                              foreground="black",
                              font=(font_btn, 15, 'bold'),
                              activebackground=color_btn_act,
                              command=command_back_to_task_btn
                              )
    back_to_task_btn.place(x=x - 10,
                           y=10,
                           anchor='ne')

    root.mainloop()


# Команда кнопки "Вернуться к выполнению задания"
def command_back_to_task_btn():
    # Удаление
    back_to_task_btn.destroy()
    canvas.delete(ALL)

    # Возвращение к работе
    if kind == 1:
        zadania_one_part()
    elif kind == 2:
        zadania_two_part()
    else:
        zadania_trainning()


def registration():
    global registration_btn, grade_entry, patronymic_entry, name_entry, surname_entry, password_entry

    # Удаление
    canvas.delete(ALL)
    registration_btn.destroy()
    login_btn.destroy()
    exit_btn.place(x=2 * x / 3,
                   y=2800 * y / 3000,
                   anchor='center')

    # Фоновое изображение
    fon = canvas.create_image(x / 2,
                              y / 2,
                              image=fon_path,
                              anchor='center')

    surname_entry = Entry(root,
                          bg=color_fon,
                          font=(font_btn, 30),
                          width=20)
    surname_entry.place(x=2 * x / 3,
                        y=1250 * y / 3000,
                        anchor='center')
    name_entry = Entry(root,
                       bg=color_fon,
                       font=(font_btn, 30),
                       width=20)
    name_entry.place(x=2 * x / 3,
                     y=1500 * y / 3000,
                     anchor='center')
    patronymic_entry = Entry(root,
                             bg=color_fon,
                             font=(font_btn, 30),
                             width=20)
    patronymic_entry.place(x=2 * x / 3,
                           y=1750 * y / 3000,
                           anchor='center')
    grade_entry = Entry(root,
                        bg=color_fon,
                        font=(font_btn, 30),
                        width=20)
    grade_entry.place(x=2 * x / 3,
                      y=2000 * y / 3000,
                      anchor='center')
    password_entry = Entry(root,
                           bg=color_fon,
                           font=(font_btn, 30),
                           width=20)
    password_entry.place(x=2 * x / 3,
                         y=2250 * y / 3000,
                         anchor='center')
    registration_btn = Button(root,
                              text="Зарегистрироваться",
                              background=color_btn,
                              foreground="black",
                              font=(font_btn, 25, 'bold'),
                              activebackground=color_btn_act,
                              command=command_registration_btn
                              )
    registration_btn.place(x=2 * x / 3,
                           y=2500 * y / 3000,
                           anchor='center')

    canvas.create_text(x / 2,
                       750 * y / 3000,
                       font=(font_text, 40),
                       text='Для регистрации Вам необходимо заполнить поля ниже')
    canvas.create_text(x / 2,
                       1250 * y / 3000,
                       font=(font_text,30),
                       text='Фамилия',
                       anchor='e')
    canvas.create_text(x / 2,
                       1500 * y / 3000,
                       font=(font_text, 30),
                       text='Имя',
                       anchor='e')
    canvas.create_text(x / 2,
                       1750 * y / 3000,
                       font=(font_text, 30),
                       text='Отчество',
                       anchor='e')
    canvas.create_text(x / 2,
                       2000 * y / 3000,
                       font=(font_text, 30),
                       text='Класс, буква (через пробел)',
                       anchor='e')
    canvas.create_text(x / 2,
                       2250 * y / 3000,
                       font=(font_text, 30),
                       text='Пароль', anchor='e')


def command_registration_btn():
    global btn

    if surname_entry.get() == '' or name_entry.get() == '' or patronymic_entry.get() == '' or grade_entry.get() == '' or password_entry.get() == '':
        canvas.create_text(x / 2,
                           1000 * y / 3000,
                           font=(font_text, 30),
                           text='Заполните все поля!',
                           anchor='center',
                           fill='red')


    else:
        files = len(os.listdir('bin/users_data'))
        users_file_path = r'bin/users_data/user_' + str(files + 1) + '.txt'
        users_file = open(users_file_path, 'w')
        users_file.write(str(password_entry.get()) + '\n' + str(surname_entry.get()) + '\n' + str(name_entry.get()) +
                         '\n' + str(patronymic_entry.get()) + '\n' + str(grade_entry.get()))
        users_file.close()
        users_file_path = r'bin/users/user_' + str(files + 1) + '.txt'
        users_file = open(users_file_path, 'w')
        users_file.write(str(surname_entry.get()) + ' ' + str(name_entry.get()) + ' ' + str(patronymic_entry.get()) +
                         '\n' + str(grade_entry.get()) + '\n\nРабота 1')
        users_file.close()

        # Удаление
        canvas.delete(ALL)
        registration_btn.destroy()
        grade_entry.destroy()
        patronymic_entry.destroy()
        name_entry.destroy()
        surname_entry.destroy()
        password_entry.destroy()
        login_btn.destroy()
        exit_btn.destroy()

        # Фоновое изображение
        fon = canvas.create_image(x / 2,
                                  y / 2,
                                  image=fon_path,
                                  anchor='center')

        btn = Button(root,
                     text="Понятно",
                     background=color_btn,
                     foreground="black",
                     font=(font_btn, 25, 'bold'),
                     activebackground=color_btn_act,
                     command=begin_1
                     )
        btn.place(x=x / 2,
                  y=1650 * y / 3000,
                  anchor='center')

        canvas.create_text(x / 2,
                           y / 3,
                           font=(font_text, 40),
                           text='Вы успешно зарегистрировались!')
        canvas.create_text(x / 2,
                           y / 3 + 60,
                           font=(font_text, 40),
                           text='Ваш ID № ' + str(files + 1))
        canvas.create_text(x / 2,
                           2 * y / 3,
                           font=(font_text, 40),
                           text='Пожалуйста, не забудьте его и Ваш пароль!')
        canvas.create_text(x / 2,
                           2 * y / 3 + 60,
                           font=(font_text, 40),
                           text='Они необходимы для повторного входа в систему')


def begin_1():
    global log, pas, beg, exit_btn

    canvas.delete(ALL)
    btn.destroy()

    # Фоновое изображение
    fon = canvas.create_image(x / 2,
                              y / 2,
                              image=fon_path,
                              anchor='center')

    # Поля ввода логина и пароля
    log = Entry(root,
                bg=color_fon,
                font=(font_btn, 30),
                width=20)
    log.place(x=x / 2,
              y=y / 2,
              anchor='w')
    pas = Entry(root,
                bg=color_fon,
                font=(font_btn, 30),
                width=20)
    pas.place(x=x / 2,
              y=y / 2 + 70,
              anchor='w')
    canvas.create_text(x / 2 - 20,
                       y / 2,
                       font=(font_text, 30),
                       text='ID',
                       anchor='e')
    canvas.create_text(x / 2 - 20,
                       y / 2 + 70,
                       font=(font_text, 30),
                       text='Пароль',
                       anchor='e')
    canvas.create_text(x / 2,
                       y / 3,
                       font=(font_text, 60),
                       text='Введите свои данные',
                       anchor='center')
    beg = Button(root,
                 text="Вход",
                 background=color_btn,
                 foreground="black",
                 font=(font_btn, 35, 'bold'),
                 activebackground=color_btn_act,
                 command=check_password
                 )
    beg.place(x=x / 2,
              y=2250 * y / 3000,
              anchor='center')

    # Кнопка "Выход"
    exit_btn = Button(root,
                      text="Выход",
                      background=color_btn,
                      foreground="black",
                      font=(font_btn, 24),
                      activebackground=color_btn_act,
                      command=command_exit,
                      overrelief=RIDGE
                      )
    exit_btn.place(x=x / 2,
                   y=180 * y / 200,
                   anchor='center')


def begin_2():
    global log, pas, beg, exit_btn

    canvas.delete(ALL)
    exit_btn.destroy()
    login_btn.destroy()
    registration_btn.destroy()

    # Фоновое изображение
    fon = canvas.create_image(x / 2,
                              y / 2,
                              image=fon_path,
                              anchor='center')

    # Поля ввода логина и пароля
    log = Entry(root,
                bg=color_fon,
                font=(font_btn, 30),
                width=20)
    log.place(x=x / 2,
              y=y / 2,
              anchor='w')
    pas = Entry(root,
                bg=color_fon,
                font=(font_btn, 30),
                width=20)
    pas.place(x=x / 2,
              y=y / 2 + 70,
              anchor='w')
    canvas.create_text(x / 2 - 20,
                       y / 2,
                       font=(font_text, 30),
                       text='ID',
                       anchor='e')
    canvas.create_text(x / 2 - 20,
                       y / 2 + 70,
                       font=(font_text, 30),
                       text='Пароль',
                       anchor='e')
    canvas.create_text(x / 2,
                       y / 3,
                       font=(font_text, 60),
                       text='Введите свои данные',
                       anchor='center')
    beg = Button(root,
                 text="Вход",
                 background=color_btn,
                 foreground="black",
                 font=(font_btn, 35, 'bold'),
                 activebackground=color_btn_act,
                 command=check_password
                 )
    beg.place(x=x / 2,
              y=2250 * y / 3000,
              anchor='center')

    # Кнопка "Выход"
    exit_btn = Button(root,
                      text="Выход",
                      background=color_btn,
                      foreground="black",
                      font=(font_btn, 24),
                      activebackground=color_btn_act,
                      command=command_exit,
                      overrelief=RIDGE
                      )
    exit_btn.place(x=x / 2,
                   y=180 * y / 200,
                   anchor='center')


def check_password():
    global ID, surname, name, patronymic

    ID = log.get()
    PASSWORD = pas.get()

    if ID == '':
        canvas.create_text(2 * x / 3 - 20,
                           y / 2 - 40,
                           text='Введите Ваш ID!',
                           font=(font_text, 10),
                           fill='red')
    elif PASSWORD == '':
        canvas.create_text(2 * x / 3 - 20,
                           y / 2 + 30,
                           text='Введите Ваш пароль!',
                           font=(font_text, 10),
                           fill='red')
    else:
        user_file = open('bin/users_data/user_' + ID + '.txt', 'r')
        user = user_file.read()
        i = user.index('\n')
        user_password = user[:i]
        user_file.close()

        # Проверка правильности пароля
        if PASSWORD == user_password:

            # Фиксирование активного пользователя
            file = open('work/id.txt', 'w')
            file.write(ID)
            file.close()

            # Удаление
            log.destroy()
            pas.destroy()
            beg.destroy()
            exit_btn.destroy()

            # Данные о пользователе
            text_file = open('bin/users/user_' + ID + '.txt', 'r')  # Открытие файла с данными
            user = str(text_file.read())  # Перенос информации с файла в переменную
            text_file.close()  # Закрытие файла с данными

            # Считывание имени, фамилии, отчества
            p = user.index('\n')
            name = user[:p]
            surname, name, patronymic = name.split(' ')

            page()

        else:
            canvas.create_text(x / 2,
                               2250 * y / 3000 + 60,
                               text='Неправильный ID или пароль',
                               font=(font_text, 20),
                               fill='red')


from tkinter import *
import random
import time
import os

V = 'bin/dataset'  # путь к базе данных

# Настройки цветовой гаммы
color_fon = '#D3D3D3'  # цвет фона программы
color_btn = '#A9A9A9'  # цвет кнопок
color_btn_act = color_btn  # цвет кнопок в активном состоянии

# Шрифты
font_text = 'IMPACT'  # шрифт текстов
font_btn = 'garamond'  # шрифт кнопок
font_ans = 'impact'  # шрифт ответов

# Создание окна
root = Tk()
root.attributes("-fullscreen",True)

x = root.winfo_screenwidth()  # ширина окна
y = root.winfo_screenheight()  # высота окна

canvas = Canvas(root,
                width=x+10,
                height=y+10,
                bd=-5)
canvas.pack()

fon_path = PhotoImage('bin/photos/background.png')  # фоновое изображение

# Фоновое изображение
fon = canvas.create_image(x / 2,
                          y / 2,
                          image=fon_path,
                          anchor='center')

# Загрузка ответов в список right_answers
right_answers = []
i = 1
while i <= 26:
    path = 'bin/answers/answers_.txt'
    path_1 = path[::-1]
    path = path_1.index('.')
    path_1 = path_1[:path + 1:] + str(i)[::-1] + path_1[path + 1::]
    path = path_1[::-1]
    right_answers_1 = open(file=path)
    right_answers_1 = list(right_answers_1.read().split('\n'))
    right_answers.append(right_answers_1)
    i += 1

canvas.create_text(x / 2,
                   40 * y / 200,
                   text='Добро пожаловать!',
                   fill='black',
                   font=(font_text, 70),
                   anchor='center')
canvas.create_text(x / 2,
                   8 * y / 20,
                   text='У Вас уже есть аккаунт или Вы здесь впервые?',
                   fill='black',
                   font=(font_text, 40))

login_btn = Button(root,
                   text="Вход",
                   background=color_btn,
                   foreground="black",
                   font=(font_btn, 25, 'bold'),
                   activebackground=color_btn_act,
                   command=begin_2
                   )
login_btn.place(x=x / 2,
                y=1750 * y / 3000,
                anchor='center')

registration_btn = Button(root,
                          text="Регистрация",
                          background=color_btn,
                          foreground="black",
                          font=(font_btn, 25, 'bold'),
                          activebackground=color_btn_act,
                          command=registration
                          )
registration_btn.place(x=x / 2,
                       y=2150 * y / 3000,
                       anchor='center')

# Кнопка "Выход"
exit_btn = Button(root,
                  text="Выход",
                  background=color_btn,
                  foreground="black",
                  font=(font_btn, 24),
                  activebackground=color_btn_act,
                  command=command_exit,
                  overrelief=RIDGE
                  )
exit_btn.place(x=x / 2,
               y=175 * y / 200,
               anchor='center')

root.mainloop()
