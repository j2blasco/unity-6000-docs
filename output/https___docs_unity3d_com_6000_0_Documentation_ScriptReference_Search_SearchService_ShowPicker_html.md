* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowPicker.html

#  [SearchService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html).ShowPicker
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
public static [Search.ISearchView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html) ShowPicker([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Action<SearchItem,bool> selectHandler, Action<SearchItem> trackingHandler, Func<SearchItem,bool> filterHandler, IEnumerable<SearchItem> subset, string title, float itemSize, float defaultWidth, float defaultHeight, [Search.SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
context | Search context to start with.  
selectHandler | Callback invoked when an item is selected.  
trackingHandler | Callback invoked when an item is clicked without it being the final selection.  
filterHandler | Callback invoked to filter search item results to display.  
title | Topic to search.  
itemSize | Initial result view item size.  
defaultWidth | Initial width of the window.  
defaultHeight | Initial height of the window.  
subset | Initial set of items to be searched.  
flags | Options defining how the query is performed.  
### Returns
**ISearchView** Creates a new search window. 
### Description
Open a search item picker window.
* * *
## Declaration
public static [Search.ISearchView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html) ShowPicker([Search.SearchViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html) viewState); 
### Parameters
Parameter | Description  
---|---  
viewState | Search view state used to open the Search Picker window.  
### Returns
**ISearchView** Creates a new search window. 
### Description
Open a Search Picker window.
This example shows how to open a custom search picker to pick a decal material.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;
using UnityEngine.Search;

static class Example_SearchService_ShowPicker
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/ShowPicker")]
    public static void Run()
    {
        var context = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("asset", "t:material");
        var viewState = new SearchViewState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html)(context,
            SearchViewFlags.GridView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.GridView.html) |
            SearchViewFlags.OpenInBuilderMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenInBuilderMode.html) |
            SearchViewFlags.DisableSavedSearchQuery[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableSavedSearchQuery.html))
        {
            windowTitle = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) Selector"),
            title = "Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)",
            selectHandler = SelectHandler,
            trackingHandler = TrackingHandler,
            position = SearchUtils.GetMainWindowCenteredPosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetMainWindowCenteredPosition.html)(new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(600, 400))
        };
        SearchService.ShowPicker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowPicker.html)(viewState);
    }

    static void SelectHandler(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) searchItem, bool canceled)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Selected {searchItem} (canceled: {canceled})");
    }

    static void TrackingHandler(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) searchItem)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Tracking {searchItem}");
    }
}

```

* * *
