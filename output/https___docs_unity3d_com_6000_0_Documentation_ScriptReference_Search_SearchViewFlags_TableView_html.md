* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.TableView.html

#  [SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html).TableView
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
The Search Picker window will open in table view.
This can be useful if you want to use a search expression to display selected (that is using a select{} statement) values in a Search table.
```
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("select{p:t:material, @label, @size}", "expression;asset", SearchViewFlags.TableView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.TableView.html))]
public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) selectMaterialBySize;
```

* * *
