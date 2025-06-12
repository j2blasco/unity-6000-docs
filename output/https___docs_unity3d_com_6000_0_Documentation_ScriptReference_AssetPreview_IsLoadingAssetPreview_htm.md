* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.IsLoadingAssetPreview.html

#  [AssetPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.html).IsLoadingAssetPreview
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
public static bool IsLoadingAssetPreview(int instanceID); 
### Parameters
Parameter | Description  
---|---  
instanceID | InstanceID of the assset that a preview has been requested for by: AssetPreview.GetAssetPreview().  
### Description
Loading previews is asynchronous so it is useful to know if a specific asset preview is in the process of being loaded so client code e.g can repaint while waiting for the loading to finish.
* * *
