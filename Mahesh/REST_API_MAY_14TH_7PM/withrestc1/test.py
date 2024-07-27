import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'
import json
def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
        'id':id
        }
    resp = requests.get(BASE_URL + END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource()
# def create_resource():
#     new_emp = {
#     'eno':106,
#     'ename':'Mallika',
#     'esal':13123,
#     'eaddr':'Chennai',
#     }
#     resp = requests.post(BASE_URL + END_POINT, data = json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()
# def update_resource(id):
#     new_emp = {
#     'id':id,
#     'ename':'Sunny Leone',
#     'esal':8000,
#     }
#     resp = requests.put(BASE_URL + END_POINT, data = json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(6)
# def delete_resource(id):
#     new_emp = {
#     'id':id,
#     }
#     resp = requests.delete(BASE_URL + END_POINT, data = json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(7)
