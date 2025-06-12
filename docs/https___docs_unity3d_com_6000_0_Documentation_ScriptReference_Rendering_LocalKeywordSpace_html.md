* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.html

# LocalKeywordSpace
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
Represents the local keyword space of a [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).
Shader keywords determine which shader variants Unity uses. For information on working with local shader keywords and [global shader keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) and how they interact, see [Using shader keywords with C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
  
When you declare a [shader keyword](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html) in the source file for a [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) or [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), Unity represents the keyword with a [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) and stores it in a `LocalKeywordSpace`.  
  
For a [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html), access the `LocalKeywordSpace` with [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html). It contains: 
  * All keywords declared in the source file. For more information, see [Declaring shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords#declaring-keywords.html).
  * All keywords declared in dependencies of that source file. This comprises all Shaders that are included via the [Fallback command](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html), and all keywords declared in all Passes that are included via the [UsePass command](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html).
  * All keywords that Unity adds automatically. For more information, see [Unity's predefined shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords#predefined-shader-keywords.html).


For a [ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html), access the `LocalKeywordSpace` with [ComputeShader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-keywordSpace.html). It contains all keywords declared in the source file. For more information, see [Declaring shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords#declaring-keywords.html).  
  
Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [ComputeShader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-keywordSpace.html), [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html).
### Properties
Property | Description  
---|---  
[keywordCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace-keywordCount.html) | The number of local shader keywords in this local keyword space. (Read Only)  
[keywordNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace-keywordNames.html) | An array containing the names of all local shader keywords in this local keyword space. (Read Only)  
[keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace-keywords.html) | An array containing all LocalKeyword structs in this local keyword space. (Read Only)  
### Public Methods
Method | Description  
---|---  
[FindKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.FindKeyword.html) | Searches for a local shader keyword with a given name in the keyword space.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace-operator_ne.html) | Returns true if the local shader keyword spaces are not the same. Otherwise, returns false.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace-operator_eq.html) | Returns true if the local shader keyword spaces are the same. Otherwise, returns false.  
* * *
