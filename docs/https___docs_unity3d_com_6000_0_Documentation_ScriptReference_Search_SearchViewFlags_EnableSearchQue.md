* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.EnableSearchQuery.html

#  [SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html).EnableSearchQuery
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
This flag enables the use of the Saved Searches workflow in the Search Picker window.
This flag is not set by default. When it is not set, the Search Picker window will not show any panel or button related to the Saved Searches workflow. The flag [OpenLeftSidePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenLeftSidePanel.html) will not work without [EnableSearchQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.EnableSearchQuery.html).
```
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:material", "asset", SearchViewFlags.EnableSearchQuery[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.EnableSearchQuery.html))]
public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) selectMaterial;
```

* * *
