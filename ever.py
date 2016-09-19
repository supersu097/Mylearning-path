#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-09-17
from evernote.api.client import EvernoteClient
import config
if __name__ == '__main__':
    client = EvernoteClient(token=config.dev_token)
    # userStore = client.get_user_store()
    # user = userStore.getUser()
    # print user.username
    noteStore = client.get_note_store()
    notebooks = noteStore.listNotebooks()
    for n in notebooks:
       print n.name
