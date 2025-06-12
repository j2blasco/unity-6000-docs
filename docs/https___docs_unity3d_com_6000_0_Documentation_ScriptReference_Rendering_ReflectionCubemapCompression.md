* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionCubemapCompression.Auto.html

#  [ReflectionCubemapCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionCubemapCompression.html).Auto
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
Baked Reflection cubemap will be compressed if compression format is suitable.
Some texture compression formats produce bad wrapping artifacts when used on cubemaps, for example PVRTC. On platforms that use these formats, baked reflection cubemaps will be left uncompressed.
* * *
