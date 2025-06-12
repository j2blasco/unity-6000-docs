* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.GetConstantBufferOffsetAlignment.html

#  [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html).GetConstantBufferOffsetAlignment
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
## Declaration
public static int GetConstantBufferOffsetAlignment(); 
### Returns
**int** The alignment (in bytes) you should use to offset any data in the Uniform Buffer Object (UBO). 
### Description
The BatchRendererGroup API is different from [SystemInfo.constantBufferOffsetAlignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-constantBufferOffsetAlignment.html) because it uses Universal Buffer Objects (UBOs) in a different way from other rendering paths. This means it requires different size and alignment constraints on GL platforms.
* * *
