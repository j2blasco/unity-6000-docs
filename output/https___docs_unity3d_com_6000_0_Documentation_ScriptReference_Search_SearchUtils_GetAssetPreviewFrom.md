* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetAssetPreviewFromPath.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).GetAssetPreviewFromPath
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
public static [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetAssetPreviewFromPath(string path, [Search.FetchPreviewOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.html) previewOptions); 
## Declaration
public static [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetAssetPreviewFromPath(string path, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) previewSize, [Search.FetchPreviewOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.html) previewOptions); 
### Parameters
Parameter | Description  
---|---  
path | Asset path.  
previewOptions | Additional preview options.  
previewSize | Request size of the preview. This is useful for the [DisplayMode.Grid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.Grid.html) view.  
### Returns
**Texture2D** Preview texture. 
### Description
Returns a preview texture to be used in the search view.
See [SearchProvider.fetchPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchPreview.html).
* * *
