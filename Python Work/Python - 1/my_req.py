import requests

ip = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(ip.json()['origin']))

browser = requests.get('https://httpbin.org/user-agent')
print('You seem to be using {0}'.format(browser.json()['user-agent']))

# https://httpbin.org/
# I guess the idea, is using python, you can make an HTTP
# Request, the webpage/webservice can return data that we 
# can break down into something useable?
