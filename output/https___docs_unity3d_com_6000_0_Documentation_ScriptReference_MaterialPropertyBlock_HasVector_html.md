* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasVector.html

#  [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).HasVector
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
public bool HasVector(string name); 
## Declaration
public bool HasVector(int nameID); 
### Parameters
Parameter | Description  
---|---  
name | The name of the property.  
nameID | The name ID of the property. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get this ID.  
### Returns
**bool** Returns true if [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) has this property. 
### Description
Checks if [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) has the Vector property with the given name or name ID. This also works with the Vector Array property. To set the property, use [SetVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetVector.html).
Additional resources: [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html), [HasProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasProperty.html), [HasFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasFloat.html), [HasTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasTexture.html), [HasBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasBuffer.html), [HasColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasColor.html), [HasConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasConstantBuffer.html), [HasInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasInt.html), [HasMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.HasMatrix.html).
* * *
