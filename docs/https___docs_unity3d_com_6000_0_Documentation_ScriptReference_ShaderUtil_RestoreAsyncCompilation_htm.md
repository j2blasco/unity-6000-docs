* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.RestoreAsyncCompilation.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).RestoreAsyncCompilation
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
public static void RestoreAsyncCompilation([Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) cmd); 
### Parameters
Parameter | Description  
---|---  
cmd | Target CommandBuffer.  
### Description
Restores the previous Shader compilation mode in this CommandBuffer scope.
The Editor compiles Shader Variants on-demand, the first time rendering requires a particular Shader Variant. By default, asynchronous Shader compilation is only enabled for requests that originate from the Game View or Scene View. With [SetAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.SetAsyncCompilation.html), you can add commands to the [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) that control the Shader compilation during the execution of the buffer. With this method, _RestoreAsyncCompilation_ , you can restore the previous compilation mode.  
  
Additional resources: [SetAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.SetAsyncCompilation.html), [allowAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-allowAsyncCompilation.html), [anythingCompiling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-anythingCompiling.html), [IsPassCompiled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.IsPassCompiled.html), [CompilePass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.CompilePass.html).
* * *
