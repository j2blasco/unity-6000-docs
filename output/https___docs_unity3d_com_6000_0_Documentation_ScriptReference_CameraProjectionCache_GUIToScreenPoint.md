* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.GUIToScreenPoint.html

#  [CameraProjectionCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.html).GUIToScreenPoint
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
## Declaration
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) GUIToScreenPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint); 
### Parameters
Parameter | Description  
---|---  
guiPoint | A point in GUI space to convert to screen space.  
### Returns
**Vector2** `guiPoint` in screen space relative to the cached camera viewport. 
### Description
Converts a point from GUI position to screen space relative to the cached camera viewport.
See also [GUIUtility.ScreenToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScreenToGUIPoint.html), [GUIUtility.GUIToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenPoint.html).
* * *
