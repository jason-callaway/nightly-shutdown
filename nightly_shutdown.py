#!/usr/bin/env python
"""Nightly shutdown tool for AWS EC2 cost-control"""

import boto.ec2
import yaml

__author__ = 'Jason Callaway'
__email__ = 'jason@jasoncallaway.com'
__license__ = 'Apache License Version 2.0'
__version__ = '0.1'
__status__ = 'alpha'

config_file = '/etc/nightly_shutdown.yml'
with open(config_file) as f:
    config = yaml.safe_load(f)

conn = boto.ec2.connect_to_region(config['region'],
                                  aws_access_key_id=config['access_key'],
                                  aws_secret_access_key=config['secret_key'])

reservations = conn.get_all_reservations()

running_instances = []
for r in reservations:
    for i in r.instances:
        if i.state == "running":
            if i.id not in config['whitelist']:
                running_instances.append(i.id)

if len(running_instances) > 0:
    conn.stop_instances(instance_ids=running_instances)
