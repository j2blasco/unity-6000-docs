* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.html

# MobileTextureSubtarget
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
Compressed texture format for target build platform.
Additional resources: [EditorUserBuildSettings.androidBuildSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings-androidBuildSubtarget.html).
### Properties
Property | Description  
---|---  
[Generic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.Generic.html) | Don't override texture compression.  
[DXT](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.DXT.html) | S3 texture compression. Supported on devices with NVidia Tegra, Vivante and Intel GPUs.  
[PVRTC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.PVRTC.html) | PowerVR texture compression. Available on devices with PowerVR GPU.  
[ETC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.ETC.html) | ETC1 texture compression (or ETC2 for textures with alpha). ETC1 is supported by all devices. ETC2 is available on devices which support OpenGL ES 3.0.  
[ETC2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.ETC2.html) | ETC2 texture compression. Available on devices which support OpenGL ES 3.0.  
[ASTC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.ASTC.html) | ASTC texture compression.  
* * *
