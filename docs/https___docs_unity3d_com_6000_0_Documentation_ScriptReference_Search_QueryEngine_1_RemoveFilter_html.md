* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.RemoveFilter.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).RemoveFilter
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
public void RemoveFilter(string token); 
## Declaration
public void RemoveFilter(Regex token); 
### Parameters
Parameter | Description  
---|---  
token | The identifier of the filter. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
### Description
Removes a custom filter.
You will get a warning if you try to remove a non-existent filter.
```
// Remove the filter with token "id"
var token = "id";
queryEngine.RemoveFilter("id");

```

* * *
## Declaration
public void RemoveFilter([Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) filter); 
### Parameters
Parameter | Description  
---|---  
filter | The filter object returned by [AddFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddFilter.html).  
### Description
Removes a custom filter.
* * *
