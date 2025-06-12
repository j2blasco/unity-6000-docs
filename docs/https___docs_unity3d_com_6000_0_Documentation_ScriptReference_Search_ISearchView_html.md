* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.html

# ISearchView
interface in UnityEditor.Search
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
Search view interface used by the search context to execute UI operations.
### Properties
Property | Description  
---|---  
[context](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-context.html) | Returns the current view search context.  
[currentGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-currentGroup.html) | Indicates the current group that is selected by the user.  
[displayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-displayMode.html) | Indicates how the data is displayed in the UI.  
[filterCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-filterCallback.html) | Callback used to filter items shown in the list.  
[itemIconSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-itemIconSize.html) | Defines the size of items in the search view.  
[multiselect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-multiselect.html) | Allows multi-selection of items in the list/grid of items. If false, a user can only select a single item.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-position.html) | Returns the absolute position of the Search window.  
[results](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-results.html) | Returns the list of all search results.  
[searchInProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-searchInProgress.html) | Indicates that the search view is currently running a query and it has not yet completed.  
[selectCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-selectCallback.html) | Callback used to override a default Search behavior.  
[selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-selection.html) | Returns the selected items in the view.  
[state](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-state.html) | Returns the view model state of the Search Window.  
[trackingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView-trackingCallback.html) | Callback used to override the tracking behavior.  
### Public Methods
Method | Description  
---|---  
[AddSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.AddSelection.html) | Adds new items to the current selection.  
[Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.Close.html) | Closes the search view.  
[ExecuteAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.ExecuteAction.html) | Executes a Search action on a given list of items.  
[ExecuteSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.ExecuteSelection.html) | Execute the default action of the active selection.  
[Focus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.Focus.html) | Make sure the Search window is now selected to receive input from a user.  
[FocusSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.FocusSearch.html) | Focus the search text field control.  
[IsPicker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.IsPicker.html) | Indicates if the search view is being used as an advanced search picker.  
[Refresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.Refresh.html) | Triggers a refresh of the search view and refetches all the search items from enabled search providers.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.Repaint.html) | Requests the search view to repaint itself.  
[SelectSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.SelectSearch.html) | Puts focus in the SearchView text field AND selects all the text inside the text field (if any).  
[SetColumns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.SetColumns.html) | Sets the search view property table columns.  
[SetSearchText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.SetSearchText.html) | Sets the search query text.  
[SetSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.SetSelection.html) | Updates the search view with a new selection.  
[ShowItemContextualMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ISearchView.ShowItemContextualMenu.html) | Shows a contextual menu for the specified item.  
* * *
