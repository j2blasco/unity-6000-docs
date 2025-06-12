* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html

# BoneWeight1
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
Describes a bone weight that affects a vertex in a mesh.
This struct can be used with the [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html) and [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html) APIs to describe up to 255 bone weights per vertex.  
  
Note that the older [BoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html) struct, and the associated [Mesh.boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html) and [Mesh.GetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html) APIs, describe exactly 4 bone weights per vertex. It is preferable to use [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) and its associated APIs; they offer more flexibility, and might result in small performance benefits as Unity does not have to perform unnecessary conversion operations.  
  
Additional resources: [Mesh.SetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.SetBoneWeights.html), [Mesh.GetAllBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetAllBoneWeights.html), [Mesh.GetBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBonesPerVertex.html), [Mesh.boneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh-boneWeights.html), [Mesh.GetBoneWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeights.html), [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
### Properties
Property | Description  
---|---  
[boneIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1-boneIndex.html) | Index of bone.  
[weight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1-weight.html) | Skinning weight for bone.  
* * *
