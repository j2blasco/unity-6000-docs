* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillDeleteAsset.html

#  [AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html).OnWillDeleteAsset(string,RemoveAssetOptions)
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
This is called by Unity when it is about to delete an asset from disk.
If this is implemented, it allows you to delete the asset yourself. Deletion of a file can be prevented by returning [AssetDeleteResult.FailedDelete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDeleteResult.FailedDelete.html) You should not call any Unity AssetDatabase api from within this callback, preferably keep to file operations or VCS apis. 
* * *
