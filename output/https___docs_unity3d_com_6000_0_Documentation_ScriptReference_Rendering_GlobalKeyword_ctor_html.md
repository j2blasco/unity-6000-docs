* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword-ctor.html

# GlobalKeyword Constructor
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
public GlobalKeyword(string name); 
### Parameters
Parameter | Description  
---|---  
name | The name of the global shader keyword.  
### Description
Creates and returns a GlobalKeyword struct that represents an existing global shader keyword.
If a global shader keyword with the given name exists in Unity's internal list of global shader keywords, Unity creates and returns a `GlobalKeyword` struct to represent it. Otherwise, Unity still creates a struct, but throws an error.  
  
To add a new global shader keyword to Unity's internal list at the same time as creating a `GlobalKeyword` to represent it, use [GlobalKeyword.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.Create.html) instead.  
  
To get all the global shader keywords that already exist, use [Shader.globalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalKeywords.html).  
  
Additional resources: [Shader variants and keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-and-keywords.html), [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html), [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.EnableKeyword.html), [DisableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.DisableKeyword.html), [SetKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.SetKeyword.html), [IsKeywordEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.IsKeywordEnabled.html), [enabledGlobalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-enabledGlobalKeywords.html), [globalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalKeywords.html).
* * *
