import sys
from twython import Twython
CONSUMER_KEY = 'Rll9w0K6ubNtsvnvGNXuPmzt4'
CONSUMER_SECRET = 'CqMFxVx4JtFSgZTnFKK7FqqMFieenxi4FaPdRx5o0X3BGMeRib'
ACCESS_KEY = '832577964898398208-E9Yb76p2Ze5guBw9RACEw8TJ9aPRTA0'
ACCESS_SECRET = '61YkFkAkjOpGgCVwEHuaZ4znYgiK8cy56FQIF1hT4aUEd'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])


#tested 23_02_2017 updates ok. Test command:
#python tweeter.py "That's Insane"
