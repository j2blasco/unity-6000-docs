* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.SetSearchText.html

#  [ISearchView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html).SetSearchText
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
public void SetSearchText(string searchText, [Search.TextCursorPlacement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.html) moveCursor); 
## Declaration
public void SetSearchText(string searchText, [Search.TextCursorPlacement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.html) moveCursor, int cursorInsertPosition); 
### Parameters
Parameter | Description  
---|---  
searchText | Text displayed in the search view.  
moveCursor | Position of the cursor after setting the search text.  
### Description
Sets the search query text.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Example_ISearchView_SetSearchText.png) ![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Example_ISearchView_SetSearchText_SetCursorPosition.png).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;

static class Example_ISearchView_SetSearchText
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ISearchView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html)/SetSearchText")]
    public static void SetInitialText()
    {
        var view = SearchService.ShowContextual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html)("asset");

        // Set the initial text of Search view. By default the whole text of the search query will be selected.
        view.SetSearchText("t:prefab");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(view.context.searchText == "t:prefab");
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ISearchView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html)/SetSearchText_WithCursorPosition")]
    public static void SetSearchText_WithCursorPosition()
    {
        var view = SearchService.ShowContextual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html)("asset");
        view.SetSearchText("t:material", TextCursorPlacement.MoveLineStart[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveLineStart.html));
    }

}


```

* * *
