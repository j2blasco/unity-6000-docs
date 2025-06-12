* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.Unlimited.html

#  [SkinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.html).Unlimited
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
An unlimited number of bones affect each vertex.
The count is only limited by the number of bones per vertex in the Mesh, which can be adjusted in its Import Setttings.  
  
When used to access [Mesh.GetBoneWeightBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.GetBoneWeightBuffer.html) the Bone Weight buffer will contain the following data: * Element 0 to (mesh vertex count + 1) contain indices. These indices describe the start and end positions for the data in the rest of the buffer, ordered by mesh vertex. For example, element 0 is the start position of the data for mesh vertex 0; element 1 is the end position of the data for mesh vertex 0 and the start position of the data for mesh vertex 1, and so on. * Element at (mesh vertex count + 1) describes the end position for the data for the final mesh vertex. * After that, the [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) that relate to each mesh vertex are stored contiguously. For example, all the [BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) that relate to mesh vertex 0 are contiguous, followed by all the blend shape vertices that relate to mesh vertex 1, and so on.  
  
Additional resources: [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html).
* * *
