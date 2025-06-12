* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html

# LocalKeyword
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
Represents a shader keyword declared in a shader source file.
Shader keywords determine which shader variants Unity uses. You can use a `LocalKeyword` to enable, disable, or check the state of a **local** shader keyword. For information on working with local shader keywords and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
When you declare a shader keyword in the source file for a [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), Unity represents the keyword with a `LocalKeyword` and stores it in a [LocalKeywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.html).  
  
For a [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html): 
  * To set the state of a local shader keyword, use [Material.SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetKeyword.html), [Material.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html), or [Material.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html).
  * To check the state of a local shader keyword, use [Material.IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsKeywordEnabled.html) or [Material.enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-enabledKeywords.html).
  * To access the `LocalKeywordSpace`, use [Material.shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-shader.html) to access the [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) that the material uses, and then use [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html).


For a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html): 
  * To set the state of a local shader keyword, use [ComputeShader.SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.SetKeyword.html), [ComputeShader.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.EnableKeyword.html), or [ComputeShader.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DisableKeyword.html).
  * To check the state of a local shader keyword, use [ComputeShader.IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsKeywordEnabled.html) or [ComputeShader.enabledKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-enabledKeywords.html).
  * To access the `LocalKeywordSpace`, use [ComputeShader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-keywordSpace.html).


In addition to this, you can also enable or disable a local or global keyword with a `CommandBuffer`. To do this, use [CommandBuffer.SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetKeyword.html), [CommandBuffer.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EnableKeyword.html), or [CommandBuffer.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DisableKeyword.html).  
  
**Note:** A `LocalKeyword` is specific to a single [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) instance. You cannot use it with other [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) instances, even if they declare keywords with the same `name`.  
  
Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html).
### Properties
Property | Description  
---|---  
[isDynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-isDynamic.html) | Specifies whether this local shader keyword is used for dynamic branching (Read Only).  
[isOverridable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-isOverridable.html) | Whether this local shader keyword can be overridden by a global shader keyword. (Read Only).  
[isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-isValid.html) | Specifies whether this local shader keyword is valid (Read Only).  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-name.html) | The name of the shader keyword (Read Only).  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-type.html) | The type of the shader keyword (Read Only).  
### Constructors
Constructor | Description  
---|---  
[LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-ctor.html) | Initializes and returns a LocalKeyword struct that represents an existing local shader keyword for a given Shader.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-operator_ne.html) | Returns true if the shader keywords are not the same. Otherwise, returns false.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-operator_eq.html) | Returns true if the shader keywords are the same. Otherwise, returns false.  
* * *
