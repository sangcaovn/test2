import requests
import json

def read_json():
    data=None
    with open("payload.json") as data_file:
        data = json.load(data_file)

    return data

def test2(gh_url):
    import urllib3

    token = 'A0008935689275482795593!s/riPgVaFR9UFIlU5pbhlanSx7J5FyYAnEYKvaX9Q2M998HBKpZJKNlVHwKcVLyR8idbVw+KPxiuZroptfYGvbH1aHY='
    http = urllib3.PoolManager()
    # gh_url = 'https://core-api-demo.grasshopper.tmachine.io/v1/contracts:simulate'
    headers = urllib3.util.make_headers(user_agent= 'my-test/1.0.1', basic_auth=token)
    requ = http.request('POST', gh_url, headers=headers)
    print (requ.headers)
    print(requ.data)

def test_url(url):
    token = 'A0008935689275482795593!s/riPgVaFR9UFIlU5pbhlanSx7J5FyYAnEYKvaX9Q2M998HBKpZJKNlVHwKcVLyR8idbVw+KPxiuZroptfYGvbH1aHY='
    
    session = requests.Session()
    session.headers.update({'user-agent': 'test'})
    session.headers.update({'x-auth-token': token})
    session.headers.update({'referer': 'https://core-api-demo.grasshopper.tmachine.io/v1/contracts:simulate'})
    header={
        'user-agent': 'my-test',
        'referer': 'https://core-api-demo.grasshopper.tmachine.io/v1/contracts:simulate',
        'Content-Type':'application/json',
        'X-Auth-Token':token
    }
    res=session.post(
        url,
        data={}
    )
    print ("res data ",res.json())

if __name__=="__main__":
    url="https://core-api-demo.grasshopper.tmachine.io/v1/contracts:simulate"
    # test_url(url)
    test2(url)