#Вступ та опис гри
print ('''Ласкаво просимо в нашу гру: \n    "Неїбічний лицар"!\n В цій міні квест-грі вам доведеться стати перед важким вибором,
який зробив би хоробрий лицарю.''')
print (' Ви, здоровий неїбічний лицар,\nякий вирушив на порятунок принцеси у лігво дракона.\n Прибувши на місце, та побачивши печеру,\nперебуваючи в легкому культурному шоці вирішили:')

#Вхід в печеру
a=input('1 Зайти в печеру; \n2 Поїхати додому;\n')
theend=('''Правильно, їжджай додому, принцес багато, а ти у мамці один такий гарнюнчик.
Живи неїбічно довго та щасливо, їзди на полювання та рибалку,
кожен день зустрічайся з друзями, пий багато пива, нажирайся в хлам,
розкидай шкари по своєму палацу,трахай служниць, сусідок та подружок,
співай у ванні, будь як пан-пердопан коли заманеться, гучно ригай,
та чухай свої яєла.''')

if(a=='1'):
    print(' Ви заходите в печеру, а там повна темрява,\nнемов в сраці негра, який сидить вночі в темній кімнаті!\n Ваші дії:')
    b=input('1 Запалити факел, та освітлити печеру;\n2 Вийти з печери;\n')
    if(b=='1'):
        print(''' Пройшовши весь лабірінт, в кінці, ви помічаєте як від світла вашого факела,
щось блищить.''')
    else:
        print(theend)
        input()
        exit(0)
#2-Підійти до світла
    print (' Трохи подумавши вирішуєте:')
    c=input('1 Підійти блище до підозрілого блиску;\n2 Розвернутися та вийти з печери;\n')
    if(c=='1'):
        print(''' Підійшовши ближче, ви помічаєте що це здоровецька срака дракона.''')
    else:
        print(theend)
        input()
        exit(0)
#3-Дати під сраку дракону
    print(' Трохи обісравши свій обладунок, та зібравшись з силами ви:')
    d=input('''1 Дали під срау дракону;\n2 Розвернулися й тишком нишком вийшли з печери,
розтираючи по сідницях тепленьке й м'якеньке;\n''')
    if(d=='1'):
        print(''' Нє, ну ти звичайно й неїбічний лицар, та головою треба думати,
ЦЕ Ж ЇБАНИЙ ДРАКОН!
ТОБІ ПІЗДА!''')
    else:
        print(theend)
        input()
        exit(0)
#Кінець гри
else:
    print(theend)
input()
