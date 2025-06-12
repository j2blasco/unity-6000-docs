* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetHierarchyPath.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).GetHierarchyPath
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
public static string GetHierarchyPath([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, bool includeScene); 
### Parameters
Parameter | Description  
---|---  
gameObject | GameObject to extract a path from.  
includeScene | If true, will append the scene name to the path.  
### Returns
**string** Returns the path of a GameObject. 
### Description
Get the hierarchy path of a GameObject including the scene name if includeScene is set to true.
```
static string FetchDescription(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
{
    var go = ObjectFromItem(item);
    return (item.description = SearchUtils.GetHierarchyPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetHierarchyPath.html)(go));
}

```

* * *
