* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetAssetFolderInfo.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).TryGetAssetFolderInfo
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
public static bool TryGetAssetFolderInfo(string path, out bool rootFolder, out bool immutable); 
### Parameters
Parameter | Description  
---|---  
path | A project relative or absolute path to a file or a folder.  
rootFolder | This value will be set to true if the given path is a root folder in the AssetDatabase.  
immutable | This value will be true if the given file or folder can't be modified by the AssetDatabase .  
### Returns
**bool** Returns true if the given path is in a folder managed by the AssetDatabase, false otherwise. 
### Description
Get AssetDatabase specific information about a folder.
This method can be used to know whether a path is tracked by the AssetDatabase. Being tracked means that files added to this folder will have a .meta file added along them and be imported and available in the current Unity project. The out arguments can be used to get more information about the given path. - rootFolder is true if the given path is the root of a tracked path on your drive. For example the Assets folder is a root. - immutable is true if the given path is under a root folder registered with the immutable flag. For example files in a package added from the package manager registry will be immutable.
* * *
