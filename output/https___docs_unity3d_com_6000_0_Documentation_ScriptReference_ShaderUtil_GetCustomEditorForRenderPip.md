* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetCustomEditorForRenderPipeline.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).GetCustomEditorForRenderPipeline
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
public static string GetCustomEditorForRenderPipeline([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, Type renderPipelineType); 
## Declaration
public static string GetCustomEditorForRenderPipeline([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader, string renderPipelineType); 
### Parameters
Parameter | Description  
---|---  
renderPipelineType | The render pipeline asset type.  
shader | The shader to check against.  
### Returns
**string** Returns the full class name of the custom editor. 
### Description
Gets the shader's custom editor class name for a specific render pipeline asset type.
* * *
