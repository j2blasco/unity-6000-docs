* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-ctor.html

# SearchContext Constructor
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
public SearchContext(IEnumerable<SearchProvider> providers, string searchText, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) options); 
## Declaration
public SearchContext(IEnumerable<SearchProvider> providers, string searchText); 
## Declaration
public SearchContext(IEnumerable<SearchProvider> providers); 
### Parameters
Parameter | Description  
---|---  
providers | The list of search providers used to resolve the specified query.  
searchText | The search query to perform.  
options | A set of options that help evaluate the query.  
### Description
Creates a new search context.
* * *
