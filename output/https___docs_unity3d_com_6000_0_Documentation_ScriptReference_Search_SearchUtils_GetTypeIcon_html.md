* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetTypeIcon.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).GetTypeIcon
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
public static [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetTypeIcon(ref Type type); 
### Parameters
Parameter | Description  
---|---  
type | Type.  
### Returns
**Texture2D** Icon for that type. 
### Description
Returns a thumbnail for a given type that can be displayed in a search view. See [SearchProvider.fetchThumbnail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchThumbnail.html).
For search we use an icon cache for types.
* * *
