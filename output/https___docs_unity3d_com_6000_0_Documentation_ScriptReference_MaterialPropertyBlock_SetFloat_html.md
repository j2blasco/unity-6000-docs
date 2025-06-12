* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetFloat.html

#  [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).SetFloat
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
public void SetFloat(string name, float value); 
## Declaration
public void SetFloat(int nameID, float value); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property.  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
value | The float value to set.  
### Description
Set a float property.
Adds a property to the block. If a float property with the given name already exists, the old value is replaced.  
  
Additional resources: [SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetColor.html), [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetVector.html), [SetMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetMatrix.html), [SetTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetTexture.html).
* * *
