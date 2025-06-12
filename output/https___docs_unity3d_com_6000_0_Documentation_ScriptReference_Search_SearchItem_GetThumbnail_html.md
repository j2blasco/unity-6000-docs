* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.GetThumbnail.html

#  [SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html).GetThumbnail
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
public [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetThumbnail([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, bool cacheThumbnail); 
### Parameters
Parameter | Description  
---|---  
context | Search context used to fetch the search item thumbnail.  
cacheThumbnail | Indicates if the search item thumbnail should be cached for next time.  
### Returns
**Texture2D** Returns the search item 2D texture. 
### Description
Gets the search item thumbnail if available, otherwise the thumbnail is fetched at this time. The thumbnail is usually used in list view compared to the grid view.
* * *
