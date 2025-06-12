* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.CreatePickerState.html

#  [SearchViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html).CreatePickerState
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
public static [Search.SearchViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html) CreatePickerState(string title, [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Action<Object,bool> selectObjectHandler, Action<Object> trackingObjectHandler, string typeName, Type filterType, [Search.SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) flags); 
## Declaration
public static [Search.SearchViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html) CreatePickerState(string title, [Search.SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Action<SearchItem,bool> selectHandler, Action<SearchItem> trackingHandler, Func<SearchItem,bool> filterHandler, [Search.SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
title | Title of the picker window.  
context | SearchContext used to setup whcih SearchProvider and initial query are setup for this Picker.  
selectObjectHandler | Selector Callback.  
trackingObjectHandler | Callbacks triggeeds when the select selects an item.  
typeName | Name of the type of assets or components we want to pick.  
filterType | Type of the items we want to pick.  
flags | Flags specifying how the picker view should be displayed.  
selectHandler | Selector Callback.  
trackingHandler | Callbacks triggeeds when the select selects an item.  
filterHandler | Filtering calback.  
### Returns
**SearchViewState** Returns a view state use to open an Object picker. 
### Description
Create a SearchViewState specially setup to show an Object Picker.
* * *
