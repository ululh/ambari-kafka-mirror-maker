"""
Kafka Mirror maker 
inspired from Symantec Elasticsearch stack for Ambari

"""

from resource_management import *
import signal
import sys
import os
from os.path import isfile

from mmconfig import mmconfig


class mirrorMaker(Script):

    def install(self, env):
        print 'No install necessary, Mirror Maker comes with Kafka package'

    def configure(self, env):
        import params
        env.set_params(params)
        print 'build configuration';
        mmconfig()   

    def stop(self, env):
        import params
        env.set_params(params)
        stop_cmd = format("service elasticsearch stop")
        Execute(stop_cmd)
        print 'Stop the Master'

    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("/usr/hdp/current/kafka-broker/bin/kafka-run-class.sh kafka.tools.MirrorMaker --consumer.config {{}}  --producer.config {{}} --whitelist={{mirror.topics.whitelist}}")
        Execute(start_cmd)
        print 'Start the Master'
"""
    def status(self, env):
        import params
        env.set_params(params)
        status_cmd = format("service elasticsearch status")
        Execute(status_cmd)
        print 'Status of the Master'
"""

if __name__ == "__main__":
    mirrorMaker().execute()


