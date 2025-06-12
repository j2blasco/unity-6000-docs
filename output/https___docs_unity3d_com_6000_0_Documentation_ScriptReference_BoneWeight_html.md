* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html

# BoneWeight
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Describes 4 skinning bone weights that affect a vertex in a mesh.
Elements in this struct must be in descending order of weight value. The sum of all weight values must be 1. If a vertex is affected by fewer than 4 bones, each of the remaining weight values must be 0.  
  
Note that this struct, and the associated [Mesh.boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html) and [Mesh.GetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html) APIs, describe exactly 4 bone weights per vertex. The newer [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) struct describes a single bone weight, and it can be used with the associated [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html) and [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html) APIs to describe up to 255 bone weights per vertex. It is preferable to use [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) and its associated APIs; they offer more flexibility, and might result in small performance benefits as Unity does not have to perform unnessary conversion operations.  
  
Additional resources: [Mesh.boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html), [Mesh.GetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html), [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html), [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html), [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
### Properties
Property | Description  
---|---  
[boneIndex0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight-boneIndex0.html) | Index of first bone.  
[boneIndex1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight-boneIndex1.html) | Index of second bone.  
[boneIndex2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight-boneIndex2.html) | Index of third bone.  
[boneIndex3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight-boneIndex3.html) | Index of fourth bone.  
[weight0](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight-weight0.html) | Skinning weight for first bone.  
[weight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight-weight1.html) | Skinning weight for second bone.  
[weight2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight-weight2.html) | Skinning weight for third bone.  
[weight3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight-weight3.html) | Skinning weight for fourth bone.  
* * *
