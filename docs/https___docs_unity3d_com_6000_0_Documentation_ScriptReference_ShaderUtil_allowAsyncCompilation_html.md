* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-allowAsyncCompilation.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).allowAsyncCompilation
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
allowAsyncCompilation; 
### Description
When true, asynchronous Shader compilation is allowed at the current call site.
The Editor compiles Shader Variants on-demand, the first time rendering requires a particular Shader Variant. By default, asynchronous Shader compilation is only enabled for requests that originate from the Game View or Scene View. With this property, you can control the compilation more precisely. For example, you can allow asynchronous compilation for custom Editor tools. You can also force synchronous compilation on parts of rendering where asynchronous compilation would be used by default. This property takes effect immediately. For [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) based control, see [SetAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.SetAsyncCompilation.html).  
  
Additional resources: [SetAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.SetAsyncCompilation.html), [RestoreAsyncCompilation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.RestoreAsyncCompilation.html), [anythingCompiling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-anythingCompiling.html), [IsPassCompiled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.IsPassCompiled.html), [CompilePass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.CompilePass.html).
* * *
