* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EnableShaderKeyword.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).EnableShaderKeyword
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
public void EnableShaderKeyword(string keyword); 
### Parameters
Parameter | Description  
---|---  
keyword | Name of a global shader keyword to enable.  
### Description
Adds a command to enable a global keyword with a given name.
If a global keyword with the name you pass in does not exist, Unity creates one with that name when you call this function. To get all the global keywords that already exist, use [Shader.globalKeywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-globalKeywords.html). Note: it is more efficient to use [EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.EnableKeyword.html).  
  
Additional resources: [DisableShaderKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DisableShaderKeyword.html), [Shader.EnableKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.EnableKeyword.html).
* * *
