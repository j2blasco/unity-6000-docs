* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetMatrixArray.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetMatrixArray
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
public void SetMatrixArray(string name, Matrix4x4[] values); 
## Declaration
public void SetMatrixArray(int nameID, Matrix4x4[] values); 
## Declaration
public void SetMatrixArray(string name, List<Matrix4x4> values); 
## Declaration
public void SetMatrixArray(int nameID, List<Matrix4x4> values); 
### Parameters
Parameter | Description  
---|---  
name | Property name.  
values | Array of values to set.  
nameID | Property name ID, use [Shader.PropertyToID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.PropertyToID.html) to get it.  
### Description
Sets a matrix array property.
Sets a matrix array property on the material. If a matrix array property with the given name already exists, the old value is replaced.  
  
The array length can't be changed once it has been added to the block. If you subsequently try to set a longer array into the same property, the length will be capped to the original length and the extra items you tried to assign will be ignored. If you set a shorter array than the original length, your values will be assigned but the original values will remain for the array elements beyond the length of your new shorter array.  
  
Array parameters are not exposed in the material inspector, nor serialized with the material asset. But they can be set and queried with `SetFloatArray`, `SetColorArray`, `SetVectorArray`, `SetMatrixArray` and the corresponding getters from scripts at runtime.  
  
Additional resources: [GetMatrixArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetMatrixArray.html).
* * *
