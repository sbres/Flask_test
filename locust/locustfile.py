"""
This is just a test that gets Locust running on runnable.com.
"""

from locust import HttpLocust, TaskSet, task
import string
import random
import json

class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        user_id = random.randint(1, 10000)
        data = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(25))
        key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
        post = self.client.post("/put", {'id': user_id, 'key': key, 'value': data}, catch_response=True)

        res = self.client.request("GET", "/get", params={'id': user_id, 'key': key}, name='/get', catch_response=True)
        try:
            test = res.json()
            if test == data:
                res.success()
                post.success()
            else:
                res.failure('Not the same param !')
                post.failure('Not the same param !')
        except Exception, e:
            print e.message
            res.failure(e.message)
            post.failure(e.message)

class Simple_load(TaskSet):
    @task
    def get_page(self):
        self.client.get('/')


class MyLocust(HttpLocust):
    #host = "http://127.0.0.1:8000"
    host = "http://dev-shosha-wa6yr4q2q5.elasticbeanstalk.com"
    #host = "http://192.168.0.42:8000"
    min_wait = 1000
    max_wait = 1000
    task_set = Simple_load

