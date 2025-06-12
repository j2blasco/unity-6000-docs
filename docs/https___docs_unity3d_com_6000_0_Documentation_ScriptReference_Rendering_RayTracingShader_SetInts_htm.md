* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.SetInts.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).SetInts
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
public void SetInts(string name, params int[] values); 
## Declaration
public void SetInts(int nameID, params int[] values); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property being set.  
nameID | The ID of the property as given by Shader.PropertyToID.  
values | The int array to set.  
### Description
Sets the values for a int array uniform.
* * *
