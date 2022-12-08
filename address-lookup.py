# Import the necessary modules from web3.py
from web3 import Web3

# Set the URL of the Ethereum node to connect to
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/your-api-key"))

# Prompt the user to enter an Ethereum address
address = input("Enter Address: ")

# Use web3.py to lookup the balance of the entered address
balance = web3.eth.getBalance(address)

# Print the balance to the console
print(f"Balance: {balance}")
