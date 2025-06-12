* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute-flags.html

#  [SearchContextAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute.html).flags
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
[Search.SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) flags; 
### Description
Search view flags used to open the Object Picker in various states.
The following example will open the Object Picker window using the compact list view and include packages results.
```
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("", "adb", SearchViewFlags.Packages[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.Packages.html) | SearchViewFlags.CompactView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.CompactView.html))]
public MonoScript[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) myPackageScript;
```

* * *
