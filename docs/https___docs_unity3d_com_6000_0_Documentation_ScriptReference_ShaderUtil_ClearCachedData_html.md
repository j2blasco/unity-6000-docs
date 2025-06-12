* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.ClearCachedData.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).ClearCachedData
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
public static void ClearCachedData([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) s); 
### Description
Clears all internally-cached data that was generated for the given shader, such as errors and compilation info.
This happens automatically on import for shader assets but should be called for programmatically-generated shaders to clear old data before calling [UpdateShaderAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.UpdateShaderAsset.html).
* * *
