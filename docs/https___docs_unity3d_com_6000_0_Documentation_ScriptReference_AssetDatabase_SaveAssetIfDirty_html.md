* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssetIfDirty.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).SaveAssetIfDirty
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
public static void SaveAssetIfDirty([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj); 
## Declaration
public static void SaveAssetIfDirty(GUID guid); 
### Parameters
Parameter | Description  
---|---  
obj | The asset object to be saved, if dirty.  
guid | The guid of the asset to be saved, if dirty.  
### Description
Writes all unsaved changes to the specified asset to disk.
This function is similar to [SaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html), and likewise should not be called during serialization.  
  
It does not invoke [AssetModificationProcessor.OnWillSaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillSaveAssets.html), as the asset is directly specified.
* * *
