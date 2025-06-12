* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMetaFileOpenForEdit.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).IsMetaFileOpenForEdit
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
public static bool IsMetaFileOpenForEdit([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) assetObject, [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) statusOptions = StatusQueryOptions.UseCachedIfPossible); 
## Declaration
public static bool IsMetaFileOpenForEdit([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) assetObject, out string message, [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) statusOptions = StatusQueryOptions.UseCachedIfPossible); 
### Parameters
Parameter | Description  
---|---  
assetObject | Object representing the asset whose metadata status you wish to query.  
message | Returns a reason for the asset metadata not being open for edit.  
statusOptions | Options for how the version control system should be queried. These options can effect the speed and accuracy of the query. Default is [StatusQueryOptions.UseCachedIfPossible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.UseCachedIfPossible.html).  
### Returns
**bool** True if the asset's metadata is considered open for edit by the selected version control system. 
### Description
Query whether an asset's metadata (.meta) file is open for edit in version control.
Your version control system may be configured to only allow a single user at a time to edit certain types of file, to avoid conflicts that arise when multiple users edit a file at the same time. In this case a user must 'open' that file for editing (also known as 'checking out') to ensure that they have permission to edit the file. Use this function to query the 'open for edit' status of a file in a version control system that supports it.  
  
Additional resources: [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html), [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html).
* * *
