* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.html

# SearchSelection
class in UnityEditor.Search
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
Provides methods to give readonly access to the current list of selected items in Search.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;

static class Example_ISearchView_AddSelection
{
    static ISearchView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html) s_View;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ISearchView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html)/AddSelection")]
    public static void Run()
    {
        s_View = SearchService.ShowContextual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html)("asset");
        s_View.SetSearchText("t:MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html)");

        EditorApplication.delayCall[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-delayCall.html) += DisplayResultsWhenReady;
    }

    public static void DisplayResultsWhenReady()
    {
        // Wait until results are ready to process.
        if (s_View.results.pending || s_View.results.Count == 0)
        {
            EditorApplication.delayCall[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-delayCall.html) += DisplayResultsWhenReady;
            return;
        }

        // Use AddSelection to append to the current selection.
        s_View.AddSelection(0);
        s_View.AddSelection(2);
        s_View.AddSelection(4);

        // Validate what is actually selected:
        var selection = s_View.selection;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(selection.Count); // 3
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(selection.MinIndex()); // 0
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(selection.MaxIndex()); // 4
    }
}

```

### Properties
Property | Description  
---|---  
[Count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.Count.html) | The number of items selected.  
### Constructors
Constructor | Description  
---|---  
[SearchSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection-ctor.html) | Creates a new SearchSelection.  
### Public Methods
Method | Description  
---|---  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.Contains.html) | Checks if the search item is contained in the current selection.  
[First](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.First.html) | Gets the first selected item in the selection.  
[GetEnumerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.GetEnumerator.html) | Gets an enumerator on the currently selected SearchItems.  
[Last](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.Last.html) | Gets the last selected item in the selection.  
[MaxIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.MaxIndex.html) | Highest selected index of any item in the selection.  
[MinIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.MinIndex.html) | Lowest selected index of any item in the selection.  
* * *
