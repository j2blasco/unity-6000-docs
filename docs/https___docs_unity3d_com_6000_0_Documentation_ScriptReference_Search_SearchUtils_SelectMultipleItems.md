* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.SelectMultipleItems.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).SelectMultipleItems
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
public static void SelectMultipleItems(IEnumerable<SearchItem> items, bool focusProjectBrowser, bool pingSelection); 
### Parameters
Parameter | Description  
---|---  
items | Search Items to select and ping.  
focusProjectBrowser | If true, will focus the project browser before pinging the objects.  
pingSelection | If true, will ping the selected objects.  
### Description
Select and ping multiple objects in the Project Browser.
```
private static void DeleteAssets(IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> items)
{
    var oldSelection = Selection.objects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-objects.html);
    SearchUtils.SelectMultipleItems[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.SelectMultipleItems.html)(items, pingSelection: false);
    // We call ProjectBrowser.DeleteSelectedAssets for the confirmation popup.
    ProjectBrowser.DeleteSelectedAssets(true);
    Selection.objects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-objects.html) = oldSelection;
}

```

* * *
