# pypi.org

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column(fieldname='Pokemon Name', column=['Pikachu', 'Squirtle', 'Charmander'], align='c')
table.add_column(fieldname='Type', column=['Electric', 'Water', 'Pikachu'], align='c')
print(table)

table.align = 'l'
print(table)
table.del_row(row_index=1)
print(table)