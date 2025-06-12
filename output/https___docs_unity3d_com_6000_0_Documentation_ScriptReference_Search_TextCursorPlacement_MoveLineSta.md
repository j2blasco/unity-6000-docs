* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveLineStart.html

#  [TextCursorPlacement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.html).MoveLineStart
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
Move the cursor to the beginning of the line of text.
```
[MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ISearchView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html)/SetSearchText_WithCursorPosition")]
public static void SetSearchText_WithCursorPosition()
{
    var view = SearchService.ShowContextual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html)("asset");
    view.SetSearchText("t:material", TextCursorPlacement.MoveLineStart[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveLineStart.html));
}

```

* * *
