* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBindposes.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetBindposes
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html "Go to Mesh Component in the Manual")
## Declaration
public NativeArray<Matrix4x4> GetBindposes(); 
### Returns
**NativeArray <Matrix4x4>** The array of bind poses belonging to the Mesh. 
### Description
Gets the bind poses of the Mesh.
The bind pose at each index corresponds to the bone with the same index. Additional resources: [SkinnedMeshRenderer.bones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-bones.html).
* * *
## Declaration
public void GetBindposes(List<Matrix4x4> bindposes); 
### Parameters
Parameter | Description  
---|---  
bindposes | A list of bind poses to populate.  
### Description
Gets the bind poses of the Mesh.
The bind pose at each index corresponds to the bone with the same index. Additional resources: [SkinnedMeshRenderer.bones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-bones.html).  
  
Use this method instead of [bindposes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-bindposes.html) if you control the life cycle of the list passed in and you want to avoid allocating a new array with every access.
* * *
