from config.config import urls, users


class Test:
    base_url = urls.get('test')
    username = users.get('default').get('username')
    password = users.get('default').get('password')
