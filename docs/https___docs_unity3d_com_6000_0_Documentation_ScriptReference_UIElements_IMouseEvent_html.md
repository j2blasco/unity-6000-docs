* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent.html

# IMouseEvent
interface in UnityEngine.UIElements
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Interface for mouse events. 
### Properties
Property | Description  
---|---  
[actionKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-actionKey.html) |  Returns true if the platform-specific action key is pressed. This key is Cmd on macOS, and Ctrl on all other platforms.   
[altKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-altKey.html) |  Return true if the Alt key is pressed.   
[button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-button.html) |  A value that indicates which mouse button was pressed or released (if any) to cause this event: 0 is the left button, 1 is the right button, 2 is the middle button. A negative value indicates that no mouse button changed state during this event.   
[clickCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-clickCount.html) |  The number of times the button is pressed.   
[commandKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-commandKey.html) |  Return true if the Windows/Command key is pressed.   
[ctrlKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-ctrlKey.html) |  Return true if the Ctrl key is pressed.   
[localMousePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-localMousePosition.html) |  The mouse position in the current target coordinate system.   
[modifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-modifiers.html) |  Flag set holding the pressed modifier keys (Alt, Ctrl, Shift, Windows/Command).   
[mouseDelta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-mouseDelta.html) |  Mouse position difference between the last mouse event and this one.   
[mousePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-mousePosition.html) |  The mouse position in the panel coordinate system.   
[pressedButtons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-pressedButtons.html) |  A bitmask that describes the currently pressed buttons.   
[shiftKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent-shiftKey.html) |  Return true if the Shift key is pressed.   
* * *
