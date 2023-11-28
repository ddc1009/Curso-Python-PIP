import csv 

# Transformar los datos a diccionario
def read_csv(path):
  with open(path, 'r') as csvfile:
    #Obtener el nombre de las columnas
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header,row)
      #Para generar el diccionario
      country_dic = {key: value for key, value in iterable}
      data.append(country_dic)
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

