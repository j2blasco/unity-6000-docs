* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-isValid.html

#  [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html).isValid
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
isValid; 
### Description
Specifies whether this local shader keyword is valid (Read Only).
A local shader keyword is invalid if: 
  * It doesn't exist in the [local keyword space](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.html) of the shader or compute shader you pass into the constructor.
  * If Unity can't find it when you call [LocalKeywordSpace.FindKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.FindKeyword.html).


If you use an invalid local shader keyword as an argument for [Material.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html), [Material.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html), [ComputeShader.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.EnableKeyword.html), or [ComputeShader.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DisableKeyword.html), it has no effect. If you use an invalid local shader keyword as an argument for [Material.IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsKeywordEnabled.html) or [ComputeShader.IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsKeywordEnabled.html), these functions return `false`.  
  
Additional resources: [LocalKeywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.html), [Material.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.EnableKeyword.html), [Material.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.DisableKeyword.html), [ComputeShader.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.EnableKeyword.html), [ComputeShader.DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.DisableKeyword.html), [Material.IsKeywordEnabled]], [ComputeShader.IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.IsKeywordEnabled.html).
* * *
