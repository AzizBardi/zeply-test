from mnemonic import Mnemonic
from web3 import Account, Web3

from crypto_address_generator.currency.bucket.coin import Coin


class ETH(Coin):
    @staticmethod
    def generate_private_key():
        private_key = Account.create().key.hex()
        return private_key

    @staticmethod
    def generate_address(private_key):
        address = Account.from_key(private_key).address
        return address

    @staticmethod
    def generate_multi_addresses(private_key, num_addresses):
        addresses = []
        current_private_key = private_key
        for _ in range(num_addresses):
            address = Account.from_key(current_private_key).address
            addresses.append(address)
            current_private_key = hex(int(current_private_key, 16) + 1)
        return addresses

    @staticmethod
    def validate_address(value):
        return not Web3.is_checksum_address(value)

    @staticmethod
    def generate_mnemonic_from_private_key(private_key):
        entropy = bytes.fromhex(private_key)
        mnemo = Mnemonic("english")
        mnemonic = mnemo.to_mnemonic(entropy)
        return mnemonic