* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.SetAsyncCompilation.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).SetAsyncCompilation
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
public static void SetAsyncCompilation([Rendering.CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) cmd, bool allow); 
### Parameters
Parameter | Description  
---|---  
cmd | Target CommandBuffer.  
allow | Is async Shader compilation allowed or not.  
### Description
Adds shader compilation mode command in the CommandBuffer.
The Editor compiles Shader Variants on-demand, the first time rendering requires a particular Shader Variant. By default, asynchronous Shader compilation is only enabled for requests that originate from the Game View or Scene View. With this method, you can add commands to [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) that control the Shader compilation during the execution of the buffer. This lets you disable and enable asynchronous compilation on specific parts of rendering, both for Game View, Scene View and other Views, for example custom tools. To restore the previous compilation mode, see [RestoreAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.RestoreAsyncCompilation.html).  
  
Additional resources: [RestoreAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.RestoreAsyncCompilation.html), [allowAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-allowAsyncCompilation.html), [anythingCompiling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-anythingCompiling.html), [IsPassCompiled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.IsPassCompiled.html), [CompilePass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.CompilePass.html).
* * *
