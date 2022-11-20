a = input('Введите выражение').split('+')
c = ''
summ = []
mlpl_tot = []
index_1 = 0

     for x in a:  # Сортируем, пары с умножением отдельно решать
        if not "*" in x and index_1 == 0:  # Eсли первое число слагаемое
            c = c.join(a[index_1])  # Убираем число которое будем складывать, оставляем только умножение.
            summ.append(c)
            summ = [int(x) for x in summ]
            c = ''
                # index_1 += 1  # Перепрыгиваем на след элемент a, который надо превратить в Int и умножить
            a = a[index_1 + 1:]#Ne uveren, chto nado bilo, no na vsiyakii sluchai udalem lishnee v virazhenii

        elif not "*" in x:#slagaemoe po sled krugu
            c = c.join(a[index_1])  # Убираем число которое будем складывать, оставляем только умножение.
            if c.isdigit():
                c = int(c)
                index_1 += 1  # Перепрыгиваем на след элемент a, который надо превратить в Int и умножить
                a = a[index_1:]

                elif "*" in x:  # Если первое число множитель
                    index_1 = 0
                    d = a[index_1]  # 1 Proizvedenie v spisok d
                    d = d.split('*')  # Sformirovali 1oe proizvedenie spiskom
                    mlpl_d = [int(x) for x in d]  # Pereveli v int

                    for i in d:
                       mlpl = mlpl_d[index_1] * mlpl_d[index_1 + 1]  # произведения двух последующих
                    mlpl_tot.append(mlpl)  # Formiruem itogovii list mnozhitelei
                    mlpl = 0  # Obnuliaem promezhutochnoe znachenie
                    a = a[index_1 + 1:]                     
                    index_1 = 0
                    index_1Total = sum(mlpl_tot+summ)
                    :print(f'Result : {Total}')
