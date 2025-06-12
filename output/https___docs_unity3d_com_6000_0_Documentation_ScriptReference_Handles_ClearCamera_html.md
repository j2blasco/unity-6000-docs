* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ClearCamera.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).ClearCamera
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
public static void ClearCamera([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
### Parameters
Parameter | Description  
---|---  
position | Where in the Scene to clear.  
camera | The camera to clear.  
### Description
Clears the camera.
The camera used by the Handle class is cleared before being used. This may happen, for example, before `DrawCamera` is used.
* * *
