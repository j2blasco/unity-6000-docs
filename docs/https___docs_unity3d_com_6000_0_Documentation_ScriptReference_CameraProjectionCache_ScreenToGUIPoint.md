* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.ScreenToGUIPoint.html

#  [CameraProjectionCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.html).ScreenToGUIPoint
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
public [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ScreenToGUIPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) screenPoint); 
### Parameters
Parameter | Description  
---|---  
screenPoint | A point in screen space.  
### Returns
**Vector2** `screenPoint` converted to GUI space relative to the cached camera viewport. 
### Description
Converts a point from screen space to GUI position relative to the viewport at the time the [CameraProjectionCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.html) was created.
The screen space y coordinate varies from zero at the top edge of the window to a maximum at the bottom edge of the window.
* * *
