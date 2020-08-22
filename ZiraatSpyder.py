from BankSpyder import BankSpyder
from CustomExceptions import *


class ZiraatSpyder(BankSpyder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_rates_list(self):
        top_container = self.page_soup.find(
            'div', {'data-id': 'rdBranchDoviz'})

        rates_list = top_container.findChildren('tr', recursive=True)

        return rates_list[1:]   # Skip column names

    @staticmethod
    def _get_currency_name(raw_val):

        raw_name = raw_val[0].text

        currency_name = raw_name.strip()

        return currency_name

    @staticmethod
    def _get_bank_buys(raw_val):

        bank_buys = raw_val[2].text.replace(',', '.')
        effective_bank_buys = raw_val[4].text.replace(',', '.')

        return float(bank_buys), float(effective_bank_buys)

    @staticmethod
    def _get_bank_sells(raw_val):

        bank_sells = raw_val[3].text.replace(',', '.')
        effective_bank_sells = raw_val[5].text.replace(',', '.')

        return float(bank_sells), float(effective_bank_sells)

    def _extract_values(self, rates_list):

        extracted_values = []

        for raw_val in rates_list:

            raw_val_items = raw_val.findChildren(recursive=False)

            currency_name = self._get_currency_name(raw_val_items)

            bank_buys, effective_bank_buys = self._get_bank_buys(raw_val_items)

            bank_sells, effective_bank_sells = self._get_bank_sells(raw_val_items)

            extracted_values.append((
                currency_name,
                bank_buys,
                bank_sells,
                effective_bank_buys,
                effective_bank_sells))

        return extracted_values

    def _get_usd_value(self, values):
        for value in values:
            if value[0] == 'USD':
                return value

        raise CurrencyNotFoundException(
            "The currency USD wasn't found in the given values")

    def get_single_reading(self):

        rates_list = self._get_rates_list()

        extracted_values = self._extract_values(rates_list)

        usd_value = self._get_usd_value(extracted_values)

        return usd_value


if __name__ == '__main__':

    print("\n\nPlease launch main_script.py\n\n")
