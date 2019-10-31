import csv #Libreria que permite tener funciones y objetos utiles para manipular archivos .csv
import os

CLIENT_TABLE = '.clients.csv' #Variable que almacena el archivo donde se creo la base de datos y a donde se van agregando nuevos elementos
CLIENT_SCHEMA = ['name', 'company', 'email', 'position'] #Elementos de identificación de cada usuario
clients = [] #Lista que se utiliza para manipular los datos


def create_client(client): #Función que permite crear un cliente
    global clients #Esta palabra reservada permite traer la variable clients que ha sido declarada fuera del scope de la función

    if client not in clients:
        clients.append(client)
    else:
        print('Client is already in client\s list')


def list_clients(): #Función para mostrar los clientes que están en la base de datos
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
        uid = idx,
        name = client['name'],
        company = client['company'],
        email = client['email'],
        position = client['position']))


def update_client(client_id, updated_client): #Función para actualizar la información de un cliente
    global clients

    if len(clients) - 1 >= client_id:  #Este condicional permite rastrear el usuario al que se le modificarán los datos a partir del id
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_name): #Función para eliminar cliente
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break
    else:
        warning()


def search_client(client_name): #Función para buscar cliente
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True



def _get_client_field(field_name, message='What is the client {}?'): #Obtener datos del usuario
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _initialize_clients_from_storage(): #Esta función declara un context manager para manipular el archivo csv
    with open(CLIENT_TABLE, mode='r') as f: #Esta es la sintaxis de un context manager
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA) #Esta variable permite explorar el archivo asumiendo cada elemento de la base de datos como un diccionario

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE) #Se crea un archivo temporal que va a contener los nuevos elementos que se agreguen por que es necesario reemplazar el archivo inicial con este nuevo dado que una vez se cierra el programa, los cambios guardados no se registrarian de otra forma
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def warning():
    print('Client is no in client\'s list')


def _print_welcome():
    print('Welcome to Juan Ventas')
    print('*'*50)
    print('What would you like to do today?')
    print('[U]pdate client')
    print('[C]reate client')
    print('[L]ist client')
    print('[D]elete client')
    print('[S]earch client')



if __name__=='__main__': #Esta es una sintaxis especial de python que inicializa el programa
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()

        create_client(client)
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
    elif command =='D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')


    _save_clients_to_storage()
