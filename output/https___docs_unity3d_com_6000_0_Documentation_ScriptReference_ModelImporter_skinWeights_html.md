* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-skinWeights.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).skinWeights
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
[ModelImporterSkinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterSkinWeights.html) skinWeights; 
### Description
Skin weights import options.
To import more than 4 bone weights per vertex, set this property to [ModelImporterSkinWeights.Custom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterSkinWeights.Custom.html) and set [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html) to the required number. You may also limit the number of bones to less than 4, or set a threshold for the weights via [ModelImporter.minBoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-minBoneWeight.html).  
  
Note that [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html) and [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html) can limit the number of bone weights that Unity uses for skinning. Ensure that these values are set to Auto, if you want to use more than 4 bone weights per vertex.  
  
Additional resources: [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html), [ModelImporter.minBoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-minBoneWeight.html),[QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html), [SkinnedMeshRenderer.quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer-quality.html).
* * *
