import os
import sqlite3
import sys
import platform

db = sqlite3.connect('productsDB.db')

cursor = db.cursor()

def clear():
    system = platform.system()
    if system == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

def handleError(err):
    clear()
    print(err)
    input('enter to continue')
    sys.exit()

def createDatabase():
    cursor.execute(f'create table if not exists produtos(nome text, preco real)')

def insertProduct():
    productName = str(input('digite o nome do produto -> '))
    productPrice = float(input('digite o preço do produto -> ')) 

    try:
        cursor.execute(f'insert into produtos values("{productName}", "{productPrice}")')
        db.commit()
        input('atualizado com sucesso')
        main()
    except Exception as err:
        handleError(err)

def updateProduct():
    try:
        cursor.execute('select * from produtos')
        
        rows = cursor.fetchall()

        products = getProducts()
        print(products)
            
        productNameToUpdate = str(input('Digite o nome do produto que deseja atualizar -> '))
    except Exception as err:
        handleError(err)

    updateAction = str(input('o que deseja atualizar?\n\n1 - nome\n2 - preço\n3 - tudo\n\n-> '))

    if updateAction == '1':
        productNewName = str(input('Digite o novo nome -> '))
        try:
            cursor.execute(f'update produtos set nome = "{productNewName}" where nome = "{productNameToUpdate}"')
            db.commit()
            input('dados atualizados!')
            main()
        except Exception as err:
            handleError(err)

    elif updateAction == '2':
        productNewPrice = float(input('Digite o novo preço -> '))
        try:
            cursor.execute(f'update produtos set preco = "{productNewPrice}" where nome = "{productNameToUpdate}"')
            db.commit()
            input('dados atualizados!')
            main()
        except Exception as err:
                handleError(err)

    elif updateAction == '3':
        productNewName = str(input('Digite o novo nome -> '))
        productNewPrice = float(input('Digite o novo preço -> '))
        try:
            cursor.execute(f'update produtos set nome = "{productNewName}" where nome = "{productNameToUpdate}"')
            cursor.execute(f'update produtos set preco = "{productNewPrice}" where nome = "{productNameToUpdate}"')
            db.commit()
        except Exception as err:
            handleError(err)

def getProducts():
    try:
        cursor.execute('select * from produtos')
        
        rows = cursor.fetchall()

        names = []
        prices = []
        space = ' '
        max_characters = 20
        table = f'Nome{(space * max_characters)}Preço\n\n'
        for r in rows:
            names.append(r[0])
            prices.append(r[1])

        for i in range(0, (len(names) -1)):
            table += f'{names[i]}{(space * (max_characters - len(names[i])))}R${prices[i]}\n'
        
        return table

    except Exception as err:
        handleError(err)

def main():
    clear()
    createDatabase()

    action = str(input('digite a ação que deseja fazer:\n\n1 - inserir um novo produto\n2 - atualizar um produto existente\n3 - Ver produtos existentes\n\n-> '))

    if action == '1':
        clear()
        insertProduct()

    elif action == '2':
        clear()
        updateProduct()
    
    elif action == '3':
        clear()
        products = getProducts()
        
        print(products)
        input('Aperte enter para continuar')
        
if __name__ == '__main__':
    main()