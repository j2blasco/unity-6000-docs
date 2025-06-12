* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-renderingPath.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).renderingPath
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
[RenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingPath.html) renderingPath; 
### Description
The rendering path that should be used, if possible.
In some situations, it may not be possible to use the rendering path specified, In this case the renderer automatically uses a different path; for example, if the underlying GPU/platform does not support the requested one, or some other situation causes a fallback.  
  
For this reason, we also provide the read-only property [actualRenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-actualRenderingPath.html), which allows you to discover which path is actually being used.  
  
Additional resources: [actualRenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-actualRenderingPath.html), [RenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingPath.html).
* * *
