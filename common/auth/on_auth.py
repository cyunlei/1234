from locust import events, task
from locust.runners import MasterRunner
import locust


class TaskStart(locust):

    @events.test_start.add_listener
    def on_test_start(self):
        print("开始测试！")

    @events.test_stop.add_listener
    def on_test_start(self):
        locust.user.HttpUser.environment.quit()
        print("结束测试！")

    @events.init.add_listener
    def on_locust_init(self, environment):
        if isinstance(environment.runner, MasterRunner):
            print('我在主节点上')
        else:
            print('我在工作节点或独立节点上')
