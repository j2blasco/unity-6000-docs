* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.html

# TransparencySortMode
enumeration
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
Transparent object sorting mode of a [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).
By default, perspective cameras sort objects based on distance from camera position to the object center; and orthographic cameras sort based on distance along the view direction.  
  
If you're making a 2D game with a perspective camera, you might want to use [TransparencySortMode.Orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.Orthographic.html) sort mode so that objects are sorted based on distance along the camera's view.  
  
Additional resources: [Camera.transparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortMode.html).
### Properties
Property | Description  
---|---  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.Default.html) | Default transparency sorting mode.  
[Perspective](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.Perspective.html) | Perspective transparency sorting mode.  
[Orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.Orthographic.html) | Orthographic transparency sorting mode.  
[CustomAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.CustomAxis.html) | Sort objects based on distance along a custom axis.  
* * *
