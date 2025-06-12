* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html

#  [SearchService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html).ShowContextual
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
public static [Search.ISearchView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html) ShowContextual(params string[] providerIds); 
### Parameters
Parameter | Description  
---|---  
providerIds | Unique IDs of search providers to enable when opening the search view.  
### Returns
**ISearchView** Returns the search view window instance. 
### Description
Open the search window using a specific context (activating specific filters).
```
[MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html)/Search Menus _F1")]
public static void SearchMenuItems()
{
    SearchService.ShowContextual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html)("menu");
}

```

* * *
