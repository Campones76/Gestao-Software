DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = '192.168.6.110'#'192.168.19.209'#'SCHOOL594B' #  SERVER_NAME = ''
DATABASE_NAME = 'ItOnDemand' 
UID = 'ten1' # UID = 'teste1'
PWD = 'VeryStr0ngP@ssw0rd'#'1234'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    PWD={PWD};
    UID={UID};
    Trust_Connection=yes;
"""
