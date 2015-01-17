# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('cali')

from cali_lib import Window
from cali.AboutCaliDialog import AboutCaliDialog
from cali.PreferencesCaliDialog import PreferencesCaliDialog
import sync as capi

# See cali_lib.Window.py for more details about how this class works
class CaliWindow(Window):
    __gtype_name__ = "CaliWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(CaliWindow, self).finish_initializing(builder)
        # action_group = Gtk.ActionGroup("my_actions")
        callenderTarget=capi.CalenderAPI()
        capi.CalenderAPI.get_events(callenderTarget)

        self.AboutDialog = AboutCaliDialog
        self.PreferencesDialog = PreferencesCaliDialog

        self.calendar = self.builder.get_object('calendar')
        self.weekly_listbox = self.builder.get_object('weekly_listbox')
        # self.add_sync_menu_actions(action_group)
        # self.weekly_listbox.insert('test',-1)

        self.sync = self.builder.get_object('btnSync')
        # Code for other initialization actions should be added here.

    def on_calendar_day_selected(self,widget):
        print(widget.get_date())

    def on_sync_clicked(self,widget):
         print("You clicked sync")