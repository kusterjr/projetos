#!/usr/bin/python

# Ubuntu Tweak - PyGTK based desktop configure tool
#
# Copyright (C) 2007-2008 TualatriX <tualatrix@gmail.com>
#
# Ubuntu Tweak is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Ubuntu Tweak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ubuntu Tweak; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

import pygtk
pygtk.require("2.0")
import gtk
import os
import gconf
import gettext

from common.systeminfo import module_check
from common.factory import Factory
from common.widgets import HScaleBox, TablePack, TweakPage

class PowerManager(TweakPage):
    """Advanced Powermanager Settings"""
    def __init__(self):
        TweakPage.__init__(self)

        box = TablePack(_("Advanced Power Management Settings"), [
                [Factory.create("gconfcheckbutton", _('Enable "Hibernation"'), "can_hibernate")],
                [Factory.create("gconfcheckbutton", _('Enable "Suspend"'), "can_suspend")],
                [Factory.create("gconfcheckbutton", _('Show "CPU frequency control option" in Power Management Preferences'), "cpufreq_show")],
                [Factory.create("gconfcheckbutton", _("Disable Network Manager when on sleep"), "network_sleep")],
                [Factory.create("gconfcheckbutton", _('Enable "Lock screen" when "Blank Screen" activates'), "blank_screen")],
                [gtk.Label(_('Display "Power Manager" panel item')), Factory.create("gconfcombobox", "icon_policy", [_("Never display"), _("When charging"), _("Always display")], ["never", "charge", "always"])],
        ]) 
        self.pack_start(box, False, False, 0)

        if module_check.get_gnome_version() < 24:
            cpu_policy_text = [_("Normal"), _("On Demand"), _("Power Save"), _("Performance")]
            cpu_policy_value = ["nothing", "ondemand", "powersave", "performance"]
            box = TablePack(_("CPU Policy"), [
                    [gtk.Label(_("The Performance value when on AC power")), Factory.create("gconfscale", 0, 100, "performance_ac", 0)],
                    [gtk.Label(_("The Performance value when on battery power")), Factory.create("gconfscale", 0, 100, "performance_battery", 0)],
                    [gtk.Label(_("The CPU frequency policy when on AC power")), Factory.create("gconfcombobox", "policy_ac", cpu_policy_text, cpu_policy_value)],
                    [gtk.Label(_("The CPU frequency policy when on battery power")), Factory.create("gconfcombobox", "policy_battery", cpu_policy_text, cpu_policy_value)],
            ])
                
            self.pack_start(box, False, False, 0)

if __name__ == "__main__":
    from utility import Test
    Test(PowerManager)