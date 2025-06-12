* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html

# GUIUtility
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
Utility class for making new GUI controls.
Unless you are creating your own GUI controls from scratch, you should not use these functions.
### Static Properties
Property | Description  
---|---  
[hasModalWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hasModalWindow.html) | A global property, which is true if a ModalWindow is being displayed, false otherwise.  
[hotControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) | The controlID of the current hot control.  
[keyboardControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-keyboardControl.html) | The controlID of the control that has keyboard focus.  
[systemCopyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-systemCopyBuffer.html) | Get access to the system-wide clipboard.  
### Static Methods
Method | Description  
---|---  
[AlignRectToDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.AlignRectToDevice.html) | Align a local space rectangle to the pixel grid.  
[ExitGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ExitGUI.html) | Puts the GUI in a state that will prevent all subsequent immediate mode GUI functions from evaluating for the remainder of the GUI loop by throwing an ExitGUIException.  
[GetControlID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetControlID.html) | Get a unique ID for a control.  
[GetStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetStateObject.html) | Get a state object from a controlID.  
[GUIToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenPoint.html) | Convert a point from GUI position to screen space.  
[GUIToScreenRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenRect.html) | Convert a rect from GUI position to screen space.  
[QueryStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.QueryStateObject.html) | Get an existing state object from a controlID.  
[RotateAroundPivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.RotateAroundPivot.html) | Helper function to rotate the GUI around a point.  
[ScaleAroundPivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScaleAroundPivot.html) | Helper function to scale the GUI around a point.  
[ScreenToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScreenToGUIPoint.html) | Convert a point from screen space to GUI position.  
[ScreenToGUIRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScreenToGUIRect.html) | Convert a rect from screen space to GUI position.  
* * *
