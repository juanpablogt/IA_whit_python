def cs(data):

    for i in dates:
        nam= i['name']
        mar= i['marca']

        if i['marca'] == 'bmw':
            print("mi nombre es "+ nam.title() + " y tengo un "+mar.upper()+" nice to meet you!")    

        else:
            print("mi nombre es "+ nam.title() + " y tengo un "+mar.title()+" nice to meet you!")





dates = [{'name':'juan', 'marca':'Audi'},{'name':'mia', 'marca':'bmw'},{'name':'pepe', 'marca':'Ford'}]
cs(dates)

