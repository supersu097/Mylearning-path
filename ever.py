#!/usr/bin/env python
# coding=utf-8
# Created by sharp.gan at 2016-09-17
from evernote.api.client import EvernoteClient

if __name__ == '__main__':
    #test
    dev_token="S=s1:U=92eb1:E=15e8b9792e9:C=15733e66640:P=1cd:A=en-devtoken:V=2:H=bbea0cf632be1401fb36c2fc07f7556c"
    # Product
    #dev_token="S=s637:U=6f19241:E=15e8c62e846:C=15734b1b908:P=1cd:A=en-devtoken:V=2:H=72d4eade0975e052eba0532f8a4210a2"
    client = EvernoteClient(token=dev_token)
    # userStore = client.get_user_store()
    # user = userStore.getUser()
    # print user.username
    noteStore = client.get_note_store()
    notebooks = noteStore.listNotebooks()
    for n in notebooks:
       print n.name
