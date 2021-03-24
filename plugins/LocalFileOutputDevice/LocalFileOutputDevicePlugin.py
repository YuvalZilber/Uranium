# Copyright (c) 2018 Ultimaker B.V.
# Uranium is released under the terms of the LGPLv3 or higher.

from UM.Qt.QtApplication import QtApplication
from UM.OutputDevice.OutputDevicePlugin import OutputDevicePlugin
from UM.i18n import i18nCatalog
from .LocalFileOutputDevice import LocalFileOutputDevice

catalog = i18nCatalog("uranium")


class LocalFileOutputDevicePlugin(OutputDevicePlugin):
    """Implements an OutputDevicePlugin that provides a single instance of LocalFileOutputDevice"""

    def __init__(self):
        super().__init__()

        QtApplication.getInstance().getPreferences().addPreference("local_file/last_used_type", "")
        QtApplication.getInstance().getPreferences().addPreference("local_file/dialog_save_path", "")

    def start(self):
        self.getOutputDeviceManager().addProjectOutputDevice(LocalFileOutputDevice(add_to_output_devices = True, parent = QtApplication.getInstance()))

    def stop(self):
        self.getOutputDeviceManager().removeProjectOutputDevice("local_file")