#!/usr/bin/env python

import subprocess

class Nginx:
    def __init__(self, agent_config, checks_logger, raw_config):
        self.agent_config = agent_config
        self.checks_logger = checks_logger
        self.raw_config = raw_config

        self.command = ["curl", "-I", "-s"]
        if 'Nginx' in self.raw_config and 'url' in self.raw_config['Nginx']:
            self.command.append(self.raw_config['Nginx']['url'])
        else:
            self.command.append("http://localhost")

    def run(self):
        try:
            output = subprocess.check_output(self.command)
            return {'running': True}
        except subprocess.CalledProcessError:
            self.checks_logger.exception("Nginx doesn't seem to be running, perhaps check your configuration?")
            return {'running': False}

if __name__ == '__main__':
    import logging
    print Nginx({}, logging, {}).run()
