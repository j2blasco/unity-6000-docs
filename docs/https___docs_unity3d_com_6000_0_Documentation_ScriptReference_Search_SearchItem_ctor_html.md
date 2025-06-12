* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-ctor.html

# SearchItem Constructor
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
public SearchItem(string _id); 
### Parameters
Parameter | Description  
---|---  
_id | Unique ID of the SearchItem.  
### Description
Construct a search item. A search item needs to have at least a unique ID for a given search query.
SearchItem are generally created using the [SearchProvider.CreateItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.CreateItem.html) function. See [SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) for example of items creation.
* * *
