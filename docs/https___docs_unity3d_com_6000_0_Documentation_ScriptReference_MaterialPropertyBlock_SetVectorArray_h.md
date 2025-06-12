* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetVectorArray.html

#  [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html).SetVectorArray
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
public void SetVectorArray(string name, Vector4[] values); 
## Declaration
public void SetVectorArray(int nameID, Vector4[] values); 
## Declaration
public void SetVectorArray(string name, List<Vector4> values); 
## Declaration
public void SetVectorArray(int nameID, List<Vector4> values); 
### Parameters
Parameter | Description  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html).  
values | The array to set.  
name | The name of the property.  
### Description
Set a vector array property.
Adds a vector array property to the block. If a vector array property with the given name already exists, the old value is replaced.  
  
The array length can't be changed once it has been added to the block. If you subsequently try to set a longer array into the same property, the length will be capped to the original length and the extra items you tried to assign will be ignored. If you set a shorter array than the original length, your values will be assigned but the original values will remain for the array elements beyond the length of your new shorter array.  
  
Additional resources: [SetFloatArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetFloatArray.html), [SetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.SetMatrixArray.html).
* * *
