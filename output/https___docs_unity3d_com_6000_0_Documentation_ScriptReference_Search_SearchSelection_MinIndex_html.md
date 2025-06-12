* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.MinIndex.html

#  [SearchSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.html).MinIndex
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
public int MinIndex(); 
### Returns
**int** Returns the lowest selected index. 
### Description
Lowest selected index of any item in the selection.
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
* * *
