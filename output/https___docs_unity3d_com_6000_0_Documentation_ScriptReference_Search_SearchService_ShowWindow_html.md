* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html

#  [SearchService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html).ShowWindow
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
public static [Search.ISearchView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html) ShowWindow([Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, string topic, float defaultWidth, float defaultHeight, bool saveFilters, bool reuseExisting, bool multiselect, bool dockable); 
### Parameters
Parameter | Description  
---|---  
context | Search context to start with.  
topic | Topic to search.  
saveFilters | True if user search provider filters should be saved for next search session.  
reuseExisting | True if the active providers should be saved for the next session.  
multiselect | True if the search supports multi-selection.  
defaultWidth | Initial width of the window.  
defaultHeight | Initial height of the window.  
dockable | If true, creates a dockable search window (that is closed when an item is activated). If false, it creates a dropdown (borderless, undockable and unmovable) version of the search window.  
### Returns
**ISearchView** Returns the search view window instance. 
### Description
Creates a new search window.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;

static class Example_SearchService_ShowWindow
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/ShowWindowEmpty")]
    public static void Run1()
    {
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)()
            .SetSearchText(string.Empty);
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/ShowWindowWithSearchText")]
    public static void Run2()
    {
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("m: Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html)"));
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/ShowWindowCustomTopic")]
    public static void Run3()
    {
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(topic: "My Things")
            .SetSearchText(string.Empty);
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html)/ShowPopupWindow")]
    public static void Run4()
    {
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(defaultWidth: 1300, defaultHeight: 700, dockable: false);
    }
}


```

* * *
## Declaration
public static [Search.ISearchView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html) ShowWindow([Search.SearchViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html) viewState); 
### Parameters
Parameter | Description  
---|---  
viewState | Search view state used to open the Search window.  
### Returns
**ISearchView** Returns the search view window instance. 
### Description
Creates a new search window.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine.Search;  
  
static class SearchWindows
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Search/Views/Simple Search Bar 1")] public static void SearchViewFlags1() => CreateWindow(SearchViewFlags.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.None.html));
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Search/Views/Simple Search Bar 2")] public static void SearchViewFlags2() => CreateWindow(SearchViewFlags.EnableSearchQuery[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.EnableSearchQuery.html));
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Search/Views/Simple Search Bar 3")] public static void SearchViewFlags3() => CreateWindow(SearchViewFlags.DisableInspectorPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableInspectorPreview.html));
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Search/Views/Simple Search Bar 4")] public static void SearchViewFlags4() => CreateWindow(SearchViewFlags.EnableSearchQuery[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.EnableSearchQuery.html) | SearchViewFlags.DisableInspectorPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableInspectorPreview.html));  
  
    static void CreateWindow(SearchViewFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) flags)
    {
        var searchContext = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)(string.Empty);
        var viewArgs = new SearchViewState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html)(searchContext, SearchViewFlags.CompactView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.CompactView.html) | flags) { title = flags.ToString() };
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(viewArgs);
    }
}
```

* * *
