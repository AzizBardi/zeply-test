from bitcoinlib.encoding import EncodingError
from bitcoinlib.keys import Key, HDKey
from mnemonic import Mnemonic

from crypto_address_generator.currency.bucket.coin import Coin


class BTC(Coin):
    @staticmethod
    def generate_private_key():
        private_key = Key()
        return private_key

    @staticmethod
    def generate_address(private_key):
        key = private_key
        address = key.address()
        return address

    @staticmethod
    def generate_multi_addresses(private_key, num_addresses):
        addresses = []
        key = private_key
        for _ in range(num_addresses):
            addresses.append(BTC.generate_address(key))
            key = BTC.generate_private_key()
        return addresses


    @staticmethod
    def validate_bitcoin_address(value):
        try:
            Key(value)
            return True
        except EncodingError:
            return False

    @staticmethod
    def generate_mnemonic_from_private_key(private_key):
        key = private_key
        entropy = key.secret
        mnemo = Mnemonic("english")
        mnemonic = mnemo.to_mnemonic(entropy)
        return mnemonic
