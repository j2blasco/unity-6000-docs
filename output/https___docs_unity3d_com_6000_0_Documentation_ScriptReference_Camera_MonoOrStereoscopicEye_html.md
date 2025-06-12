* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.html

# MonoOrStereoscopicEye
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
### Description
A Camera eye corresponding to the left or right human eye for stereoscopic rendering, or neither for non-stereoscopic rendering.  
  
A single Camera can render both left and right views in a single frame. Therefore, this enum describes which eye the Camera is currently rendering when returned by [Camera.stereoActiveEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-stereoActiveEye.html) during a rendering callback (such as [Camera.OnRenderImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnRenderImage.html)), or which eye to act on when passed into a function.  
  
The default value is [Camera.MonoOrStereoscopicEye.Left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Left.html), so [Camera.MonoOrStereoscopicEye.Left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Left.html) may be returned by some methods or properties when called outside of rendering if stereoscopic rendering is enabled.
### Properties
Property | Description  
---|---  
[Left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Left.html) | Camera eye corresponding to stereoscopic rendering of the left eye.  
[Right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Right.html) | Camera eye corresponding to stereoscopic rendering of the right eye.  
[Mono](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.MonoOrStereoscopicEye.Mono.html) | Camera eye corresponding to non-stereoscopic rendering.  
* * *
