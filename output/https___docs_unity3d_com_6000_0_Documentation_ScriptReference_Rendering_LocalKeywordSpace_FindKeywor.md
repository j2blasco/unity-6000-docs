* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.FindKeyword.html

#  [LocalKeywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.html).FindKeyword
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
public [Rendering.LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) FindKeyword(string name); 
### Parameters
Parameter | Description  
---|---  
name | The name of the shader keyword to search for.  
### Returns
**LocalKeyword** Returns a valid [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) if it's present in the keyword space. Otherwise, returns an invalid [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html). 
### Description
Searches for a local shader keyword with a given name in the keyword space.
Use this method to efficiently retrieve a local shader keyword with a given name. The resulting keyword's [LocalKeyword.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-isValid.html) property indicates whether the keyword exists in this local keyword space.  
  
Additional resources: [LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html), [LocalKeyword.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword-isValid.html), [Shader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-keywordSpace.html), [ComputeShader.keywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader-keywordSpace.html).
* * *
