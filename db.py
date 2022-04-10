def get_database(dbname):
    from pymongo import MongoClient
    from dotenv import load_dotenv, dotenv_values

    load_dotenv() # get variables from .env file

    username = dotenv_values()['USERNAME']
    password = dotenv_values()['PASSWORD']
    clustername = dotenv_values()['CLUSTERNAME']
    CONNECTION_STRING = "mongodb+srv://{}:{}@{}.jn0tp.mongodb.net/{}?retryWrites=true&w=majority".format(username, password, clustername, dbname)

    client = MongoClient(CONNECTION_STRING)

    return client[dbname]

if __name__ == "__main__":
    db = get_database(dbname = "")
