* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VRTextureUsage.html

# VRTextureUsage
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
This enum describes how the [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) is used as a VR eye texture. Instead of using the values of this enum manually, use the value returned by [eyeTextureDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-eyeTextureDesc.html) or other VR functions returning a [RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html).
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VRTextureUsage.None.html) | The RenderTexture is not a VR eye texture. No special rendering behavior will occur.  
[OneEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VRTextureUsage.OneEye.html) | This texture corresponds to a single eye on a stereoscopic display.  
[TwoEyes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VRTextureUsage.TwoEyes.html) | This texture corresponds to two eyes on a stereoscopic display. This will be taken into account when using Graphics.Blit and other rendering functions.  
[DeviceSpecific](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VRTextureUsage.DeviceSpecific.html) | The texture used by an external XR provider. The provider is responsible for defining the texture's layout and use.  
* * *
