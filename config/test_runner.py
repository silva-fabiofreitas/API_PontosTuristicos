import os
import subprocess
import time

from django.test.runner import DiscoverRunner


class CustomTestRunner(DiscoverRunner):

    def setup_test_environment(self, **kwargs):
        # FNULL = open(os.devnull, 'w')
        # print('Starting elastic search...')
        # subprocess.Popen(['docker-compose', 'up', 'es'],
                        #  stdout=FNULL,
                        #  stderr=subprocess.STDOUT)
        # time.sleep(15)
        super(CustomTestRunner, self).setup_test_environment(**kwargs)

    def teardown_test_environment(self, *args, **kwargs):
        # FNULL = open(os.devnull, 'w')
        # print('Stopping elastic search...')
        # subprocess.Popen(['docker-compose', 'down'],
                        #  stdout=FNULL,
                        #  stderr=subprocess.STDOUT)
        super(CustomTestRunner, self).teardown_test_environment(*args, **kwargs)
