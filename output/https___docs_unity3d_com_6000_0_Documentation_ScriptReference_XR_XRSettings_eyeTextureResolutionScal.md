* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-eyeTextureResolutionScale.html

#  [XRSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings.html).eyeTextureResolutionScale
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
eyeTextureResolutionScale; 
### Description
Controls the actual size of eye textures as a multiplier of the device's default resolution.
A value of 1.0 will use the default eye texture resolution specified by the XR device. Values less than 1.0 will use lower resolution eye textures, which may improve performance at the expense of a less sharp image. Values greater than 1.0 will use higher resolution eye textures, resulting in a potentially sharper image at a cost to performance and increased memory usage.  
  
When this property is changed, eye textures are always reallocated, which can be an expensive operation. For dynamically changing eye render resolution on the fly, consider using [XRSettings.renderViewportScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-renderViewportScale.html) instead.
* * *
