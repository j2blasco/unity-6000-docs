* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasMatrix.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).HasMatrix
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
## Declaration
public bool HasMatrix(string name); 
## Declaration
public bool HasMatrix(int nameID); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property. Use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get this ID.  
name | The name of the property.  
### Returns
**bool** Returns true if the ShaderLab file assigned to the Material has this property. 
### Description
Checks if the ShaderLab file assigned to the Material has a Matrix property with the given name. This also works with the Matrix Array property.
Additional resources: [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html), [HasProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasProperty.html), [HasFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasFloat.html), [HasTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasTexture.html), [HasBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasBuffer.html), [HasColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasColor.html), [HasConstantBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasConstantBuffer.html), [HasInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasInt.html), [HasVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.HasVector.html).
* * *
