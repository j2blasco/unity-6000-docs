* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsSetConstantBuffer.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).supportsSetConstantBuffer
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
supportsSetConstantBuffer; 
### Description
Does the current renderer support binding constant buffers directly? (Read Only)
Methods such as Shader.SetConstantBuffer and [Material.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetConstantBuffer.html) allow overriding all shader parameters that reside in a given constant buffer with a custom GfxBuffer. This property returns true if the currently active renderer supports binding constant buffers. It returns false if the render does not support such bindings.
* * *
