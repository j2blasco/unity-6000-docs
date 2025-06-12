* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-scaleOfAllRenderTargets.html

#  [XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html).scaleOfAllRenderTargets
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
scaleOfAllRenderTargets; 
### Description
Controls the size of the textures submitted to the display as a multiplier of the display's default resolution.
A value of 1.0 uses the default texture resolution specified by the display provider. Values less than 1.0 use lower resolution textures, which might improve performance at the expense of a less sharp image. Values greater than 1.0 use higher resolution textures, resulting in a potentially sharper image at a cost to performance and increased memory usage.  
  
When this property changes, textures are always reallocated, which can negatively impact performance. To dynamically change texture resolution on the fly, consider using [XRDisplaySubsystem.scaleOfAllViewports](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem-scaleOfAllViewports.html).
* * *
