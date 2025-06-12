* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-ctor.html

# SearchProvider Constructor
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
public SearchProvider(string id); 
## Declaration
public SearchProvider(string id, string displayName); 
## Declaration
public SearchProvider(string id, Func<SearchContext,List<SearchItem>,SearchProvider,object> fetchItemsHandler); 
## Declaration
public SearchProvider(string id, Func<SearchContext,SearchProvider,object> fetchItemsHandler); 
## Declaration
public SearchProvider(string id, string displayName, Func<SearchContext,SearchProvider,object> fetchItemsHandler); 
## Declaration
public SearchProvider(string id, string displayName, Func<SearchContext,List<SearchItem>,SearchProvider,object> fetchItemsHandler); 
### Parameters
Parameter | Description  
---|---  
id | Search Provider unique ID.  
displayName | Search Provider pretty name, used to display in UI.  
fetchItemsHandler | Handler responsible for populating a list of SearchItems according to a query.  
### Description
Create a new SearchProvider.
For different use cases see [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html), [SearchProvider.id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-id.html), [SearchProvider.isExplicitProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-isExplicitProvider.html), [SearchProvider.priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-priority.html).
* * *
