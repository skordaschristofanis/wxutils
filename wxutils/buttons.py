import wx

from typing import Callable, Optional

class Button(wx.Button):
    """Simple button with bound action
    b = Button(parent, label, action=None, **kws)

    """
    def __init__(self, parent: wx.Window, label: str, action: Optional[Callable] = None, **kws) -> None:
        super(Button, self).__init__(parent=parent, label=label, **kws)
        if action is not None:
            self.SetAction(action)

    def SetAction(self, action: Callable) -> None:
        self.Bind(wx.EVT_BUTTON, handler=action)

    def RemoveAction(self, action: Callable) -> None:
        self.Unbind(wx.EVT_BUTTON, handler=action)


class BitmapButton(wx.BitmapButton):
    def __init__(
        self, parent: wx.Window, bmp: wx.Bitmap, action: Optional[Callable] = None, tooltip: Optional[str] = None, size: tuple[int, int] = (20, 20), **kws
    ) -> None:
        bitmap_arg = wx.BitmapBundle.FromBitmap(bmp) if isinstance(bmp, wx.Bitmap) else bmp
        super(BitmapButton, self).__init__(parent=parent, id=-1, bitmap=bitmap_arg, size=wx.Size(size[0], size[1]), **kws)

        if action is not None:
            self.SetAction(action)
        if tooltip is not None:
            self.SetToolTip(tooltip)

    def SetAction(self, action: Callable) -> None:
        self.Bind(wx.EVT_BUTTON, handler=action)

    def RemoveAction(self, action: Callable) -> None:
        self.Unbind(wx.EVT_BUTTON, handler=action)


def ToggleButton(parent, label, action=None, tooltip=None,
                 size=(25, 25), **kws):
    b = wx.ToggleButton(parent, -1, label, size=size, **kws)
    if action is not None:
        b.Bind(wx.EVT_TOGGLEBUTTON, action)
    if tooltip is not None:
        b.SetToolTip(tooltip)
    return b
