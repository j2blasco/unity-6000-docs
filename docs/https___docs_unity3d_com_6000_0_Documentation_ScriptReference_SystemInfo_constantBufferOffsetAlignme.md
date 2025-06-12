* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-constantBufferOffsetAlignment.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).constantBufferOffsetAlignment
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
constantBufferOffsetAlignment; 
### Description
Minimum buffer offset (in bytes) when binding a constant buffer using Shader.SetConstantBuffer or [Material.SetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetConstantBuffer.html).
If the currently active renderer supports binding constant buffers directly (see [SystemInfo.supportsSetConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsSetConstantBuffer.html)), and supports binding constant buffers with an offset, this property specifies the minimum required alignment in bytes for the offset parameter given to Shader.SetConstantBuffer etc. If this property is 0, the current renderer only supports binding constant buffers at offset 0 (for example, DX11 devices that do not expose DX11.1 features).
* * *
