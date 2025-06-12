* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.AllowVerticalFlip.html

#  [RenderTextureCreationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.html).AllowVerticalFlip
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
Clear this flag when a RenderTexture is a VR eye texture and the device does not automatically flip the texture when being displayed. This is platform specific and It is set by default. This flag is only cleared when part of a RenderTextureDesc that is returned from GetDefaultVREyeTextureDesc or other VR functions that return a RenderTextureDesc. Currently, only Hololens eye textures need to clear this flag.
* * *
