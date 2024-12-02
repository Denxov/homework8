from os import statvfs_result

class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message=message
class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message=message
class Car:

    __vin=0
    __numbers=0
    def __is_valid_vin(self,vin_number):
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        elif not type(vin_number)==int:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        else:return True
    def __is_valid_numbers(self,numbers):
        if  len(numbers)!=6:
            raise IncorrectCarNumbers('Неверная длина номера')
        elif not type(numbers)==str:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        else: return True

    def __init__(self,model:str,vin:int,numbers:str):
        self.model=model
        if Car.__is_valid_vin(self,vin): self.__vin=vin
        if Car.__is_valid_numbers(self,numbers):self.__numbers=numbers

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')



