* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.CreateItem.html

#  [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).CreateItem
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
public [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, string id, int score, string label, string description, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) thumbnail, object data); 
**Obsolete** Use CreateItem which take a SearchContext.
## Declaration
public [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(string id, int score, string label, string description, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) thumbnail, object data); 
## Declaration
public [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, string id); 
**Obsolete** Use CreateItem which take a SearchContext.
## Declaration
public [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(string id); 
**Obsolete** Use CreateItem which take a SearchContext.
## Declaration
public [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(string id, string label); 
## Declaration
public [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem(string id, string label, string description, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) thumbnail, object data); 
## Declaration
public [Search.SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) CreateItem([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, string id, string label, string description, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) thumbnail, object data); 
### Parameters
Parameter | Description  
---|---  
context | Search context from the query that generates this item.  
id | Unique ID of the search item. This is used to remove duplicates in the user view.  
score | Relevance score of the search item. The relevance score is used to sort all the results per search provider. Lower relevance scores indicate more relevance and are shown first.  
label | Relevance score of the search item. The relevance score is used to sort all the results per search provider. Lower relevance scores indicate more relevance and are shown first.  
description | The search item description is displayed on the second line of the search item UI widget.  
thumbnail | The search item thumbnail is displayed to the left of the item label and description as a preview.  
data | The search item thumbnail is displayed to the left of the item label and description as a preview.  
### Returns
**SearchItem** The newly created search item attached to the current search provider. 
### Description
Helper function to create a new search item for the current search provider.
For different use cases see [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html), [SearchProvider.id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-id.html), [SearchProvider.isExplicitProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-isExplicitProvider.html), [SearchProvider.priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-priority.html).
* * *
