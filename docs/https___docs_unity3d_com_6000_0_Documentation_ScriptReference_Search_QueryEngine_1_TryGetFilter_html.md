* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.TryGetFilter.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).TryGetFilter
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
public bool TryGetFilter(string token, out [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) filter); 
## Declaration
public bool TryGetFilter(Regex token, out [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) filter); 
### Parameters
Parameter | Description  
---|---  
token | The token used to create the filter.  
filter | The existing [IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html), or null if it does not exist.  
### Returns
**bool** Returns true if the filter is retrieved or false if the filter does not exist. 
### Description
Get a filter by its token.
This method tries to retrieve a filter by its token. If it exists, it will be put in the output parameter "filter" and the function returns true. If the filter does not exist, the parameter "filter" is set to null and the function returns false.
```
// Get the filter corresponding to the token "id"
if (!queryEngine.TryGetFilter("id", out var idFilter))
    Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("The filter \"id\" should have been found.");

```

See [GetAllFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.GetAllFilters.html) for a complete example.
* * *
