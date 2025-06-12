* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnAssignMaterialModel.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnAssignMaterialModel(Material,Renderer)
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
Feeds a source material.
The returned material will be assigned to the renderer. If you return null, Unity will use its default material finding / generation method to assign a material. The `sourceMaterial` is generated directly from the model before importing and will be destroyed immediately after OnAssignMaterial.  
  

* * *
