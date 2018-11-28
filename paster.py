# author: https://github.com/ddesmond/clarisse-drop
# importing module
import os
import clipboard as cb

from cryptography.fernet import Fernet

import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson import json_util

print os.getcwd()

#edit path to your keyfile
path_to_keyfile = r'PATHTO\keyfile.key'

if os.path.isfile(path_to_keyfile):
    print "-------------------------------------------------------"
    print "keyfile is OK"
    f = open(path_to_keyfile, 'r')
    key_store = f.readline()

    print "-------------------------------------------------------"
else:
    print "-------------------------------------------------------"
    print "no keys"



store_ctx = "project://store"

shop = 'shop'
container = ''


#SET EMAIL/USER HERE
drop_user = 'test@devtest.com'

shop_name = 'Test copy'
shop_category = 'network'

#CHANGE IF YOU HAVE YOUR OWN MONGO
connection = pymongo.MongoClient('ds115244.mlab.com', 15244)
db = connection['cl']
db.authenticate('developer', 'd3v3loper')
db.clarisse = db.shop


def mom_get_ctx():
    sel_ctx = ix.application.get_current_context()
    return sel_ctx

def mom_set_def_ctx():
    try:
        create_import_ctx = ix.get_item(store_ctx)
        print "store is here"
    except:
        create_import_ctx = ix.cmds.CreateContext('store', 'Global', 'project://')
        print "created store"
    return create_import_ctx



def get_all_data():
    try:
        ad = db.clarisse.find({'usersubmitted': drop_user })
        return ad


    except Exception, e:
        print str(e)

def get_data_by_category(cat):
    ad = db.clarisse.find({'category': cat})
    return ad

def get_data_by_id(obj_id):
    ad = db.clarisse.find_one({"_id": ObjectId(obj_id)}).get('container_data')
    return ad

def get_store_by_id(obj_id):
    ad = db.clarisse.find_one({"_id": ObjectId(obj_id)})
    return ad

def get_data_by_name(name):
    return
pastethose = []



class EventRewire(ix.api.EventObject):
    def get_List_Item(self, sender, evtid):
        print sender.get_item_name(sender.get_selected_index())
        return


    def on_select(self, sender, evtid):
        split_vals = sender.get_item_name(sender.get_selected_index())
        objid= split_vals.split()[-1]
        pastethose.append(objid)
        return



#--------------- START NEEDED CODE TO MAKE WINDOW WORK-----------------
clarisse_win = ix.application.get_event_window()
window = ix.api.GuiWindow(clarisse_win, 900, 450, 380, 400) #Parent, X position, Y position, Width, Height
window.set_title('Preset GET') #Window name

#Main widget creation <= this is the correct way to make a GUI, make a default widget and add inside what you want
panel = ix.api.GuiPanel(window, 0, 0, window.get_width(), window.get_height())
panel.set_constraints(ix.api.GuiWidget.CONSTRAINT_LEFT, ix.api.GuiWidget.CONSTRAINT_TOP, ix.api.GuiWidget.CONSTRAINT_RIGHT, ix.api.GuiWidget.CONSTRAINT_BOTTOM)






#--------------- END NEEDED CODE TO MAKE WINDOW WORK-----------------
listView = ix.api.GuiListView(panel, 10, 10, 360, 340)
listView.set_mouse_over_selection(False) #Disable the selection by mouse over


event_rewire = EventRewire() #init the class

list_handle_input_data = []


for data in get_all_data():
    setmeup = (data['store_name'], data['_id'])
    list_handle_input_data.append(setmeup)
    lv = listView.add_item(str(data['store_name'] +" " + str(data['_id'])))

#Connect to function

event_rewire.connect(listView, "EVT_ID_LIST_VIEW_SELECT", event_rewire.get_List_Item)
event_rewire.connect(listView, "EVT_ID_LIST_VIEW_SELECT", event_rewire.on_select)


#--------------- START NEEDED CODE TO MAKE WINDOW WORK-----------------
#Send all info to clarisse to generate window
window.show()
while window.is_shown():    ix.application.check_for_events()
window.destroy()
#--------------- END NEEDED CODE TO MAKE WINDOW WORK-----------------


print "ends"


def paste_me_recipe(numid):
    retrieve_data = get_data_by_id(numid)
    suite=Fernet(key_store)
    print "keystore is: ",key_store
    print "data is ", retrieve_data.decode('utf-8')
    data = str(retrieve_data)
    decrypteddata = suite.decrypt(data)
    set_data = cb.copy(decrypteddata)

    ix.api.SdkHelpers.paste(ix.application)
    print "Imported: ",numid

for each in pastethose:

    paste_me_recipe(each)


