* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError-ctor.html

# SearchQueryError Constructor
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
public SearchQueryError(int index, int length, string reason, [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, [Search.SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider, bool fromSearchQuery, [Search.SearchQueryErrorType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryErrorType.html) type); 
### Parameters
Parameter | Description  
---|---  
index | Index where the error occurred.  
length | Length of the block that was being parsed.  
reason | The reason for the error.  
context | The context in which this error was logged.  
provider | Which search provider logged this error.  
fromSearchQuery | Set to true if this error comes from parsing the searchQuery. This will correctly offset the index with respect to the raw text.  
type | The type of query error. See [SearchQueryErrorType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryErrorType.html). Defaults to [SearchQueryErrorType.Error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryErrorType.Error.html).  
### Description
Creates a new SearchQueryError.
* * *
## Declaration
public SearchQueryError([Search.QueryError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError.html) error, [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, [Search.SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider, bool fromSearchQuery); 
### Parameters
Parameter | Description  
---|---  
error | The original [QueryError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError.html).  
context | The context in which this error was logged.  
provider | Which search provider logged this error.  
fromSearchQuery | Set to true if this error comes from parsing the searchQuery. This will correctly offset the index with respect to the raw text.  
### Description
Creates a new SearchQueryError from an existing [QueryError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError.html).
* * *
