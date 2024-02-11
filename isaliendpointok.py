import httpx 

ENDPOINT_PAGE_URL = 'https://www.alibabacloud.com/help/en/simple-application-server/developer-reference/api-swas-open-2020-06-01-endpoint'


TELEGRAM_BOT_TOKEN = 'xxx'
TELEGRAM_CHATID = 1111111


C = httpx.Client(verify=False , follow_redirects=True )

r = C.get(ENDPOINT_PAGE_URL)

telegramUrl = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN +  '/sendMessage'

if 'Thailand' in r.text :
    data = {
        'chat_id' : TELEGRAM_CHATID,
        'text' : 'thailand ok le'
    }
    r = C.post(url=telegramUrl, data=data)

if 'Philippines' in r.text :
    data = {
        'chat_id' : TELEGRAM_CHATID,
        'text' : 'philippines endpoint ok le'
    }
    r = C.post(url=telegramUrl, data=data)
    

