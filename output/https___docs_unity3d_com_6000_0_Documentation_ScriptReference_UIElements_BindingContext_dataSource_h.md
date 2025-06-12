* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingContext-dataSource.html

#  [BindingContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingContext.html).dataSource
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
dataSource; 
### Description
The data source that was resolved for a given binding. 
If a [Binding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.html) implements the [IDataSourceProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDataSourceProvider.html) interface and provides its own data source, it will automatically be used as the resolved data source; otherwise the data source will be resolved to the first valid data source on the target element or its ancestors. This value can be `null`. 
* * *
