* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-clearStencilAfterLightingPass.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).clearStencilAfterLightingPass
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
clearStencilAfterLightingPass; 
### Description
Should the camera clear the stencil buffer after the deferred light pass?
When using Deferred Shading, the G-buffer and lighting passes use the stencil buffer. By default contents of the stencil buffer are preserved (not cleared) and end up containing information related to lights. Setting this property to `true` makes stencil be cleared to zero after the deferred light pass is done.  
  
Typically if you're using deferred shading camera and UI elements with Masks (see UI.Mask), you'll want the stencil buffer to be cleared.
* * *
