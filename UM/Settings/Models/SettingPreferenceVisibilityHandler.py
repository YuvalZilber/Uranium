# Copyright (c) 2021 Ultimaker B.V.
# Uranium is released under the terms of the LGPLv3 or higher.

from typing import Optional, TYPE_CHECKING

from UM.Application import Application

from . import SettingVisibilityHandler

if TYPE_CHECKING:
    from PyQt5.QtCore import QObject

class SettingPreferenceVisibilityHandler(SettingVisibilityHandler.SettingVisibilityHandler):
    def __init__(self, parent: Optional["QObject"] = None, *args, **kwargs):
        super().__init__(parent = parent, *args, **kwargs)

        Application.getInstance().getPreferences().preferenceChanged.connect(self._onPreferencesChanged)
        self._onPreferencesChanged("general/visible_settings")

        self.visibilityChanged.connect(self._onVisibilityChanged)

    def _onPreferencesChanged(self, name):
        if name != "general/visible_settings":
            return

        new_visible = set()
        visibility_string = Application.getInstance().getPreferences().getValue("general/visible_settings")
        if visibility_string is None:
            return
        for key in visibility_string.split(";"):
            new_visible.add(key.strip())

        self.setVisible(new_visible)

    def _onVisibilityChanged(self):
        preference = ";".join(self.getVisible())
        Application.getInstance().getPreferences().setValue("general/visible_settings", preference)
