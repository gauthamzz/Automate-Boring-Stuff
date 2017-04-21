from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--dns-prefetch-disable')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--lang=en-US')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})
browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
browser.implicitly_wait(25)

browser.get('http://facebook.com')

emailElem = browser.find_element_by_id('email')
emailElem.send_keys('') # add user name over here
passwordElem = browser.find_element_by_id('pass')
passwordElem.send_keys('') # add password over here
passwordElem.submit()

# findchat = browser.find_element_by_partial_link_text('_55ln')
# findchat.submit()

# html = browser.find_element_by_class_name('_55lp')
