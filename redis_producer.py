import redis
import sys
from uuid import uuid4
from time import sleep

REDIS_HOST = 'haproxy'

if __name__ == "__main__":
    r = redis.Redis(host=REDIS_HOST, port=6379, db=0)
    if len(sys.argv) < 3:
        print("Required: role (prod,cons); sleep time")
        sys.exit(1)

    if sys.argv[1] == 'prod':
        while(1):
            k = str(uuid4())
            r.set('testkey', 'val_'+k)
            print('set: testkey ' + k)
            sleep(int(sys.argv[2]))

    elif sys.argv[1] == 'cons':
        while(1):
            k = r.get('testkey')
            print(k)
            sleep(int(sys.argv[2]))
    
    else:
        print('wrong role')
        sys.exit(1)
