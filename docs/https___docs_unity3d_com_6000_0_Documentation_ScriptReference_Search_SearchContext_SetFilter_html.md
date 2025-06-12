* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.SetFilter.html

#  [SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html).SetFilter
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
public void SetFilter(string providerId, bool isEnabled); 
### Parameters
Parameter | Description  
---|---  
providerId | ID of the search provider. See SearchProvider.name.id.  
isEnabled | If true, enables the search provider to perform a query.  
### Description
Enables or disables a single search provider. A disabled search provider won't be asked to provide items to resolve the query.
* * *
