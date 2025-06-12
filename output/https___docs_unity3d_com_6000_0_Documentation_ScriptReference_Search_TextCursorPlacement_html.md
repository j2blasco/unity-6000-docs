* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.html

# TextCursorPlacement
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
Where to place the cursor in the text. (see [ISearchView.SetSearchText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.SetSearchText.html)).
```
[MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ISearchView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html)/SetSearchText_WithCursorPosition")]
public static void SetSearchText_WithCursorPosition()
{
    var view = SearchService.ShowContextual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowContextual.html)("asset");
    view.SetSearchText("t:material", TextCursorPlacement.MoveLineStart[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveLineStart.html));
}

```

### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.None.html) | Do not move the cursor.  
[MoveLineEnd](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveLineEnd.html) | Move the cursor to the end of the line of text.  
[MoveLineStart](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveLineStart.html) | Move the cursor to the beginning of the line of text.  
[MoveToEndOfPreviousWord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveToEndOfPreviousWord.html) | Move the cursor to the end of the previous word.  
[MoveToStartOfNextWord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveToStartOfNextWord.html) | Move the cursor to the start of the previous word.  
[MoveWordLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveWordLeft.html) | Move the cursor one word to the left.  
[MoveWordRight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveWordRight.html) | Move the cursor one word to the right.  
[MoveAutoComplete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.MoveAutoComplete.html) | Default cursor position (end of the line of text).  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.Default.html) | Do not move the cursor.  
* * *
