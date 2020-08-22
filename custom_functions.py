from ZiraatSpyder import ZiraatSpyder
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def make_spyder():

    url = "https://www.ziraatbank.com.tr/tr/fiyatlar-ve-oranlar"

    options = FirefoxOptions()
    options.headless = True

    spyder = ZiraatSpyder(url=url, options=options)

    return spyder

