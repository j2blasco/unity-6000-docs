* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.CreateDefaultMaskForClip.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).CreateDefaultMaskForClip
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
## Declaration
public void CreateDefaultMaskForClip([ModelImporterClipAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterClipAnimation.html) clip); 
### Parameters
Parameter | Description  
---|---  
clip | Clip to which the mask will be applied.  
### Description
Creates a mask that matches the model hierarchy, and applies it to the provided [ModelImporterClipAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterClipAnimation.html).
When writing an [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html), use this method with your created clips to apply a mask that matches the transform hierarchy in the [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).
* * *
