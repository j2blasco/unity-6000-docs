* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetProvider.html

#  [SearchService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html).GetProvider
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
public static [Search.SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) GetProvider(string providerId); 
### Parameters
Parameter | Description  
---|---  
providerId | Unique ID of the search provider.  
### Returns
**SearchProvider** The matching search provider. 
### Description
Returns the data of a search provider given its ID.
```
var menuProvider = SearchService.GetProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetProvider.html)("menu");
Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(menuProvider != null);

```

* * *
