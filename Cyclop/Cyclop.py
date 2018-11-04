import time
from selenium import webdriver

def call_driver(link, argument):
    browser = webdriver.ChromeOptions()

    if argument == 1:
        browser = add_option(browser)
    browser = webdriver.Chrome(chrome_options=browser)
    browser.get(link)
    # browser.execute_script('alert("código javascript sendo executado")')
    # time.sleep(3)
    # br.quit()
    return browser


def add_option(browser):
    # browser.add_argument("--headless")
    browser.add_argument("--start-maximized")
    browser.add_argument("--disable-notifications")
    browser.add_argument("--incognito")

    return browser


def login(browser, usr, pas):
    browser.find_element_by_id('txtcd_Logon').send_keys(usr)
    browser.find_element_by_id('txtcd_Pwd').send_keys(pas)
    browser.find_element_by_id('btOK').click()


def unidade(browser):
    browser.find_element_by_id('cmbUnidade').send_keys('CIVEL')
    browser.find_element_by_id('btOk').click()
    # <li class="s-header-lvl2-item" rel="Menu_5"><a href="#" rel="PJ" onclick="MudaClasseMenu('Menu_5', '6');Carrega_Combo('PJ');">Jurídico</a></li>

    print(browser.find_elements_by_class_name('s-header-lvl2-item'))

    # time.sleep(5)
    browser.quit()


if __name__ == '__main__':
    url = 'https://ref.gestorjuridico.com.br/Paginas/Principal/_FSet_Abertura.asp'
    username = 'agp.e-xyon'
    password = '417j3l'
    option = 1
    br = call_driver(url, option)
    try:
        login(br, username, password)
        unidade(br)
        request = br.current_url
    except:
        request = ''
        br.switch_to_window(br.switch_to_window[-1])
    print('resposta:'+request)

    # print(br.page_source)
    # forcebrute()
