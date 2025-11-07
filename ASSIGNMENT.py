def find_account_index(account_ids, account_id):
    for id in range (len(account_ids)):
        if account_ids[id] == account_id:
            return id
    return -1
def process_ledger(initial_accounts, initial_balances, transactions):
    accounts = initial_accounts[:]
    balances = initial_balances[:]
    for transaction in transactions:
        command = transaction[0]
        account_id = transaction[1]
        if command == "OPEN":
            initial_deposit = transaction[2]
            index = find_account_index(accounts , account_id )
            if index == -1 :
                accounts.append(account_id)
                balances.append(initial_deposit)
        elif command == "DEPOSIT":
            amount = transaction[2]
            index = find_account_index(accounts, account_id)
            if index != -1 :
                balances[index] += amount
        elif  command == "WITHDRAW":
            amount_w = transaction[2]
            index = find_account_index(accounts, account_id)
            if index != -1 and balances[index] >= amount:
                balances[index]-= amount_w 
    return accounts , balances
    
accounts = ["ACC-001","ACC-002","ACC-003 "]
balances=[500.00,1200.00,250.00]
daily_transactions = [
    ["DEPOSIT", "ACC-001", 150.00],
    ["WITHDRAW", "ACC-002", 250.00],
    ["WITHDRAW", "ACC-003", 300.00], 
    ["OPEN", "ACC-004", 1000.00],
    ["DEPOSIT", "ACC-002", 50.00]
]
final_accounts , final_balances =  process_ledger(accounts, balances, daily_transactions)
print("Final Accounts:",final_accounts)
print("Final Balances:",final_balances)

     
