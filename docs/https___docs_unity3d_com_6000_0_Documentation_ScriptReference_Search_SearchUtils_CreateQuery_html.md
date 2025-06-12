* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.CreateQuery.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).CreateQuery
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
public static [Search.ISearchQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchQuery.html) CreateQuery(ref string name, [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, [Search.SearchTable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.html) tableConfig); 
### Parameters
Parameter | Description  
---|---  
name | Name of the query.  
context | Search context used to execute the query.  
tableConfig | Search table used to populate the table view. Can be null.  
### Returns
**ISearchQuery** Returns a new search query object. 
### Description
Creates a new search query.
This search query needs to be persisted manually.
* * *
