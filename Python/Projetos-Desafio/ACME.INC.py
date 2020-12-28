# https://wiki.python.org.br/ListaDeExerciciosProjetos

# conversion
def conversionBtoKB(value):
  value /= 1024
  return value

def conversionKBtoMB(value):
   value /= 1024
   return value 

def percentual(total, value_to_percent):
  value_to_percent /= total
  value_to_percent *= 100
  return value_to_percent

# data of exercise
employee = {1:['Alessandro', 456123789], 2:['anderson', 1245698456], 3:['antonio  ',123456456],
                4:['carlos  ', 91257581], 5:['cesar   ', 987458], 6:['rosemary', 789456125]}

separator = '-'*60

# list for store total of used memory
total_memory = []

# default print
print(
    'ACME Inc.\tUso do espaço em disco pelos usuários',
    '\n{}'.format(separator),
    '\n|N°\t|Usuário\t|Espaço utilizado(MB)\t|% do uso',
    '\n|\t|\t\t|\t\t\t|'
)

# to add values in the memory list
for data in range(0, len(employee)):
  memorykb = conversionBtoKB(employee[data + 1][1])
  memorymb = conversionKBtoMB(memorykb)

  total_memory.append(memorymb)
  
# all the operation with the data of employees and the used memory
for data in range(0, len(employee)):
  data_index = data + 1
  percent = percentual(sum(total_memory), total_memory[data])

  print(
      '|{}\t|{}\t| {:.2f}   \t\t| {:.2f}'.format(data_index, employee[data_index][0], total_memory[data], percent)
  )

# the final default print = total of memory used and the mean of memory
print(
    '\nTotal de espaço ocupado: {:.2f} MB'.format(sum(total_memory)),
    '\nEspaço médio ocupado: {:.2f} MB'.format(sum(total_memory)/len(total_memory))
)