* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EnableKeyword.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).EnableKeyword
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
public void EnableKeyword(ref [Rendering.GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) keyword); 
## Declaration
public void EnableKeyword([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, ref [Rendering.LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) keyword); 
## Declaration
public void EnableKeyword([ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) computeShader, ref [Rendering.LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) keyword); 
### Parameters
Parameter | Description  
---|---  
keyword | The global or local shader keyword to enable.  
material | The material on which to enable the local shader keyword.  
computeShader | The compute shader for which to enable the local shader keyword.  
### Description
Adds a command to enable a global or local shader keyword.
Shader keywords determine which shader variants Unity uses. For information on working with [local shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DisableKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [Shader.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.DisableKeyword.html), [Material.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html), [ComputeShader.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DisableKeyword.html).
* * *
