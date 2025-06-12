* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetAssetPath.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).GetAssetPath
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
public static string GetAssetPath(ref [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item); 
### Parameters
Parameter | Description  
---|---  
item | Search item.  
### Returns
**string** Asset path of the item or null if none can be found. 
### Description
Returns the asset path of a search item if any.
The returned asset path depends on the [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) of the item.
* * *
