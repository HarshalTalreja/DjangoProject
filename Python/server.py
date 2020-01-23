import secrets

class Token():
    id = ''
    state = ''
    assigned_to = ''
    def __init__(self):
        self.id = secrets.token_hex()
        self.state = 'Free'
        self.assigned_to = 'None'

if __name__ == '__main__':
    pool_length = 10
    pool = []
    for i in range(pool_length):
        myinstance = Token()
        pool.append(myinstance)

    def get_token_index(key):
        for i in range(len(pool)):
            if pool[i].id == key:
                return i

    def delete_token(key):
        index = get_token_index(key)
        del pool[index]
        new_instance = Token()
        pool.append(new_instance)

    def print_pool():
        for i in range(len(pool)):
            print(pool[i].id)

    def assign_token(ip):
