file_header_record = 'FH19032019:23020002'

print(type(file_header_record))

client_transaction_record = 'CT19032019:080414D000000000023.5500001431759372813465'
record_type = 'CT'
transaction_date = '19032019:080414'
transaction_type = 'D'
transaction_amount = '000000000023.550000'
third_party_acount = '1431759372813465'

print(type(client_transaction_record))
print(type(record_type))
print(type(transaction_date))
print(type(transaction_type))
print(type(transaction_amount))
print(type(third_party_acount))

transaction_amount = 000000000023.550000

print(type(transaction_amount))

third_party_acount = 1431759372813465

print(type(third_party_acount))