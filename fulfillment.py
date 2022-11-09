import time

from main import redis, Product

key = 'order-completed'
group = 'warehouse-group'

try:
    redis.xgroup_create(name=key, groupname=group, mkstream=True)
    print("Group created")
except Exception as e:
    print(str(e))
    
while True:
    try:
        results = redis.xreadgroup(groupname=group, consumername=key, streams={key: '>'})
        print(results)
    except Exception as e:
        print(str(e))
    time.sleep(3)