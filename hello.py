from snoop import snoop
#tab="=============================================="
#print("Hello, Python!")
#print ("I'm learning Python for SDET")
#print ("Hellp, Python!\nI'm learning Python for SDET\n")

#print("Status:", end=" ")
#print("OK")

#print("Hello. Python!", end=" ")
#print("I'm learning Python for SDET")


#service_name = "kldfs"
#print(service_name)

#student_name = "Nikita"
#learning_goal = "SDET"

#print("Student:", student_name)
#print ("Goal:", learning_goal)

#service_name = "kldfs"
#service_name = "test-service"

#print(service_name)

#attempts = 3
#extra_attempts = 2

#print(3+2) # = 5
#print("3" + "2") # 32
# Для текста + = соединение текста, для цифр и чисел = мат. сложение

#total_attempts = attempts + extra_attempts
#print("Total attempts:", total_attempts)

#total_gb = 100
#used_gb = 72

#free_space = total_gb - used_gb

#print("Free space:", free_space, "Gb")


file_size_mb = 10
file_count = 3
total_size = file_size_mb * file_count
#print("Total size:", total_size, "MB")
# Total size: 30 MB

#print(10 / 2)
# Вывод = 5.0. print(10/2) = print(10 / 2)

#total_gb = 400
#used_gb = 103
#used_percent = (used_gb / total_gb) * 100
#rounded_used_percent_1 = round((used_gb / total_gb) * 100)
#rounded_used_percent_2 = round(used_percent)
#print("Used space:", used_percent, "%")
#print(rounded_used_percent_1)
#print(rounded_used_percent_2)

# Ноль НА число делить можно, Число делить На ноль - нелья
# (.venv) nikitin_n@nikitin-nix:~/Documents/sdet-learning/python-basics$ python hello.py
#Traceback (most recent call last):
#  File "/home/nikitin_n/Documents/sdet-learning/python-basics/hello.py", line 57, in <module>
#    used_percent = (used_gb / total_gb) * 100
#                    ~~~~~~~~^~~~~~~~~~
#ZeroDivisionError: division by zero
#  <module> = строка выполнялась непосредственно в самом запускаемом файле, а не вне файла
#  Traceback (most recent call last) = Тип исключения + пояснение
#    описывает цепочку вызовов, приведшую к этой ошибке. Это не журнал разных ошибок по времени. Если функций было несколько, ниже показываются более поздние вызовы в этой цепочке.
# round = округлить по матану
# int = убрать дробную часть полностью
# убрать дробную часть в выводе - через форматирование текста

#attempts = 3
#limit = 3

#limit_reached = attempts >= limit

#print("Limit reached:", limit_reached)
# Выводит True / False

#total_gb = 100
#used_gb = 72
#min_free_gb = 20

#free_gb = total_gb - used_gb

#low_space = free_gb <= min_free_gb

#print("Free space:", free_gb)
#print("Low space:", low_space)
################################################
#limit_reached = True
#if limit_reached:
#    print("Limit reached") # Если True
#else:
#    print("Attempts available") # Если False
# двоеточие и отступ обозначают начало и содержимое блока
# После esle - двоеточие ОБЯЗАТЕЛЬНО!
# Tab после if / else = 4 пробела
# Отдельного fi - НЕТ

#print("Free space:", free_gb, "GB")

#if free_gb <= min_free_gb:
#    print("Warning: low disk space")
#else:
#    print("Disk space is OK")
#

#total_gb = 100
#used_gb = 79
#min_free_gb = 20

#free_gb = total_gb - used_gb
#low_space = free_gb <= min_free_gb

#print("Free space:", free_gb, "GB")

#if low_space:
#    print("Warning: low disk space")
#else:
#    print("Disk space is OK")

################################################
#failed_attempts = 3
#if failed_attempts >= 5: # Первое условие, если нет - то следующее, elif
#    print("Critical")
#elif failed_attempts >= 1: # Второе, елси нет - то следующее elif / else
#    print("Warning")
#else:
#    print("OK")
#
#total_gb = 100
#used_gb = 101
#critical_free_gb = 10
#min_free_gb = 20

#free_gb = total_gb - used_gb

#print("Total_GB =", total_gb)
#print("Used_GB =", used_gb)
#print("Free space:", free_gb, "GB")

#if free_gb <= critical_free_gb:
#    print("Critical: very low disk space")
#elif critical_free_gb < free_gb <= min_free_gb:
# Тут elif можно сократить до:
# elif free_gb <= min_free_gb:, потому что: программа доходит только тогда
# когда free_gb <= critical_free_gb уже дало False
# Значит, свободное место больше критического порога.
#    print("Warning: low disk space")
#else:
#    print("Disk space is OK")

################################################
#attempts = 3
# and
#if attempts >= 0 and attempts <= 5:
#    print("Valid attempts count")
#else:
#    print("Invalid attempts count")
# Количество попыток не меньше 0 и не больше 5
# Or
#if attempts < 0 or attempts > 5:
#    print("Valid attempts count")
#else:
#    print("Invalid attempts count")
# Количество попыток меньше 0 или больше 5

#total_gb = 100
#used_gb = 79

#free_gb = total_gb - used_gb

#print("Total GB =", total_gb)
#print("Used GB =", used_gb)

#if total_gb <= 0 or used_gb < 0 or used_gb > total_gb:
#    print ("Error: invalid disk data")
#else:
#    print ("Disk data is valid")

#if total_gb > 0 and used_gb >= 0 and used_gb <= total_gb:
#    print("Disk data is valid")
#else:
#    print("Error: invalid disk data")

################################################

#data_is_valid = True
#low_space = False
#if data_is_valid:
#    if low_space:
#        print("Warning")
#    else:
#        print("OK")
#else:
#    print("Invalid data")

#total_gb = 100
#used_gb = 101
#critical_free_gb = 10
#min_free_gb = 20

#print("Total GB =", total_gb)
#print("Used GB =", used_gb)

#if total_gb > 0 and used_gb >= 0 and used_gb <= total_gb:
#    free_gb = total_gb - used_gb
#    print("Free GB:", free_gb)
#    if free_gb <= critical_free_gb:
#        print("Critical: very low disk space")
#    elif free_gb <= min_free_gb:
#        print("Warning: low disk space")
#    else:
#        print("Disk space is OK")
#else:
#     print("Error: invalid disk data")

################################################

#service_state = "running"
#
#if service_state == "running":
#    print("Service is running")
#else:
#    print("Service is not running")
#
# = - присваивает, т.е. задает занчение
# == - сравнение, сранивает значение 1 и знаечние 2
# Сравнение идет полное, как регистр, так и все символы
#print("running" == "running") # True
#print("Running" == "running") # False
#print("running " == "running") # False

#service_state = "error"
#print("Service state =", service_state)

#if service_state == "running" or service_state == "starting":
#    print("Service is running or running")
#elif service_state == "stopped":
#    print("Service is stopped")
#else:
#    print("Unknown service state")

################################################
#service_name = input("Enter service name: ")
#print("Service:", service_name)

# input всегда возвращает строку, вне зависимости от ввода
# Вводишь цифры - 80 - получишь "80", на число 80

#service_state = input("Enter service state: ")
#print("Service state =", service_state)

#if service_state == "running" or service_state == "starting":
#    print("Service is running or running")
#elif service_state == "stopped":
#    print("Service is stopped")
#else:
#    print("Unknown service state")

# int = превращает строку с целым числом в число 
# type = получить ТИП значения

#attempts_text = "3"
#attempts = int(attempts_text)

#print(attempts + 1) # Output = 4

# Ask for number:
#attempts_text = input("Enter attempt count: ") # Первая строка получает текст
#attempts = int(attempts_text) # ВТорая строка преобразует текст -> число

#total_gb = 100
#print("Total GB:", total_gb)

#user_input = input("Enter used space in GB: ")
##print("Input before int", user_input)
##print("Input type:", type(user_input)) # str = строка

#used_gb = int(user_input)
##print("Input After int", used_gb)
##print("Converted type:", type(used_gb)) # int = целое число
#if used_gb >= 0 and used_gb <= total_gb:
#    print("Used GB check is OK")
#    free_gb = total_gb - used_gb
#    print("Free space =", free_gb, "GB")
#else:
#    print("Error: invalid disk data")
#
################################################
# f-строки = удобный способ вставлять значения в текст
#print("Free space =", free_gb, "GB")
# = 
#print(f"Free space: {free_gb} GB")
# f перед "  - включает подстановку значений в строку
# Без f { и } = обычный текст
# В f-строке можно указать формат отображения числа:
# used_percent = 25.75
#print(f"Used space: {used_percent:.1f} %") 
# Output = Used space: 25.8 %
# : - начало указание формата
# 1f = формат = 25.8
# 0f = формат = 26
# Меняется только текст, переменная - не изменяется

#total_gb = 100
#print(f"Total GB: {total_gb}")
#
#user_input = input("Enter used space in GB: ")
#
#used_gb = int(user_input)
#if used_gb >= 0 and used_gb <= total_gb:
#    print("Used GB check is OK")
#    free_gb = total_gb - used_gb
#    print(f"Free space = {free_gb} GB")
#else:
#    print("Error: invalid disk data")
#
#total_gb = 400
#print(f"Total GB: {total_gb}")

#user_input = input("Enter used space in GB: ")

#used_gb = int(user_input)
#if used_gb >= 0 and used_gb <= total_gb:
#    print("Used GB check is OK")
#    free_gb = total_gb - used_gb
#    print(f"Free space = {free_gb} GB")
#    used_percent = used_gb / total_gb * 100
#    print(f"Used space: {used_percent:.1f} %")
#    print(f"Used space rounded: {used_percent:.0f} %")
#
#    print("Value after formatting:", used_percent)

#else:
#    print("Error: invalid disk data")

################################################
# коллекции
################################################
# List
#
# service_states = ["running", "starting", "stopped"]
# [...] обозначает список;
# элементы разделены запятыми;
# порядок элементов сохраняется;
# каждый элемент в этом примере — строка.
# Чтобы получить отдельный элемент, после имени списка указывают его индекс
# в квадратных скобках. Индексы начинаются с нуля:
# 0 = "running"
# 1 = "starting"
# 2 = "stopped"
# print(service_states[0]) = running
# Количество элементов можно получить через встроенную функцию len:
# state_count = len(service_states)
# print("State count:", state_count)
# Output = State count: 3


# service_names.append("cron") = Добавить в список
# service_names - куда добавить
# . (точка) = связывает действие со списком
# append = сетод списка = добавить 1 элемент в КОНЕЦ списка
# cron = что добавляем
# Метод — Метод — это операция, которую вызывают у конкретного объекта через точку. Подробнее разберём это при изучении ООП
# append - изменяет сам список - вызывается отдельной строкой

# service_names.append("cron") -> ["kldfs", "sssd", "rsyslog", "cron"]

#service_names = ["kldfs", "sssd", "rsyslog"]
#print("Second service:", service_names[1])
#state_count = len(service_names)
#print("Service count:", state_count)

#service_names = ["kldfs", "sssd", "rsyslog"]
#service_names.append("cron")
#print("Fourth service:", service_names[3])
#state_count = len(service_names)
#print("Service count:", state_count)
################################################
# Циклы
#
#
#service_names = ["sssd", "rsyslog", "NetworkManager"]
#failed_services = []

#for service_name in service_names: # поочереди взять каждый элемент списка и присовить переменной
# service_name и выполнить блок с отступом (следующий). Аналогично for в Bash
#    service_state = input(f"State of {service_name}: ") # в данном примере блок выполнится 3 раза
#    if service_state == "stopped": # sssd rsyslog NetworkManager
#        failed_services.append(service_name)

#print("Failed services:", failed_services)
#print("Failed count:", len(failed_services))
# Пример выполнения:
#State of sssd: running
#State of rsyslog: stopped
#State of NetworkManager: running
#Failed services: ['rsyslog']
#Failure count: 1

#service_names = ["sssd", "rsyslog", "NetworkManager"]

#for service_name in service_names: # Для каждого элемента из service_names 
#выполнить следующий блок
#    print(f"Service: {service_name}") 
# на каждом проходе переменная servive_name -получает НОВОЕ очередное значение
# Имя ervice_name - выбираем сами
#print("Done")
# Единственное число = текущий элемент
# Множественное число = весь список

# Пример выполнения:
#Service: sssd
#Service: rsyslog
#Service: NetworkManager
#Done

# Исходные данные:
#service_names = ["sssd", "rsyslog", "NetworkManager"]
# service_names = []
# Если в service_names будет ПУСТО, 0 значений, то:
# цикл НЕ запустится, так как нет элементов для его запуска, "не по чему проходиться"
# НЕТ цикла = НЕТ ничего что чть в цикле - запрсов input, print и прочего
# ВСЕ 3 списка окажутся ПУСТЫМИ
# ВСЁ что ВНЕ цикла - выполнится
#running_services = []
#stopped_services = []
#unknown_services = []

#for service_name in service_names:
#    print(f"Service: {service_name}")
#    user_input = input("Enter service status: ")
#    if user_input == "running":
#       running_services.append(service_name)
#    elif user_input == "stopped":
#        stopped_services.append(service_name)
#    else:
#        unknown_services.append(service_name)
#        print("Custom service status")

#running_count = len(running_services)
#stopped_count = len(stopped_services)
#unknown_count = len(unknown_services)

#print("Running count:", running_count)
#print("Running services", running_services)

#print("Stopped count:", stopped_count)
#print("Stopped services", stopped_services)


#print("Unknown count:", unknown_count)
#print("Unknown services:", unknown_services)


#print("Done")

################################################
# Dict | dict | Словари
# Словари хранят соотвествия |Ключ - Значение|
#service_states = {
#    "sssd": "running",
#    "rsyslog": "stopped",
#}
# sssd = ключ | runnig = Значение
# rsyslog = ключ | stopped = Значение
# {...} = Словарь
# : (двоеточие) = разделитель между К и З
# , (запятая) = разделитель пар К-З
# Каждый ключ = УНИКАЛЕН
# Повторная запись по тому же Ключу = ОБНОВИТ Значение
#service_names = ["sssd", "rsyslog", "sssd"] = 2 ключа, НЕ 3, так как ssd = повторка

#print(service_states["sssd"]) # Получить Значение по Ключу sssd
# Вывод:
# running
# ВЫВЕССТИ ВЕСЬ СЛОВАРЬ
#print(service_states)
#
# РАЗНИЦА СО СПИСКОМ:
# В Списке = обращаются по ПОЗИЦИИ
# В Словаре = по ИМЕНИ
#
# ДОБАВИТЬ НОВУЮ ПАРУ
#service_states["NetworkManager"] = "dead"
# В_какой_СЛОВАРЬ_добавить[Ключ] = "Значение"
#
# ЗАМЕНИТЬ СУЩЕСТВУЮЩЕЕ ЗНАЧЕНИЕ НО НОВОЕ
#service_states["rsyslog"] = "running"
# В_каком СЛОВАРЕ_Меняем[Какой_КЛЮЧ_Меняем] = "Новое_Значение"

# Исходные данные
#service_names = ["sssd", "rsyslog", "NetworkManager"]
#service_states = {} # Пустой Словарь
#
#for service_name in service_names:
#    print(f"Service name: {service_name}")
##    print("Current state for", service_name, "is:", service_states[service_name])
#    if service_name in service_states: # Есть ли такой ключ в словаре или нет
#      print("Curent state:", service_states [service_name]) # Ключ есть - вывести какой
#    else:
#        print("No saved state") # ключа нет
#    user_input = input("Enter service status: ")
#    service_states[service_name] = user_input # Задать новое значение сервису из service_states
#    print("New state for", service_name, "is:", service_states[service_name])
#
#print(service_states)
#services_count = len(service_states)
#print("Services count:", services_count)

# ПЕРЕБОР СЛОВАРЯ
# = Обработка жанных после бсора без нового ввода
# 
#for service_name in service_states:
#    print(service_name) # Получает Ключи словаря ПООЧЕРЕДИ - имена сервисов
# Получить Значение Ключа:
#service_state = service_states[service_name]
#
# Пример:
#
#service_states = {
#    "sssd": "running",
#    "rsyslog": "stopped",
#}
#
#for service_name in service_states:
#    service_state = service_state[service_name]
#    print(f"{service_name}: {service_state}")
#
# Вывод:
# sssd: running
# rsyslog: stopped
#
# Исходные данные:
#service_states = {
#    "sssd": "running",
#    "rsyslog": "stopped",
#    "NetworkManager": "dead",
#}
#stopped_service = []
#
#for service_name in service_states:
#    service_state = service_states[service_name]
##    print("Current states are:")
#    print(f"{service_name}: {service_state}")
#    if service_state == "stopped":
#        stopped_service.append(service_name)
#    #print("Current service is:", service_name)
#    #print("Current service is:", service_name)
#
#stopped_service_count = len(stopped_service)
#print("Stopped services:", stopped_service)
#print("Stopped count:", stopped_service_count)


################################################
# ОБЩИЕ ПРОМЕЖУТОЧНЕЫ ЗАДАЧИ
# 1)
def control_first_task():
    # Исходные данные:
    service_names = ["sssd", "rsyslog", "NetworkManager"]

    for service_name in service_names:
        print("Service:", service_name)
    service_count = len(service_names)
    print("Total services:", service_count)

#control_first_task()
# 2)
def control_second_task():
    # Исходные данные:
    service_names = ["sssd", "rsyslog", "NetworkManager"]
    # OR
    service_names = ["rsyslog", "sssd", "rsyslog", "NetworkManager"]
    # OR
    #service_names = ["sssd", "NetworkManager"]
    matched_services = []

    for service_name in service_names:
        if service_name == "rsyslog":
    #        matched = matched_services.append(service_name) # НЕпраивльно
            matched_services.append(service_name) # ПРАВИЛЬНО
    #        print("Service:", service_name)

    #service_count = len(service_names)
    #print("Total services", service_count)

    print("Matched services:", matched_services)
    matched_count = len(matched_services)
    print("Matched count:", matched_count)

#control_second_task()

# 3)
# Исходные данные:
def control_third_task():
    free_space_values = [28, 20, 9, 35]
    free_space_values = [0, 20, 21]
    low_space_values = []
    matched_values = []

    for free_space_value in free_space_values:
        if free_space_value <= 20:
            matched_values.append(free_space_value)

    print("Low space caluse:", matched_values)
    matched_count = len(matched_values)
    print("Low space count:", matched_count)


#control_third_task()

# 4)
# Исходные данные:
def control_fourth_task():
    free_space_values = [28, 20, 9, 35]
    free_space_values = [20, 20, 21]
    low_space_values = []
    normal_space_values = []

    for free_space_value in free_space_values:
        if free_space_value <= 20:
            low_space_values.append(free_space_value)
        else:
            normal_space_values.append(free_space_value)

    low_space_count = len(low_space_values)
    normal_space_count = len(normal_space_values)

    print("Low space values:", low_space_values)
    print("Low space count:", low_space_count)

    print("Normal space values", normal_space_values)
    print("Normal space count:", normal_space_count)

#control_fourth_task()

# 5)
# Исходные данные:
def control_slovar_1_task():
    disk_free_space = {
    "/": 28,
    "/home": 9, # home = Ключ
    "/var": 35, # 35 = Значение
    }

    def example():
        print("Home free space:", disk_free_space["/home"], "GB")
        # Output:
        # Home free space: 9 GB
    #example()

    print("/var free space:", disk_free_space["/var"], "GB")
    slovar_count = len(disk_free_space)

    print("/ free space", disk_free_space["/"], "GB")

    print("Disk count:", slovar_count)


#control_slovar_1_task()

# 6)
def control_slovar_2_task():
    disk_free_space = {
    "/": 28,
    "/home": 9, # home = Ключ
    "/var": 35, # 35 = Значение
    }

    def example():
        disk_path = "/home" # читает значение disk_path - строку "/home"
        free_gb = disk_free_space[disk_path] # Ищет этот ключ в disk_free_space
        # Присваивает найденной значение (9) переменной free_gb
        print("Free space:", free_gb, "GB")
    
    #example()

    disk_path = "/"
    free_gb = disk_free_space[disk_path]
    print(f"{disk_path}: {free_gb} GB")

#control_slovar_2_task()

# 7)
def control_slovar_for():
    disk_free_space = {
    "/": 28,
    "/home": 9, # home = Ключ
    "/var": 35, # 35 = Значение
    }

    for disk_path in disk_free_space: # На каждом проходе disk_path получает очережной ключ
        free_gb = disk_free_space[disk_path] # а disk_free_space[disk_path] - соотвествующее число
        print(f"{disk_path}: {free_gb} GB")

#control_slovar_for()

# 8)
def control_slovar_for_2():
    disk_free_space = {
    "/": 28,
    "/home": 9, # home = Ключ
    "/var": 20, # 35 = Значение
    }

    for disk_path in disk_free_space: # На каждом проходе disk_path получает очережной ключ
        free_gb = disk_free_space[disk_path] # а disk_free_space[disk_path] - соотвествующее число
        if free_gb <= 20:
            print(f"{disk_path}: {free_gb} GB")

#control_slovar_for_2()

# 9)
def control_slovar_for_spisok():
    disk_free_space = {
    "/": 28,
    "/home": 9, # home = Ключ
    "/var": 20, # 35 = Значение
    }

    low_space_disks = []

    for disk_path in disk_free_space:
        free_gb = disk_free_space[disk_path] # записываем в low_space_disks пути дисков
        if free_gb <= 20: # если свободно менее 20, то:
            low_space_disks.append(disk_path) # добавить путь диска в low_space_disks

    disks_count = len(low_space_disks) # Посчитать сколько дисков получилось

    print("Low space disks", low_space_disks) # вывести пути дисков из low_space_disks
    print("Low space count:", disks_count) # вывести сколько таких дисков

#control_slovar_for_spisok()

# 10) 
def services_statusess():
    service_states = {
    "sssd": "running",
    "rsyslog": "stopped",
    "NetworkManager": "stopped",
    "cron": "running",
    }
    stopped_services = []

    for service_name in service_states:
        service_status = service_states[service_name]
        if service_status == "stopped":
            stopped_services.append(service_name)
    
    service_count = len(stopped_services)

    print("Stopped services:", stopped_services)
    print("Stopped count:", service_count)

#services_statusess()

# 11)
def change_slovar():
    service_states = {
    "sssd": "running",
    "rsyslog": "stopped",
    "NetworkManager": "stopped",
    "cron": "running",
    }
    stopped_services = []

    def stopped_check():
        for service_name in service_states:
            service_status = service_states[service_name]
            if service_status == "stopped":
                stopped_services.append(service_name)

    def exapmple():
        service_states["sssd"] = "stopped" # Если ключ существует - его значение меняется
        # Если ключ новый - добавляется новая запись
        print(service_states) # Вывести весь список

    service_count_all = len(service_states)
    print("Services count before adding new:", service_count_all)
    print("Adding SSH")
    service_states["ssh"] = "running"
    service_count_all = len(service_states)
    print("Services count after adding new:", service_count_all)



    print("Check stopped before changing rsyslog")
    stopped_check()
    print("Stopped services:", stopped_services)

    stopped_services = [] # Удаление накопления и результатов предыдущих проверок !
    service_states["rsyslog"] = "running"  
     
    print("Check stopped after changeing rsyslog")
    stopped_check()
    print("Stopped services:", stopped_services)
    
    stopped_count = len(stopped_services)
    service_count_all = len(service_states)

    print("Stopped services:", stopped_services)
    print("Stopped count", stopped_count)
    print("Total count:", service_count_all)

#change_slovar()

################################################
# ФУНКЦИИ
# Функция — именованный блок кода, который можно запускать по имени. Она помогает один раз описать действие и затем выполнять его несколько раз.
def show_service(service_name): # Определение функции
# Def = ключ определния функции
# show_service = Имя Функции
# service_name (в скобках) = параметр, через которые функции получает данные
# : (двоеточие) = начала блока кода функции
    print(f"Service: {service_name}") # тело функции, то что делает фнукция
# ОТСТУПЫ = показывают, что команды относятся к телу функции (4 пробелы / 1 Таб)
# ОТСТУПЫ = определяет границы блоки, принадлежность команд к чем-либо
# Само определение не запускает тело функции
# Если оставить только эти две строки, сообщения Service: ... не будет. Python запомнит функцию, чтобы её можно было вызвать дальше.

# show_service("sssd") # обращаемся к функции по имени и передаём ей значение "sssd"
# при таком вызове:
# * Параметр service_name получает значение "sssd".
# * Выполняется тело функции.
# * F-строка подставляет это значение, и print выводит Service: sssd.
# * После завершения функции выполнение продолжается со следующей строки после вызова.
# show_service("cron") # обращаемся к функции по имени и передаём ей значение "cron"
# запускает ту же функцию ещё раз, теперь со значением "cron". Поэтому весь пример выводит:

################################################
# # ПАРАМЕТРЫ И АРГУМЕНТЫ
#
# Имя = show_free_space = Имя для входных данных внутри функции
# Параметр = (free_gb) в скобках = Конкретное значение, которое передали
# Аргумент = 15 = Значение, переданное при вызове функции

# Func_Test_1
def show_free_space(free_gb):
    print("Free space:", free_gb, "GB")

#show_free_space(28)
#show_free_space(9)

# Example
def show_free_space_E(free_gb):
    print("Free space:", free_gb, "GB")

# space = 15
# show_free_space_E(space)
# show_free_space_E(0)

# Вывод:
# Free space: 15 GB
# Free space: 0 GB

# Func_Test_2

def show_free_space(free_gb):
    print("Free space:", free_gb, "GB")
    if free_gb < 10:
        print("Warning: low disk space")

# test = show_free_space(28)
# print(test)
# show_free_space(28)
# print(show_free_space(28))
# show_free_space(28)
# show_free_space(9)
# show_free_space(10)

# # RETURN | return - как получить результат из функции, чтобы дальше использовать его в программе
# return возвращает значение в место вызова и завершает текущий вызов функции
# print выводит данные на экран

def double(number): # Вызов цункции double (6) - парметр number получает значение 6
    return number * 2 # Вычиление 6 * 2
#   return возвращает число 12

result = double(6) # Оно (12) записываеится в переменную result
# print(result) # Вывести на кэран результат = 12

# Сама функция здесь ничего не печатает. Если убрать последнюю строку, вычисление и присваивание произойдут, но при запуске файла вывода не будет

# Func_Test_return
def calculate_free_space(total_gb, used_gb):
    return total_gb - used_gb

result = calculate_free_space(100, 72)
#print(result)

#print(calculate_free_space(100, 72)) # Использовать перменную НЕ обязательно - можно сразу
# НО ТОЛЬКО ЕСЛИ ЕСТЬ return !

# Здесь программа использует возвращённое число в условии
# return завершает вызов текущей функции 
# БЕЗ result функция не возвращает вычисленное число наружу.

# Вывести результат в нужный момент = одна из возможностей
# Но главное: return позволяет дальше использовать вычисленное значение, а не только увидеть его на экране

# ПРИМЕР:
def calculate_free_space_e1(total_gb, used_gb):
    print("Calculating")
    return total_gb - used_gb

# test = calculate_free_space_e1(100, 72)
# print(test) # Функция повторно не запускается !
# print(calculate_free_space(100, 72))
# Вывод:
# Calculating = печается внутренним print
# 28 = то что было записано в return
# 28 = второй вывод print(calculate_free_space(100, 72))
# print(calculate_free_space(100, 72)) = test = calculate_free_space_e1(100, 72) + print(test), НО! ТОЛЬКО ЕСЛИ ЕСТЬ return!

# Func_Test_return_2
def is_service_running(status):
    if status == "running":
        return True
    else:
        return False

# print("1st run with RUNNING:", is_service_running("running")) # Значение в виде текста / слова = перадается в кавычках. БЕЗ кавычек - передать параменную
# print("2nd run with STOPPED:", is_service_running("stopped"))

# running = is_service_running("running")
# if running:
#    print("Service is running")
# else:
#    print("Service is not running")

#rint(is_service_running(running))
# print(running)

# Func_Test_return_3

def calculate_used_percent_1(total_gb, used_gb):
    print("Here will be Result + None")
    used_percent = used_gb / total_gb * 100
    print(used_percent)

#print(calculate_used_percent_1(200, 50))

devide = "---------------------"
#print(devide)

def calculate_used_percent_2(total_gb, used_gb):
#    print("Here will be result w/o None")
#    used_percent = used_gb / total_gb * 100
#    return used_percent
    return used_gb / total_gb * 100

#used_percent = calculate_used_percent_2(200, 50)
#print("%:", used_percent)


#print(calculate_used_percent_2(200, 50))

#print(devide)

# Func_Test_return_4
def get_disk_status(total_gb, used_gb):
    free_gb = total_gb - used_gb
    if free_gb < 0:
        return "invalid"
    elif free_gb < 10:
        return "critical"
    elif free_gb < 30:
        return "warning"
    else:
        return "ok"

#print("100 - 110 - Your disk status is:", get_disk_status(100, 110))
#print("100 - 100 - Your disk status is:", get_disk_status(100, 100))
#print("100 - 91 - Your disk status is:", get_disk_status(100, 91))
#print("100 - 90 - Your disk status is:", get_disk_status(100, 90))
#print("100 - 71 - Your disk status is:", get_disk_status(100, 71))
#print("100 - 70 - Your disk status is:", get_disk_status(100, 70))

################################################
# ЛОКАЛЬНЫЕ ПЕРЕМЕННЫЕ
# ПРИМЕР
# Перменные ВНТУРИ функции НЕ видны снаржу функции по умолчанию
# В общем коде и внутри функции могут быть пеерменные с одлинаковым именем и они могут иметь РАЗНЫЕ значения
def calculate_used_percent_2(total_gb, used_gb):
    used_percent = used_gb / total_gb * 100
    return used_percent # return передает Значение НАРУЖУ, НО не саму переменную (НЕ ее имя) !
    # Снаружи - это значение под именем result !
    # total_gb, used_gb, used_percent = локальные перменные функции. Использвются ТОЛКО внутри фнукции !

# result = calculate_used_percent_2(200, 50)
#print(result)

# Func_Local_Func
def calculate_used_percent_3(total_gb, used_gb):
    used_percent = used_gb / total_gb * 100
    return used_percent

#result = calculate_used_percent_3(200, 50)
#print(used_percent) = Error  - NameError: name 'used_percent' is not defined

################################################
# FINAL FUNC COMBO
# Исходыне данные:
#@snoop
service_states = {
    "sssd": "running",
    "NetworkManager": "stopped",
    "cron": "running",
    "ssh": "stopped",
}

#@snoop
def get_stopped_services(service_states):
    stopped_services = []
    for service_name in service_states:
        status = service_states[service_name]
        if status == "stopped":
            stopped_services.append(service_name)
    return stopped_services


#print(get_stopped_services(service_states))
#result = get_stopped_services(service_states)
#print(result)
#count = len(result)
#print(count)

# FINAL FUNC COMBO 2
# Исходыне данные:
free_space = {
    "/": 18,
    "/var": 6,
    "/home": 42,
    "/boot": 2,
    "/data": 10,
}

def get_low_space_mounts(free_space):
    spisok = []
    for mount_point in free_space:
        size = free_space[mount_point]
        if size < 10:
            spisok.append(mount_point)
    return spisok

#print(get_low_space_mounts(free_space))

# FINAL FUNC COMBO 3
# Исходыне данные:
before = {
    "curl": "8.5.0",
    "git": "2.43.0",
    "sssd": "2.9.4",
    "rsync": "3.2.7",
}

after = {
    "curl": "8.5.1",
    "git": "2.43.0",
    "sssd": "2.9.5",
    "rsync": "3.2.7",
}

old_version = ""
new_version = ""

def get_changed_packages(before, after):
    changed = []
    for names in before:
        old_version = before [names]
        new_version = after [names]
        if old_version != new_version:
            changed.append(names)
    return changed

# changed = get_changed_packages(before, after)
# print(changed)

# MEMORY - списки, словари

# Список = квадратные скобки, значения через запятыую, без других символов ["curl", "git"]
# [одно, другое]
# Добавить:
# ИмяСписка.append("Значение")
#
# Изменить значение:
# ИмяСписка[Номер] = "Значение"

# Словарь = фигурные скобки, значения с двоеточиями {"curl": "8.5.0"} парами
# {имя: значение}
# Добавить / изменить значение:
# ИмяСписка["Ключ"] = "значение"

def spisok():
    packages = ["curl", "git"] # изначальный список
    packages[0] = "wget" # заменить ПЕРВЫЕ элемент списка на wget
    print(packages) # вывести список всех = ['wget', 'git']

def slovar():
    versions = {"curl": "8.5.0", "git": "2.43.0"}
    print(versions)
    versions["git"] = "2.44.0"
    versions["rsync"] = "3.2.7"
    print(versions)
    print(len(versions))

#slovar()

def combined():
    devide = "---------------------------------------"
    service_names = []
    print(service_names)
    service_names.append("sssd") # Добавить в спиок sssd
    service_names.append("cron") # Добавить в список cron

    print(service_names) # Вывести содержимое ВСЕГО списка
    print(len(service_names)) # Вывести длину, кол-ва элементов в списке

    print(service_names[1]) # вывести второй элемент списка

    print(devide)
################################################
    service_states = {}
    print(service_states) 
    service_states["sssd"] = "running" # Добавить в словарь sssd со значением running
    service_states["cron"] = "stopped" # Добавить в словарь cron со значением stopped
    print(service_states) # вывести весь словарь
    print(len(service_states)) # вывести длину, кол-вао элементов в словаре
    print(service_states["cron"]) # вывести зачение (статус) ТОЛЬКО одного элемента из словаря - cron
################################################
    name = service_names[1] # записать в перменную name - ВТОРОЙ элемент из списка service_names
#   print(service_states[name]) # Из словваря service_states - взять элемент = name (cron) и вывести его значение
    # Словарь -> имя -> значение = print(service_states["cron"]) -> stopped
################################################
    for name in service_names: # Цикл - для КАЖДОГО значения из списка service_names
        print(name, service_states[name]) # вывести ИМЯ СТАТУС
# Т.е. пройтись по всему списку, и для КАЖДОГО значения в списке выполнить команду нижу, в которой:
# name = значение списка, service_states[cron] и так далее
# Вывод:
# sssd running
# cron stopped
################################################
    print(devide)
    for name in service_states:
#        print(name)
        print(name, service_states[name])
################################################
    print(devide)
    stopped_services = []
    service_states["sssd"] = "stopped"
    for name in service_states:
#        print(name)
        status = service_states[name]
#        print(status)
        if status == "stopped":
            print("Stopped service is:", name)
            stopped_services.append(name)
    print(stopped_services)
################################################
    print(devide)
    print ("values")
    name = "cron"
    if name in service_states: # Если имя сервиса name есть в service_states
        print(service_states[name]) # True = выведи на экран его статус
    else: # False = Если нет
        print("Unknown service") # выведи текст
################################################
    print(devide)
    print("requested")
    unknown_services = []
#    requested = ["cron", "ssh", "nginx"] # заданный список
    requested = ["cron", "ssh", "nginx", "ssh"]
    for name in requested: # По очереди брать каждое имя из списка requested
        if name in service_states: # Если ДА, то - # Проверить, есть ли это имя среди ключей словаря, и если ДА, то:
            print(name, service_states[name]) # выведи Имя_Сервиса Статус_Сервиса
        else: # Если НЕТ, то:
            #print(name, "Unknown service") # выведи текст
            if name not in unknown_services: # Если элемента НЕТ в списке unknown_services - то добавить его. Если ЕСТЬ - ничего не делать. Избавляет от повторов
                unknown_services.append(name)
    print(unknown_services)

    print(devide)


#combined()

# IN |in = прверка наличия в списке / словаре
# Исходные данные
def IN_example():
    service_states = {"sssd": "stopped","cron": "stopped"} # словарь
    stopped_services = ["sssd", "cron"] # список

# NOT IN | not in = прверка наличия в списке / словаре

    print("cron" in stopped_services) # Проверить ЕСТЬ ЛИ значение cron в stopped_services и вывести на экран
# Вывод = True
    print("stopped" in service_states) # Проверить ЕСТЬ ЛИ значение stopped в service_states и вывести на экран
# Вывод = False
# Проверка выдает False т.к. ищется по ключам, а ключи = sssd и cron = False. НЕ по значениям!

# .values() = ЗНАЧЕНИЯ в словаре
    print("cron" in service_states)
    print("cron" in service_states.values())

# TASK_1
# Входные данные:
#requested = ["cron", "ssh", "nginx", "ssh"]
requested = ["cron", "ssh", "cron"]

service_states = {
    "sssd": "stopped",
    "cron": "stopped",
}


def get_unknown_services(requested, service_states):
    unknown_services = [] # СОздали пустой спислк
    for name in requested: # Для каждого объекта в списке requested, выполнить:
        if name not in unknown_services: # Если объект НЕ находится в списке unknown_services, то:
            if name not in service_states: # и при этом, если объект НЕ находится в словаре service_states, то:
                unknown_services.append(name) # Добавь этот объект в список unknown_services
    #return(unknown_services) # выведи во вне содержание списка unknown_services

    result = {}
    for name in requested: # Пройтись по всем объектам requested
        if name in service_states: # Если указанный объект есть в словаре service_states:
            existing_status = service_states[name] # записать статус этого объекта в переменную existing_status
            result[name] = existing_status # Записать объект и его статус в словарь result
        else:
            result[name] = "unknown" # Если объекта не было в словаре service_states - то записать этот объект со статусом unkown в словарь result
    print(result)


#get_unknown_services(requested, service_states)
#print(get_unknown_services(requested, service_states))
#first = get_unknown_services(requested, service_states)
#second = get_unknown_services(["cron", "sssd"], service_states)

#print(first)
#print(second)

# TASK_2
# Входные данные:
requested = ["cron", "ssh", "cron"]
service_states = {"sssd": "running", "cron": "stopped"}

def get_service_statuses(requested, service_states):
    result = {}
    for name in requested: # Пройтись по всем объектам requested
        if name in service_states: # Если указанный объект есть в словаре service_states:
            existing_status = service_states[name] # записать статус этого объекта в переменную existing_status
            result[name] = existing_status # Записать статус (ключ) объекта по его имени (name) словарь result
        else:
            result[name] = "unknown" # Если объекта не было в словаре service_states - то записать этот объект со статусом unkown в словарь result
    return(result)

#statuses = get_service_statuses(["cron"], service_states)
#statuses = {"cron": "stopped"}
#print(statuses)
#assert statuses == {"cron": "stopped"}
#assert statuses["cron"] == "stopped"
#statuses = {"cron": "stopped"}
#assert statuses == {"cron": "stopped"}
#assert statuses["cron"] == "stopped"

#get_service_statuses(requested, service_states)
#get_service_statuses([], service_states)
#print(get_service_statuses(requested, service_states))
#print(get_service_statuses([], service_states))

#statuses = get_service_statuses(requested, service_states)

#print(statuses["ssh"])
#print(statuses["cron"])

################################################
# ASSERT | assert = проверка в коде
# assert нужен, чтобы коротко записать, какой результат ты считаешь правильным, и получить ошибку, если результат другой.
# Читается так: «Я ожидаю, что это условие истинно. Если оно ложно — остановись здесь и сообщи об ошибке»
statuses = {"cron": "stopped", "ssh": "unknown"}

def assert_expplain():
    assert statuses["cron"] == "stopped" # == - это как ДОЛЖНО быть, что я ОЖИДАЮ от кода, т.е. cron  ДОЛЖЕН быть = stopped
# Принцип: assert Берёт statuses["cron"] и получает строку "stopped" ->
# -> Вычисляет "stopped" == "stopped" и получает True ->
# -> assert видит True = проверка ПРОШЛА, Python переходит к СЛЕДУЮЩЕЙ строке и выполняет её
    print("Проверка пройдена") # Поэтому на экране появится Проверка пройдена — это сообщение напечатал print
    assert statuses["ssh"] == "running"
# Это пример с ошибкой, ВЫВОД:
#Traceback (most recent call last):
#  File "/home/nikitin_n/Documents/sdet-learning/python-basics/hello.py", line 1291, in <module>
#    assert_expplain()
#  File "/home/nikitin_n/Documents/sdet-learning/python-basics/hello.py", line 1288, in assert_expplain
#    assert statuses["ssh"] == "running"
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#AssertionError
#
# Как это читается:
# читать снизу вверх: AssertionError — какая ошибка возникла, строка 1288 — какая проверка её вызвала, строка 1291 — откуда была вызвана функция assert_expplain().
# 
    print("Дошли до print")

#assert_expplain()

#
#
#
#
# statuses = {"cron": "stopped", "ssh": "running"}
# assert statuses["ssh"] == "running"


################################################
# IMPORT | import
# import нужен, чтобы использовать в своём скрипте код из модуля.
# Модуль — это именованная часть Python с готовыми инструментами
# json умеет работать с форматом JSON
# pathlib — с путями к файлам и каталогам
# Оба модуля входят в стандартную библиотеку Python: устанавливать их через pip не нужно

# import pathlib = делает доступным имя pathlib и дает возможность создавать каталоги и использовать:
# pathlib.Path("reports").mkdir(exist_ok=True)
# Через . (точку) идет обращение к Path внутри модуля
# from pathlib import Path = «из pathlib возьми Path» -> Теперь в скрипте доступно имя Path ->
# -> после чего можно писать Path напрямую 
# «из pathlib возьми Path, чтобы дальше в этом файле можно было писать Path»

# import json
# «Загрузи модуль с именем json и сделай имя json доступным в моём скрипте»

################################################
# Создание Файлов, папок, запись текста в файлы

# СОЗДАНИЕ папки
from pathlib import Path

def create_dir_example ():
    Path("reports").mkdir(exist_ok=True)
# Path("reports") задаёт путь относительно текущего каталога
# mkdir() создаёт каталог
# exist_ok=True позволяет повторно запускать скрипт, когда каталог уже есть

# ЗАПИСАТЬ текст в файл 
def wrie_file_example_1():
    with open("reports/services.txt", "w", encoding="utf-8") as file:
        file.write("sssd running\n")
# open = откроет файл services.txt в текущей папке
# "w" - режим - создает файл, если файл уже есть - осищает его
# as file = дает открытому файлу имя file
# file.write(...) - записывает текст
# \n перевед строки на след строку
# когда блок with заканчивается - файл закрывается

def wrie_file_example_1():
    with open("reports/services.txt", "a", encoding="utf-8") as file:
        file.write("cron stopped\n")

# ПРОЧИТАТЬ текст из файла
def read_file_example(): 
    with open("reports/services.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print(text)


################################################
# JSON
# JSON — это способ записать данные обычным текстом по определённым правилам
# {} обозначают объект — так в JSON называется набор пар «ключ — значение» ->
# -> {"cron": "stopped"} ->
# -> имени "cron" соответствует значение "stopped"

# 1  Создать файл и записать в него данные
import json
service_states = {"cron": "stopped"}
def json_write_expample():
    with open("reports/services.json", "w") as file: 
        json.dump(service_states, file) # записывает данные.
# json.dump(что_записать, куда_записать)

#open("reports/services.json", "w") создаёт файл, если его ещё нет. Если файл уже есть, режим "w" очищает его. Пока открыт блок with, имя file обозначает этот открытый файл.

# 2 Открыть файл и прочтитать данные

def json_read_expample():
    with open("reports/services.json", "r") as file: # open(..., "r") открывает существующий файл для чтения
        loaded_states = json.load(file)
# куда записать (пременная) = прочитать файл

    print(loaded_states["cron"])

# УПРАЖНЕНИЯ
# 1)

file_before = "reports/services.json"
file_after = "reports/services_updated.json"
data = {'sssd': 'running', 'cron': 'stopped'}

def json_read_ex1():
    with open(my_json, "r") as file:
        text = json.load(file)
    
    status = text["sssd"]
    print(status)

#json_read_ex1()

# 2)
def json_read_ex2():
    with open (file_before, "r") as file:
        text = json.load(file)
        status = text
    print("Curent status:", status)
####################################
    text["cron"] = "running"
    print("New status:", text)

    with open (file_after, "w") as file:
        json.dump(text, file)

    with open (file_after, "r") as file:
        new_status = json.load(file)
        print("File after json: ", new_status)

    print("New status: ", new_status["cron"])
    check = new_status["cron"]
    assert check == "running"


json_read_ex2()
################################################

# GIT
# Репозиторий — каталог проекта, для которого Git может вести историю. Сама история хранится в скрытом подкаталоге .git.
# Коммит — сохранённая версия выбранных файлов с твоим коротким комментарием. Например: «Добавил чтение и запись JSON». Когда ты сохраняешь hello.py в VS Code, меняется файл на диске. Коммит появится только тогда, когда ты отдельно попросишь Git сохранить эту версию в истории.

# проверить, есть ли репозиторий
# git rev-parse --show-toplevel

# СОЗДАТЬ репозиторий
# git init -b main
# init означает «создать здесь репозиторий»
# -b main задаёт имя начальной ветки — линии истории, куда позже попадёт первый коммит

# git add -- hello.py
# git add берёт текущее содержимое hello.py и готовит его к коммиту.
# -- обозначает конец параметров команды, дальше идёт имя файла.
# git status --short
# покажет результат
# Вывод:
# A  hello.py # А = файл подготовлен к добавлению в историю
# ?? .venv/ # файлы с ?? не отслеживаются и в этот коммит не попадут
# ?? reports/
# ?? services.txt

# СОХРАНИТЬ подготовленную версию в ЛОКАЛЬНОЙ истории:

# git commit -m "Добавил упражнения по Python и работе с JSON"
# commit сохраняет то, что ты подготовил через git add
# -m задаёт короткое описание версии, чтобы потом её можно было узнать в истории.
# root-commit — это первый коммит репозитория
# 1 file changed, 1453 insertions(+) означает, что Git впервые записал в историю весь файл — 1453 строки.

# ПОСМОТРИТЬ ИСТОРИЮ ПРОЕКТА
# git log -1 --oneline
# -1 означает «показать последний коммит»
# --oneline — «в одну строку»

# Вывод:
# e79311f (HEAD -> main) Добавил упражнения по Python и работе с JSON

# ПОКАЗАТЬ ИЗМЕНЕНИЯ

# git diff -- hello.py
# строка с - — прежний вариант
# строка с + — новый

# ВЫЙТИ = строчная q

# ПОСМОТРЕТЬ что попоадет в следующий коммит:
# git add -- hello.py # подготовит все текущие правки в hello.py
# git diff --cached -- hello.py # покажет подготовленные изменения.
# --cached здесь означает «покажи то, что уже отобрано для следующего коммита»

