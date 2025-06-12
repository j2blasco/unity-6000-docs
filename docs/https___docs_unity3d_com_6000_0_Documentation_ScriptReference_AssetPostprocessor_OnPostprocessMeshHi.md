* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessMeshHierarchy.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPostprocessMeshHierarchy(GameObject)
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
### Parameters
Parameter | Description  
---|---  
root | The root GameObject of the imported Asset.  
### Description
This function is called when a new transform hierarchy has finished importing.
The ModelImporter calls this function for every root transform hierarchy in the source model file. This lets you change each root transform hierarchy before other artifacts are imported, such as the avatar or animation clips.  
  
If this function destroys the root hierarchy, any associated animation clips are not imported.
* * *
