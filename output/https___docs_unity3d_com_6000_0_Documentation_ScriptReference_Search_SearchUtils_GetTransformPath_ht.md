* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetTransformPath.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).GetTransformPath
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
public static string GetTransformPath([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) tform); 
### Parameters
Parameter | Description  
---|---  
tform | Transform to extract name from.  
### Returns
**string** Returns a transform name using "/" as hierarchy separator. 
### Description
Format the pretty name of a Transform component by appending all the parent hierarchy names.
```
static string FetchLabel(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
{
    if (item.label != null)
        return item.label;

    var go = ObjectFromItem(item);
    if (!go)
        return item.id;

    var transformPath = SearchUtils.GetTransformPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetTransformPath.html)(go.transform);
    var components = go.GetComponents<Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)>();
    if (components.Length > 2 && components[1] && components[components.Length - 1])
        item.label = $"{transformPath} ({components[1].GetType().Name}..{components[components.Length - 1].GetType().Name})";
    else if (components.Length > 1 && components[1])
        item.label = $"{transformPath} ({components[1].GetType().Name})";
    else
        item.label = $"{transformPath} ({item.id})";

    return item.label;
}

```

* * *
