* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterSkinWeights.html

# ModelImporterSkinWeights
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
Skin weights options for [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).
In order to import more than 4 skin weights per vertex, set [ModelImporter.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-skinWeights.html) to [ModelImporterSkinWeights.Custom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterSkinWeights.Custom.html) and set [ModelImporter.maxBonesPerVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-maxBonesPerVertex.html) to the required number. You may also limit the number of bones to less than 4, or set a threshold for the weights via [ModelImporter.minBoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-minBoneWeight.html).  
  
Note that you must set [QualitySettings.skinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-skinWeights.html) to Unlimited in order for additional skin weights to be used.
### Properties
Property | Description  
---|---  
[Standard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterSkinWeights.Standard.html) | Import the standard number of bones per vertex (currently 4).  
[Custom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterSkinWeights.Custom.html) | Import a custom number of bones per vertex.  
* * *
