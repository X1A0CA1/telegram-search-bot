# coding: utf-8
import glob
import os.path

MOD_PATH = 'user_handlers'

custom_handlers = []
files = glob.glob(MOD_PATH + '/[a-z]*.py')
for filename in files:
    module_name, ext = os.path.splitext(os.path.basename(filename))
    module = __import__('{}.{}'.format(MOD_PATH, module_name), fromlist=['*'])
    custom_handlers.append(module.handler)
