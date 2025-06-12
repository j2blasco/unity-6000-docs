* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.html

# SkinWeights
enumeration
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
Skin weights.
How many bones affect each vertex. This can be used when accessing the Bone Weight Buffer with [Mesh.GetBoneWeightBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeightBuffer.html) to determine what way the data will be ordered.  
  
Additional resources: [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html), [Mesh.GetBoneWeightBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeightBuffer.html).
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.None.html) | The mesh does not contain any bone weight data.  
[OneBone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.OneBone.html) | One bone affects each vertex. When used to access Mesh.GetBoneWeightBuffer the Bone Weight buffer will contain only indices to the bones, as the weight will be set to 1.   
[TwoBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.TwoBones.html) | Two bones affect each vertex. When used to access Mesh.GetBoneWeightBuffer the Bone Weight buffer will contain two indices and two floats per vertex.  
[FourBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.FourBones.html) | Four bones affect each vertex. When used to access Mesh.GetBoneWeightBuffer the Bone Weight buffer will contain one BoneWeight per vertex.   
[Unlimited](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.Unlimited.html) | An unlimited number of bones affect each vertex.  
* * *
