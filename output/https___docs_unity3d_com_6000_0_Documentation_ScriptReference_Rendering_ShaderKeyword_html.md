* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html

# ShaderKeyword
struct in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Represents an identifier for a specific code path in a shader.
Unity now provides the [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) APIs which are more performant than ShaderKeyword. It is best practice to use these APIs instead.  
  
Additional resources: [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [ShaderKeywordSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeywordSet.html), [Shader.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.EnableKeyword.html), [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [Declaring and using shader keywords in HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html).
### Properties
Property | Description  
---|---  
[index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword-index.html) | The index of the shader keyword.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword-name.html) | The name of the shader keyword. (Read Only)  
### Constructors
Constructor | Description  
---|---  
[ShaderKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword-ctor.html) | Initializes a new instance of the ShaderKeyword class from a shader global keyword name.  
### Public Methods
Method | Description  
---|---  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.IsValid.html) | Checks whether the global shader keyword exists.  
### Static Methods
Method | Description  
---|---  
[GetGlobalKeywordType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.GetGlobalKeywordType.html) | Returns the type of global keyword: built-in or user defined.  
[IsKeywordLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.IsKeywordLocal.html) | Returns true if the keyword is local.  
* * *
