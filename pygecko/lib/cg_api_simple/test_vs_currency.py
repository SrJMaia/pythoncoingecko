from vs_currency import get_supported_vs_currencies_api
import unittest


class TestVsCurrency(unittest.TestCase):
    def test_api_status_without_status_code(self):
        url = url = "https://api.coingecko.com/api/v3/"
        actual = get_supported_vs_currencies_api(url=url)
        expected = [
            "btc",
            "eth",
            "ltc",
            "bch",
            "bnb",
            "eos",
            "xrp",
            "xlm",
            "link",
            "dot",
            "yfi",
            "usd",
            "aed",
            "ars",
            "aud",
            "bdt",
            "bhd",
            "bmd",
            "brl",
            "cad",
            "chf",
            "clp",
            "cny",
            "czk",
            "dkk",
            "eur",
            "gbp",
            "hkd",
            "huf",
            "idr",
            "ils",
            "inr",
            "jpy",
            "krw",
            "kwd",
            "lkr",
            "mmk",
            "mxn",
            "myr",
            "ngn",
            "nok",
            "nzd",
            "php",
            "pkr",
            "pln",
            "rub",
            "sar",
            "sek",
            "sgd",
            "thb",
            "try",
            "twd",
            "uah",
            "vef",
            "vnd",
            "zar",
            "xdr",
            "xag",
            "xau",
            "bits",
            "sats",
        ]
        print(actual)
        self.assertEqual(actual, expected)
