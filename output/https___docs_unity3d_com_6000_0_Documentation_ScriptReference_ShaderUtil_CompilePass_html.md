* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.CompilePass.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).CompilePass
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
public static void CompilePass([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material, int pass, bool forceSync); 
### Parameters
Parameter | Description  
---|---  
material | Target Material.  
pass | Index of the target Shader pass.  
forceSync | Forces the script execution to wait until the compilation has finished. Optional.  
### Description
Request the Editor to compile the Shader Variant needed for the specific pass of the given Material.
Additional resources: :ref::IsPassCompiled, [allowAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-allowAsyncCompilation.html), [anythingCompiling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-anythingCompiling.html), [SetAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.SetAsyncCompilation.html), [RestoreAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.RestoreAsyncCompilation.html).
* * *
