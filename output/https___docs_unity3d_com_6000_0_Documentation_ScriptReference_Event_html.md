* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html

# Event
class in UnityEngine
/
Implemented in:[UnityEngine.IMGUIModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.IMGUIModule.html)
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
A UnityGUI event.
Events correspond to user input (key presses, mouse actions), or are UnityGUI layout or rendering events.  
  
For each event [OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnGUI.html) is called in the scripts; so OnGUI is potentially called multiple times per frame. [Event.current](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html) corresponds to "current" event inside OnGUI call.  
  
Additional resources: [GUI Scripting Guide](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html), [EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html).
### Static Properties
Property | Description  
---|---  
[current](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html) | The current event that's being processed right now.  
### Properties
Property | Description  
---|---  
[alt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-alt.html) | Is Alt/Option key held down? (Read Only)  
[button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-button.html) | Which mouse button was pressed.  
[capsLock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-capsLock.html) | Is Caps Lock on? (Read Only)  
[character](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-character.html) | The character typed.  
[clickCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-clickCount.html) | How many consecutive mouse clicks have we received.  
[command](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-command.html) | Is Command/Windows key held down? (Read Only)  
[commandName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-commandName.html) | The name of an ExecuteCommand or ValidateCommand Event.  
[control](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-control.html) | Is Control key held down? (Read Only)  
[delta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-delta.html) | The relative movement of the mouse compared to last event.  
[displayIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-displayIndex.html) | Index of display that the event belongs to.  
[functionKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-functionKey.html) | Is the current keypress a function key? (Read Only)  
[isKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-isKey.html) | Is this event a keyboard event? (Read Only)  
[isMouse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-isMouse.html) | Is this event a mouse event? (Read Only)  
[keyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-keyCode.html) | The raw key code for keyboard events.  
[modifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-modifiers.html) | Which modifier keys are held down.  
[mousePosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-mousePosition.html) | The mouse position.  
[numeric](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-numeric.html) | Is the current keypress on the numeric keyboard? (Read Only)  
[penStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-penStatus.html) | Specifies the state of the pen. For example, whether the pen is in contact with the screen or tablet, whether the pen is inverted, and whether buttons are pressed.  
[pointerType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-pointerType.html) | The type of pointer that created this event (for example, mouse, touch screen, pen).  
[pressure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-pressure.html) | How hard pen pressure is applied, normalized between 0 (no pressure) and 1 (maximum pressure).  
[shift](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-shift.html) | Is Shift held down? (Read Only)  
[tilt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-tilt.html) | Specifies the angle of the pen relative to the X and Y axes, expressed in radians.  
[twist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-twist.html) | Specifies the rotation of the pen around its axis, expressed in radians. The default value is 0.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-type.html) | The type of event.  
### Public Methods
Method | Description  
---|---  
[GetTypeForControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.GetTypeForControl.html) | Get a filtered event type for a given control ID.  
[Use](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.Use.html) | Use this event.  
### Static Methods
Method | Description  
---|---  
[GetEventCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.GetEventCount.html) | Returns the current number of events that are stored in the event queue.  
[KeyboardEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.KeyboardEvent.html) | Create a keyboard event.  
[PopEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.PopEvent.html) | Get the next queued [Event] from the event system.  
* * *
