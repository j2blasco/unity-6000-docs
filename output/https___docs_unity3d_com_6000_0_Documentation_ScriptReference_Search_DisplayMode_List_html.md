* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.List.html

#  [DisplayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.html).List
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
Display as a list view.
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
* * *
