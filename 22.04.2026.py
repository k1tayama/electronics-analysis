import requests

class User:
    def __init__(self, name, email, country):
        self.name = name 
        self.email = email 
        self.country = country
    def __eq__(self, other):
        if not isinstance(other, user):
            return False
        return self.email == other.email

    def __hash__(self):
        return hash(self.email)
    

url = "https://randomuser.me/api/"

def print_attrs(obj):
    income_meth = dir(obj)
    result_meth = list([x for x in income_meth if "__" not in x ])
    return result_meth
p = {"results": 5}

r = requests.get(url, params=p)
data = r.json()
users = []
for user in data['results']:
    new_user = (
        user['name']['first'],
        user['email'],
        user['location']['country']
    )
    
    users.append(new_user)
    users.append(new_user)

print(print_attrs(users[0]))