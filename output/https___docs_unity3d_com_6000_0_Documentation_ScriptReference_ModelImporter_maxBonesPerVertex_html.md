* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).maxBonesPerVertex
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
maxBonesPerVertex; 
### Description
The maximum number of bones per vertex stored in this mesh data.
Range: 1 - 255, inclusive. Note that higher bone counts may have a performance cost, especially above 4 bones per vertex.  
  
This setting affects the underlying mesh data; vertices with more than this number will have the lowest weighted bones discarded.  
  
You can limit the number of bones that Unity takes into account when performing skinning using the [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html) and [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html) APIs. Note that these settings do not affect the underlying mesh data.  
  
Additional resources: [ModelImporter.minBoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-minBoneWeight.html), [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
* * *
