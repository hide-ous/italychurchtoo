from pytangle.api import API

DEFAULT_CT_TOKEN_PATH = './ct.txt'
def read_token(fpath=DEFAULT_CT_TOKEN_PATH):
    with open(fpath) as f:
        return f.read().strip()
if __name__ == '__main__':
    token=read_token()
    api = API(token=token)

    for post in api.search(
        includeHistory=False,
        language='it',
        searchTerm=''
    ):
        print(post)
        break
