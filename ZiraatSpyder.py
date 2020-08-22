from BankSpyder import BankSpyder


class ZiraatSpyder(BankSpyder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_single_reading(self):
        pass