б) Подумайте, как наделить бота "интеллектом"

# вариант человек против бота c "интеллектом":
из  случайного  импорта  randint

def  input_dat ( имя ):
    x  =  int ( input ( f" { name } , введите количество конфет, которое возьмете от 1 до 28: " ))
    в то время как  х  <  1  или  х  >  28 :
        x  =  int ( input ( f" { name } , введите корректное количество конфет: " ))
    вернуть  х


def  p_print ( имя , k , счетчик , значение ):
    print ( f"Ходил { name } , он взял { k } , теперь у него { counter } . Осталось на столе { value } конфет." )


определение  bot_calc ( значение ):
    k  =  случайный ( 1 , 29 )
    в то время как  значение - k  <=  28  и  значение  >  29 :
        k  =  случайный ( 1 , 29 )
    вернуть  к

player1  =  input ( "Введите имя первого игрока: " )
player2  =  "Бот"
value  =  int ( input ( "Ввести количество конфет на столе: " ))
flag  =  randint ( 0 , 2 ) # флаг очередности
если  флаг :
    print ( f"Первый ходит { player1 } " )
еще :
    print ( f"Первый ходит { player2 } " )

счетчик1  =  0
счетчик2  =  0

в то время как  значение  >  28 :
    если  флаг :
        k  =  input_dat ( player1 )
        счетчик1  +=  к
        значение  -=  к
        флаг  =  Ложь
        p_print ( игрок1 , k , счетчик1 , значение )
    еще :
        k  =  bot_calc ( значение )
        счетчик2  +=  к
        значение  -=  к
        флаг  =  Истина
        p_print ( игрок2 , k , счетчик2 , значение )

если  флаг :
    print ( f"Выиграл { player1 } " )
еще :
    print ( f"Выиграл { player2 } " )