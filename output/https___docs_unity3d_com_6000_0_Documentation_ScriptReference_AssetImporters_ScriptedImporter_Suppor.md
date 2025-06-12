* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.SupportsRemappedAssetType.html

#  [ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html).SupportsRemappedAssetType
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
public bool SupportsRemappedAssetType(Type type); 
### Parameters
Parameter | Description  
---|---  
type | The type of asset to check.  
### Returns
**bool** Returns true if the importer supports remapping the given type. Otherwise, returns false. 
### Description
Override this method if your [ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html) supports remapping specific asset types.
A remapped asset must be explicitly handled by the importer. For example, an importer for a file format that supports materials can assign a remapped [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) reference from the external object map directly to the [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) component.  
  
Additional resources: [AssetImporter.GetExternalObjectMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetExternalObjectMap.html).
* * *
