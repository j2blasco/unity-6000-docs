* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FoveatedRenderingCaps.html

# FoveatedRenderingCaps
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
Capabilities of the foveated rendering implementation.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FoveatedRenderingCaps.None.html) | Foveated rendering is not supported.  
[FoveationImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FoveatedRenderingCaps.FoveationImage.html) | The platform can use a foveation image to control the shading rate per tile in screen-space.  
[NonUniformRaster](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FoveatedRenderingCaps.NonUniformRaster.html) | The platform can use non-uniform rasterization to redistribute the resolution density.  
[ModeChangeOnlyBeforeRenderTargetSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FoveatedRenderingCaps.ModeChangeOnlyBeforeRenderTargetSet.html) | The platform requires that the mode change (enable/disable) to be done before changing render target. If this flag is not set the mode can be changed every drawcall.  
* * *
