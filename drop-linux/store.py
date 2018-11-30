# author: https://github.com/ddesmond/clarisse-drop
# clarisse user forums
# importing modules
import os
import clipboard as cb

from cryptography.fernet import Fernet

import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson import json_util
import ctypes

ix.application.copy()

#windows paster

def get_clipboard_data():
	set_paste = cb.paste()
    return set_paste

print os.getcwd()


#change path to key
path_to_keyfile = r'drop\keyfile.key'

if os.path.isfile(path_to_keyfile):
    print "-------------------------------------------------------"
    print "keyfile is OK"
    f = open(path_to_keyfile, 'r')
    key_store = f.readline()
    print "-------------------------------------------------------"
else:
    print "-------------------------------------------------------"
    print "no keys"
    key_store = ''




shop = 'shop'
container = ''

#SET EMAIL USER HERE
drop_user = 'test@devtest.com'


shop_name = 'Test copy'
shop_category = 'network'


#CHANGE IF YOU HAVE YOUR OWN MONGO
#database and shop vars
connection = pymongo.MongoClient('ds115244.mlab.com', 15244)
db = connection['cl']
db.authenticate('developer', 'd3v3loper')
api_id = ''
db = db.shop



#data
pname = ''
setup = {}


#functions
def store_data(stdata):
    db.insert_one(stdata)
    return

def copy_clipboard():
    setcopy = ix.application.copy()
    container = cb.paste()
    return container

def block_store_create(container,pname):
    getdata = container
    store_data(getdata)
    ix.log_info(getdata)
    return


#events and GUI
class EventRewire(ix.api.EventObject):
    def cancel(self, sender, evtid):
        ix.log_info("Canceled")
        window.hide()
        #self.kill_window

class run_button(ix.api.GuiPushButton):
    def __init__(self, parent, x, y, w, h, label):
        ix.api.GuiPushButton.__init__(self, parent, x, y, w, h, label)
        self.connect(self, 'EVT_ID_PUSH_BUTTON_CLICK', self.on_click)


    def on_click(self, sender, evtid):
        print setup
        name = nameedit.get_text()
        cmnts = cmntsedit.get_text()
        #print datasample
        print "keystore is: ",key_store
        sample = get_clipboard_data()
        print sample
        suite=Fernet(key_store)
        token = suite.encrypt(sample.encode('utf-8'))
        print "enc:",token
        print ""
        data_sample={

            "store_name" : name,
            "usersubmitted" : drop_user,
            "container_data" : token,
            "comments" : cmnts,
            "category" : setup['set_cat']
         }
        block_store_create(data_sample,pname)


        window.hide()
        #self.kill_window


class itemname(ix.api.GuiLineEdit):
    def __init__(self, parent, x, y, w, h,label):
        ix.api.GuiLineEdit.__init__(self, parent, x, y, w, h, label)
        self.connect(self, 'EVT_ID_LINE_EDIT_CHANGED', self.enter_text)

    def enter_text(self, sender, evtid):
        #setup['set_name'] = self.get_text()
        ix.log_info(self.get_text())



class list_cats(ix.api.GuiListButton):
    def __init__(self, parent, x, y, w, h):
        ix.api.GuiListButton.__init__(self, parent, x, y, w, h)
        self.connect(self, 'EVT_ID_LIST_BUTTON_SELECT', self.on_select)
        self.connect(self, 'EVT_ID_LIST_BUTTON_SELECT_UNCHANGED', self.on_select_unchanged)

        #Fill the list
        self.add_item("GEO") #add_item('the_name_of_your_item')
        self.add_item("CAM") #add_item('the_name_of_your_item')
        self.add_item("TEX") #add_item('the_name_of_your_item')
        self.add_item("NETWORK") #add_item('the_name_of_your_item')
        self.add_item("MISC") #add_item('the_name_of_your_item')
        setup['set_cat'] = self.get_selected_item_name()#refresh result


    def on_select(self, sender, evtid):
        setup['set_cat'] = self.get_selected_item_name()#refresh result
        print setup['set_cat']
        return self.get_selected_item_name()

    def on_select_unchanged(self, sender, evtid):
        setup['set_cat'] = self.get_selected_item_name()#refresh result
        return self.get_selected_item_name()



#setup = {}
#--------------- START NEEDED CODE TO MAKE WINDOW WORK-----------------
clarisse_win = ix.application.get_event_window()
window = ix.api.GuiWindow(clarisse_win, 600, 150, 320, 280) #Parent, X position, Y position, Width, Height
window.set_title('Save selection') #Window name

#Main widget
panel = ix.api.GuiPanel(window, 0, 0, window.get_width(), window.get_height())
panel.set_constraints(ix.api.GuiWidget.CONSTRAINT_LEFT, ix.api.GuiWidget.CONSTRAINT_TOP, ix.api.GuiWidget.CONSTRAINT_RIGHT, ix.api.GuiWidget.CONSTRAINT_BOTTOM)

#--------------- END NEEDED CODE TO MAKE WINDOW WORK-----------------


nameedit = itemname(panel, 10, 20, 160, 20, "Set Name")
cmntsedit = itemname(panel, 10, 100, 220, 20, "Comments")
tex_listLabel = ix.api.GuiLabel(panel, 10, 60, 140, 22, "Select Type: ") #Clarrisse_function(parent, X_position, Y_position, Width, Height, "label")
list_tex = list_cats(panel, 140, 60, 160, 22) #Make an object of your class with the param inside __init__(parent, X, Y, Width, Height)


cancelBtn = ix.api.GuiPushButton(panel, 10, 240, 100, 22, "Cancel") #The cancel button (destroy the script window)


runBtn = run_button(panel, 130, 240, 100, 22, "Run") # The run button to run your script



#Connect to function
event_rewire = EventRewire() #init the class
event_rewire.connect(cancelBtn, 'EVT_ID_PUSH_BUTTON_CLICK', event_rewire.cancel)


#--------------- START NEEDED CODE TO MAKE WINDOW WORK-----------------
#Send all info to clarisse to generate window
window.show()
while window.is_shown(): ix.application.check_for_events()
window.destroy()
#--------------- END NEEDED CODE TO MAKE WINDOW WORK-----------------