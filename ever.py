#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-09-17

import subprocess
import config
import time
import os
from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec


def notes_list_requests(notebookGuid, noteStore):
    filterInstance = NoteFilter(notebookGuid=notebookGuid)
    offset = 0
    max_notes = 250
    result_spec = NotesMetadataResultSpec(includeTitle=True,
                                          includeCreated=True,
                                          # includeTagGuids=True
                                          )
    result_list = noteStore.findNotesMetadata(config.dev_token,
                                              filterInstance,
                                              offset,
                                              max_notes,
                                              result_spec)
    return result_list

def date_getter():                                                                                                                       
    return time.strftime("%m-%d", time.localtime())


def time_convert(timestamp):
    time_cleared = int(str(timestamp)[0:-3])
    time_converted = time.strftime('%Y-%m-%d', time.localtime(time_cleared))
    return time_converted


def main():
    print 'We are pulling some notes, it takes some times...'
    client = EvernoteClient(token=config.dev_token,
                            sandbox=False)
    noteStore = client.get_note_store()
    groupList = set([_.stack for _ in noteStore.listNotebooks()])
    with open('README.md', 'w') as r:
        r.write("""
# Mylearning-road
A list of all my notes below in Evernote to show my currently learning road map
and some other in the past.

# Credit
http://stackoverflow.com/questions/18532862/setting-notefilter-in-evernote-api

# Overview

""")

    with open('README.md', 'a+') as r:
        for groupname in groupList:
            print >> r, '- ' + groupname + '  '
            for notebook in noteStore.listNotebooks():
                if notebook.stack == groupname:
                    print >> r, '&emsp;&emsp;' + notebook.name + '  '
                    for note in notes_list_requests(notebook.guid, noteStore).notes:
                        print >> r, '&emsp;&emsp;&emsp;&emsp;' + \
                            note.title, time_convert(note.created) + '  '

def git():
    if 'clean' not in subprocess.check_output('git status',shell=True):
        os.system('git add .')
        os.system("git commit -m 'weekly auto update {}'".format(date_getter()))
        os.system('git push origin master')

if __name__ == '__main__':
    main()
    git()	
