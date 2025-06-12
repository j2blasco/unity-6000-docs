* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.AfterGBuffer.html

#  [CameraEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.html).AfterGBuffer
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
After deferred rendering G-buffer is rendered.
Will be called immediately after all objects are rendered into G-buffer. The G-buffer render target(s) will be active, however they will not be set up as shader properties yet.  
  
Generally the [BeforeLighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.BeforeLighting.html) event is probably a better place to start doing custom G-buffer modifications.
* * *
