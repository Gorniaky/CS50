# Open and read the file as a single buffer
file = open('finance.sql', 'r')
sql = file.read()
file.close()

sqlCommands = sql.replace("\n", "").split(';')