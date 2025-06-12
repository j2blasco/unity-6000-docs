* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent.html

# IPointerEvent
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
This interface describes properties available to pointer events. 
### Properties
Property | Description  
---|---  
[actionKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-actionKey.html) |  Gets a boolean value that indicates whether the platform-specific action key is pressed. True means the action key is pressed. False means it isn't.   
[altitudeAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-altitudeAngle.html) |  Gets the angle of the stylus relative to the surface, in radians   
[altKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-altKey.html) |  Gets a boolean value that indicates whether the Alt key is pressed. True means the Alt key is pressed. False means it isn't.   
[azimuthAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-azimuthAngle.html) |  Gets the angle of the stylus relative to the x-axis, in radians.   
[button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-button.html) |  Gets a value that indicates which mouse button was pressed or released (if any) to cause this event: 0 is the left button, 1 is the right button, 2 is the middle button. A negative value indicates that no mouse button changed state during this event.   
[clickCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-clickCount.html) |  Gets the number of times the button was pressed.   
[commandKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-commandKey.html) |  Gets a boolean value that indicates whether the Windows/Cmd key is pressed. True means the Windows/Cmd key is pressed. False means it isn't.   
[ctrlKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-ctrlKey.html) |  Gets a boolean value that indicates whether the Ctrl key is pressed. True means the Ctrl key is pressed. False means it isn't.   
[deltaPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-deltaPosition.html) |  Gets the difference between the pointer's position during the previous mouse event and its position during the current mouse event.   
[deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-deltaTime.html) |  Gets the amount of time that has elapsed since the last recorded change in pointer values, in seconds.   
[isPrimary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-isPrimary.html) |  Gets a boolean value that indicates whether the pointer is a primary pointer. True means the pointer is a primary pointer. False means it isn't.   
[localPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-localPosition.html) |  Gets the pointer position in the current target's coordinate system.   
[modifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-modifiers.html) |  Gets flags that indicate whether modifier keys (Alt, Ctrl, Shift, Windows/Cmd) are pressed.   
[penStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-penStatus.html) |  Specifies the state of the pen. For example, whether the pen is in contact with the screen or tablet, whether the pen is inverted, and whether buttons are pressed. On macOS, penStatus will not reflect changes to button mappings.   
[pointerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-pointerId.html) |  Gets the identifier of the pointer that sends the event.   
[pointerType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-pointerType.html) |  Gets the type of pointer that created the event.   
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-position.html) |  Gets the pointer position in the Screen or World coordinate system.   
[pressedButtons](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-pressedButtons.html) |  Gets a bitmask that describes the buttons that are currently pressed.   
[pressure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-pressure.html) |  Gets the amount of pressure currently applied by a touch.   
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-radius.html) |  Gets an estimate of the radius of a touch.   
[radiusVariance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-radiusVariance.html) |  Gets the accuracy of the touch radius.   
[shiftKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-shiftKey.html) |  Gets a boolean value that indicates whether the Shift key is pressed. True means the Shift key is pressed. False means it isn't.   
[tangentialPressure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-tangentialPressure.html) |  Gets the pressure applied to an additional pressure-sensitive control on the stylus.   
[tilt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-tilt.html) |  Specifies the angle of the pen relative to the X and Y axis respectively, in radians.   
[twist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent-twist.html) |  Gets the rotation of the stylus around its axis, in radians.   
* * *
