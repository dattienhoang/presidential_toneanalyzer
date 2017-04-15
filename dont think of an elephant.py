# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 21:28:13 2017

@author: Dat Tien Hoang
"""

import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from watson_developer_cloud import ToneAnalyzerV3

#def pp_json(json_thing, sort=True, indents=4):
#    if type(json_thing) is str:
#        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
#    else:
#        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
#    return None
#
#df = pd.read_csv('C:/Users/Dat Tien Hoang/Desktop/data side projects/2016-us-presidential-debates/debate.csv')
#
#tone_analyzer = ToneAnalyzerV3(
#    username='bc4523fa-8efe-4298-80a9-aa0da187a69f',
#    password='T6v4FWCNNgPn',
#    version='2016-05-19')
#
#uniq_dates = list(np.unique(df['Date'], return_index=True)[0])
#for i in uniq_dates:
#    print 'Debate date: ', i
#    df_i_HRC = df.ix[(df['Date']== i) & (df['Speaker'] == 'Clinton')] # use | for 'and'
#    df_i_DJT = df.ix[(df['Date']== i) & (df['Speaker'] == 'Trump')] 
#    HRC = df_i_HRC['Text'].str.cat(sep=' ').decode('latin-1')
#    DJT = df_i_DJT['Text'].str.cat(sep=' ').decode('latin-1')
#    if i == uniq_dates[0]:
#        print 'special date test', i
#        tone_info1 = tone_analyzer.tone(text=HRC, sentences=False)
#        tone_info2 = tone_analyzer.tone(text=DJT, sentences=False)
#
##print 'HRC RESULT'
##print(json.dumps(tone_info1, indent=2))
##pp_json(tone_info1)
##
##print 'DJT RESULT'
##print(json.dumps(tone_info2, indent=2))
##pp_json(tone_info2)

labels_h = []
scores_h = []
labels_d = []
scores_d = []
for i in range(len(tone_info1['document_tone']['tone_categories'])):
    for j in range(len(tone_info1['document_tone']['tone_categories'][i]['tones'])):
        labels_h.append(tone_info1['document_tone']['tone_categories'][i]['tones'][j]['tone_name'])
        scores_h.append(tone_info1['document_tone']['tone_categories'][i]['tones'][j]['score'])
        
        labels_d.append(tone_info2['document_tone']['tone_categories'][i]['tones'][j]['tone_name'])
        scores_d.append(tone_info2['document_tone']['tone_categories'][i]['tones'][j]['score'])


# http://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111
# subplot indices = (nrow, ncol, plt no.)
fig = plt.figure(figsize=(12, 5))
plt.suptitle('Overall Scores for Debate of' + str(i), fontsize=18, linespacing=3)


pos = np.arange(len(labels_h[0:5]))
ax = fig.add_subplot(131)
plt.barh(pos-0.125, scores_h[0:5], align='center', height=0.25, color='blue')
plt.barh(pos+0.125, scores_d[0:5], align='center', height=0.25, color='red')
plt.yticks(range(len(labels_h[0:5])), labels_h[0:5], size='small')
plt.xticks([0.0, 0.5, 1.0])
ax.set_xlim([0,1.5])
ax.set_title('           Emotion', loc='left')
plt.ylim((-0.25,4.25))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.axvline(x=0.0, color='black', linestyle='dotted', linewidth=0.1)
plt.axvline(x=0.5, color='black', linestyle='dotted', linewidth=0.1)
plt.axvline(x=1.0, color='black', linestyle='dotted', linewidth=0.1)

pos = np.arange(len(labels_h[5:8]))
ax = fig.add_subplot(132)
plt.barh(pos-0.125+2, scores_h[5:8], align='center', height=0.25, color='blue')
plt.barh(pos+0.125+2, scores_d[5:8], align='center', height=0.25, color='red')
plt.yticks([i+2 for i in range(len(labels_h[5:8]))], labels_h[5:8], size='small')
plt.xticks([0.0, 0.5, 1.0])
ax.set_xlim([0,1.5])
ax.set_title('      Language Style', loc='left')
plt.ylim((-0.25,4.25))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.axvline(x=0.0, color='black', linestyle='dotted', linewidth=0.1)
plt.axvline(x=0.5, color='black', linestyle='dotted', linewidth=0.1)
plt.axvline(x=1.0, color='black', linestyle='dotted', linewidth=0.1)

pos = np.arange(len(labels_h[8:13]))
ax = fig.add_subplot(133)
plt.barh(pos-0.125, scores_h[8:13], align='center', height=0.25, color='blue')
plt.barh(pos+0.125, scores_d[8:13], align='center', height=0.25, color='red')
plt.yticks(range(len(labels_h[8:13])), labels_h[8:13], size='small')
plt.xticks([0.0, 0.5, 1.0])
ax.set_xlim([0,1.5])
ax.set_title('   Social Tendencies', loc='left')
plt.ylim((-0.25,4.25))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.axvline(x=0.0, color='black', linestyle='dotted', linewidth=0.1)
plt.axvline(x=0.5, color='black', linestyle='dotted', linewidth=0.1)
plt.axvline(x=1.0, color='black', linestyle='dotted', linewidth=0.1)

plt.show()