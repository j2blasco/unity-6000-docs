* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableInspectorPreview.html

#  [SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html).DisableInspectorPreview
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
This flag disables the use of the Inspector Preview in the Search Picker window.
This flag is not set by default. When it is set, the Search Picker window will not show any panel or button related to the Inspector Preview. The flag [OpenInspectorPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.OpenInspectorPreview.html) will not work when [DisableInspectorPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableInspectorPreview.html) is set.
```
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("t:material", "asset", SearchViewFlags.DisableInspectorPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.DisableInspectorPreview.html))]
public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) selectMaterial;
```

* * *
