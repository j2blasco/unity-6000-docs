* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.SetPreviewTextureCacheSize.html

#  [AssetPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.html).SetPreviewTextureCacheSize
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
public static void SetPreviewTextureCacheSize(int size); 
### Parameters
Parameter | Description  
---|---  
size | The number of previews that can be loaded into the cache before the least used previews are being unloaded.  
### Description
Set the asset preview cache to a size that can hold all visible previews on the screen at once.
If showing previews in a scrollpane make sure the cache larger than the count of the visible previews otherwise flickering will occur since least used previews will be unloaded to make space in the cache.
* * *
