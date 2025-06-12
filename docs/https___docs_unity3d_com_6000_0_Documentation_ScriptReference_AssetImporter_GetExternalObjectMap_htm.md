* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetExternalObjectMap.html

#  [AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html).GetExternalObjectMap
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
public Dictionary<SourceAssetIdentifier,Object> GetExternalObjectMap(); 
### Returns
**Dictionary <SourceAssetIdentifier,Object>** The map between a sub-asset and an external Asset. 
### Description
Gets a copy of the external object map used by the AssetImporter.
Changing the map does not affect the state of the AssetImporter.  
  
Additional resources: [AssetImporter.AddRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.AddRemap.html), [AssetImporter.RemoveRemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.RemoveRemap.html).
* * *
