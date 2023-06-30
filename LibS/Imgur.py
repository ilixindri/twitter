import pip
try: from imgurpython import ImgurClient
except: pip.main(['install', 'imgurpython'])
client_id = ''
client_secret = ''
client = ImgurClient(client_id, client_secret)
items = client.upload_from_path(path, config=None, anon=True)
    