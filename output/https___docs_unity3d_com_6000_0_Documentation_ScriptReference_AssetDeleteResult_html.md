* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDeleteResult.html

# AssetDeleteResult
enumeration
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
Result of Asset delete operation
### Properties
Property | Description  
---|---  
[DidNotDelete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDeleteResult.DidNotDelete.html) | Tells the internal implementation that the callback did not delete the asset. The asset will be delete by the internal implementation.  
[FailedDelete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDeleteResult.FailedDelete.html) | Tells Unity that the file cannot be deleted and Unity should leave it alone.  
[DidDelete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDeleteResult.DidDelete.html) | Tells Unity that the asset was deleted by the callback. Unity will not try to delete the asset, but will delete the cached version and preview file.  
* * *
