* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unwrapping.GeneratePerTriangleUV.html

#  [Unwrapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unwrapping.html).GeneratePerTriangleUV
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
public static Vector2[] GeneratePerTriangleUV([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) src); 
### Parameters
Parameter | Description  
---|---  
src | The source mesh to generate UVs for.  
### Returns
**Vector2[]** The list of UVs generated. 
### Description
Will generate per-triangle uv (3 UVs for each triangle) with default settings.
You'll need to merge them yourself.
* * *
## Declaration
public static Vector2[] GeneratePerTriangleUV([Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) src, [UnwrapParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnwrapParam.html) settings); 
### Parameters
Parameter | Description  
---|---  
src | The source mesh to generate UVs for.  
settings | Allows you to specify custom parameters to control the unwrapping.  
### Returns
**Vector2[]** The list of UVs generated. 
### Description
Will generate per-triangle uv (3 UVs for each triangle) with provided settings.
You'll need to merge them yourself.
* * *
