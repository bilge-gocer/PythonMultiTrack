from controller.account_parser import parse_account_file
from controller.transaction_parser import parse_transaction_file
from model.account import Account
import json
from controller.custom_encoder import CustomEncoder


def parse_data(accounts_path, transaction_path):
    parse_account_file(accounts_path)
    parse_transaction_file(transaction_path)

    json_output = json.dumps(list(Account.get_accounts().values()), cls=CustomEncoder)
    return json_output