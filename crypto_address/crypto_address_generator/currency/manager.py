from crypto_address_generator.currency.bucket.coin import Coin
from django.conf import settings


class CoinManager:
    def __init__(self):
        self.coins = {}
        self.register(settings.COINS)

    def register(self, coins_dict):
        for coin_acronym, coin_class in coins_dict.items():
            self.register_coin(coin_acronym, coin_class)

    def register_coin(self, coin_acronym, coin_class):
        if issubclass(coin_class, Coin):
            self.coins[coin_acronym.upper()] = coin_class()
        else:
            raise "this class is not a Coin please check it parent class"

    def is_exist(self, acronym):
        return acronym.upper() in self.coins

    def generate_private_key(self, coin_acronym):
        coin_class = self.coins.get(coin_acronym.upper())
        if coin_class:
            return coin_class.generate_private_key()
        raise ValueError(f"Coin '{coin_acronym}' is not registered.")

    def generate_address(self, coin_acronym, private_key=None):
        private_key = private_key if private_key else self.generate_private_key(coin_acronym.upper())
        coin_class = self.coins.get(coin_acronym.upper())
        if coin_class:
            return coin_class.generate_address(private_key)
        raise ValueError(f"Coin '{coin_acronym}' is not registered.")

    def generate_multi_addresses(self, coin_acronym, num_addresses, private_key=None):
        private_key = private_key if private_key else self.generate_private_key(coin_acronym.upper())
        coin_class = self.coins.get(coin_acronym.upper())
        if coin_class:
            return coin_class.generate_multi_addresses(private_key, num_addresses)
        raise ValueError(f"Coin '{coin_acronym}' is not registered.")

    def validate_address(self, coin_acronym, address):
        coin_class = self.coins.get(coin_acronym.upper())
        if coin_class:
            return coin_class.validate_address(address)
        raise ValueError(f"Coin '{coin_acronym}' is not registered.")
