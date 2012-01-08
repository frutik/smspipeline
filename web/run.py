#!/usr/bin/python

import os,sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'smspipeline.settings'

from pipelines.models import Pipeline
from targets.models import TargetRunnerFactory

#try:
pipe, message = Pipeline.getSMS('430913', '1313 resend test test test 12')
#except:
#    print 'pipe not found'
#    sys.exit()	

msg = message.get()

for target in pipe.targets.all():
    target_runner = TargetRunnerFactory.get_runner(target)
    if target_runner.enabled:
	target_runner.send(msg)
	