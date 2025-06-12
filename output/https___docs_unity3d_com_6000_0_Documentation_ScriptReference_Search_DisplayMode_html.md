* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.html

# DisplayMode
enumeration
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
### Description
Options for setting the display mode to use for a search view.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;

static class Example_ISearchView_displayMode
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ISearchView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html)/displayMode")]
    public static void Run()
    {
        // SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html) can open a SearchView.
        var view = SearchService.ShowContextual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html)("asset");

        // You can assign DisplayMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.html) as iconSizeValue...
        view.itemIconSize = (float)DisplayMode.List[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.List.html);

        // ... and this will update displayMode
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(view.displayMode == DisplayMode.List[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.List.html));
    }
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.None.html) | Unspecified ISearchView display mode.  
[Compact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.Compact.html) | Display as a compact list view.  
[List](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.List.html) | Display as a list view.  
[Grid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.Grid.html) | Display as a grid of icons of various sizes.  
[Table](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.Table.html) | Display search results in a table.  
* * *
