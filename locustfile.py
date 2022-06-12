from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def testget(self):
        self.client.get("https://datmq-udacity-project.azurewebsites.net")