from glue.viewers.common.qt.toolbar import BasicToolbar
from glue.viewers.common.qt.tool import CheckableTool, Tool

from qtpy.QtWidgets import QAction, QComboBox, QSpacerItem


class CyclePreviousTool(Tool):
    def __init__(self, viewer, toolbar=None):
        super(CyclePreviousTool, self).__init__(viewer=viewer)
        self.tool_id = 'mv:previous'
        self.action_text = "Previous"
        self.tool_tip = "Previous source in selection"
        self.shortcut = "P"
        self.checkable = False
        self.toolbar = toolbar

    def activate(self):
        pass


class CycleForwardTool(Tool):
    def __init__(self, viewer, toolbar=None):
        super(CycleForwardTool, self).__init__(viewer=viewer)
        self.tool_id = 'mv:next'
        self.action_text = "Next"
        self.tool_tip = "Next source in selection"
        self.shortcut = "N"
        self.checkable = False
        self.toolbar = toolbar

    def activate(self):
        pass


class MOSViewerToolbar(BasicToolbar):
    def __init__(self, *args, **kwargs):
        super(MOSViewerToolbar, self).__init__(*args, **kwargs)

        # Define the toolbar actions
        self.cycle_previous_action = QAction("Previous", self)
        self.cycle_next_action = QAction("Next", self)

        # Include the dropdown widget
        self.source_select = QComboBox()

        # Add the items to the toolbar
        self.addAction(self.cycle_previous_action)
        self.addWidget(self.source_select)
        self.addAction(self.cycle_next_action)

    def _setup_connections(self):
        pass