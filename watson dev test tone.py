# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:40:14 2017

@author: Dat Tien Hoang
"""

# see documentation
# https://github.com/watson-developer-cloud/tone-analyzer-nodejs
# http://www.ibm.com/watson/developercloud/doc/tone-analyzer/index.shtml

import json
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    username='bc4523fa-8efe-4298-80a9-aa0da187a69f',
    password='T6v4FWCNNgPn',
    version='2016-05-19')

tone_info = tone_analyzer.tone(text='I am very happy. Are you happy? Fuck you.', )

print(json.dumps(tone_info, indent=2))

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

pp_json(tone_info)