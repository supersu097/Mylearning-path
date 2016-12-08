#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-09-17

import config
import time
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


def time_convert(timestamp):
    time_cleared = int(str(timestamp)[0:-3])
    time_converted = time.strftime('%Y-%m-%d', time.localtime(time_cleared))
    return time_converted


def main():
    client = EvernoteClient(token=config.dev_token,
                            sandbox=False)
    noteStore = client.get_note_store()
    groupList = set([_.stack for _ in noteStore.listNotebooks()])
    with open('README.md', 'w') as r:
        r.write("""
# Mylearning-road
A list of all my notes below in Evernote to show my learning road map and some other in the past.

# Credit
http://stackoverflow.com/questions/18532862/setting-notefilter-in-evernote-api

# Overview

""")

    with open('README.md', 'a+') as r:
        for groupname in groupList:
            print >> r, '- ' + groupname + '  '
            for _ in noteStore.listNotebooks():
                if _.stack == groupname:
                    print >> r, '&emsp;&emsp;' + _.name + '  '
                    for _ in notes_list_requests(_.guid, noteStore).notes:
                        print >> r, '&emsp;&emsp;&emsp;&emsp;' + _.title, time_convert(_.created) + '  '


if __name__ == '__main__':
    main()
