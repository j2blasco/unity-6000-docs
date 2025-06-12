* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.html

# CameraProjectionCache
struct in UnityEditor
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
Project points from world to screen space.
Projection from world to screen space depends on internal camera matrices that Unity must recalculate whenever they are accessed. When accessed in a loop where the camera state does not change, these calculations are not necessary, which results in significant performance improvements.
### Constructors
Constructor | Description  
---|---  
[CameraProjectionCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache-ctor.html) | Creates a CameraProjectionCache with the camera's current state.  
### Public Methods
Method | Description  
---|---  
[GUIToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.GUIToScreenPoint.html) | Converts a point from GUI position to screen space relative to the cached camera viewport.  
[ScreenToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.ScreenToGUIPoint.html) | Converts a point from screen space to GUI position relative to the viewport at the time the CameraProjectionCache was created.  
[WorldToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.WorldToGUIPoint.html) | Converts a world space point to a 2D GUI position.  
[WorldToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.WorldToScreenPoint.html) | Transforms position from world space into screen space using the cached camera projection and viewport.  
* * *
