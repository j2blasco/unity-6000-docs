* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html

#  [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html).GetBoneWeights
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
public void GetBoneWeights(List<BoneWeight> boneWeights); 
### Parameters
Parameter | Description  
---|---  
boneWeights | A list of [BoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html) structs to populate.  
### Description
Gets the bone weights for the Mesh.
Use this method instead of [Mesh.boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html) if you want to avoid allocating a new array with every access.  
  
The [BoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html) at each index corresponds to the vertex with the same index if this mesh has bone weights defined. Otherwise the list will be empty.  
  
Note that this property uses [BoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html) structs, which represent exactly 4 bone weights per vertex. The newer [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) struct describes a single bone weight, and it can be used with the associated [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html) and [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html) APIs to describe up to 255 bone weights per vertex. It is preferable to use [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) and its associated APIs; they offer more flexibility, and might result in small performance benefits as Unity does not have to perform unnessary conversion operations.  
  
Additional resources: [Mesh.boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html), [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html), [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html), [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
* * *
