* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanOpenForEdit.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).CanOpenForEdit
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
public static bool CanOpenForEdit([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) assetObject, [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) statusOptions = StatusQueryOptions.UseCachedIfPossible); 
## Declaration
public static bool CanOpenForEdit(string assetOrMetaFilePath, [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) statusOptions = StatusQueryOptions.UseCachedIfPossible); 
## Declaration
public static bool CanOpenForEdit([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) assetObject, out string message, [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) statusOptions = StatusQueryOptions.UseCachedIfPossible); 
## Declaration
public static bool CanOpenForEdit(string assetOrMetaFilePath, out string message, [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) statusOptions = StatusQueryOptions.UseCachedIfPossible); 
### Parameters
Parameter | Description  
---|---  
assetObject | Object representing the asset whose status you wish to query.  
assetOrMetaFilePath | Path to the asset file or its .meta file on disk, relative to project folder.  
message | Returns a reason for the asset not being available for edit.  
statusOptions | Options for how the version control system should be queried. These options can effect the speed and accuracy of the query. Default is [StatusQueryOptions.UseCachedIfPossible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.UseCachedIfPossible.html).  
### Returns
**bool** True if the asset is considered available for edit by the selected version control system. 
### Description
Query whether an Asset file can be opened for editing in version control and is not exclusively locked by another user or otherwise unavailable.
See [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html) for detailed explanation.  
  
Additional resources: [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html), [AssetDatabase.MakeEditable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MakeEditable.html).
* * *
## Declaration
public static void CanOpenForEdit(string[] assetOrMetaFilePaths, List<string> outNotEditablePaths, [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) statusQueryOptions = StatusQueryOptions.UseCachedIfPossible); 
### Parameters
Parameter | Description  
---|---  
assetOrMetaFilePaths | Paths to Assets or their .meta files, relative to the project folder.  
outNotEditablePaths | Destination list of non-editable Asset paths.  
statusQueryOptions | Specifies how Unity should query the version control system. The default value is [StatusQueryOptions.UseCachedIfPossible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.UseCachedIfPossible.html).  
### Description
Query which of the provided Asset files can be opened for editing in version control and are not remotely locked or otherwise unavailable.
This variant of the `CanOpenForEdit` function can query multiple Asset paths at once. It writes paths for Assets that are not 'available for edit' into the `outNotEditablePaths` list.
* * *
