* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CameraCallback.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).CameraCallback
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
## Declaration
public delegate void CameraCallback([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam); 
### Description
Delegate type for camera callbacks.
Use this with [Camera.onPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreCull.html), [Camera.onPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreRender.html) or [Camera.onPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html) to get callbacks when any camera does rendering.  
  
Camera that invokes the callback will be passed as the argument.  
  
Additional resources: [onPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreCull.html), [onPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPreRender.html), [onPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html).
* * *
