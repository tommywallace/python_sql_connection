from scripts import sql_func

arg1 = input('Insert first argument: ')
arg2 = input('Insert second argument: ')

if __name__ == '__main__':
    sql_func.sql_query(arg1,arg2)
