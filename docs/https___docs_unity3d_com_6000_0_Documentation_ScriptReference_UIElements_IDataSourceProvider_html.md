* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDataSourceProvider.html

# IDataSourceProvider
interface in UnityEngine.UIElements
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
Binding types deriving from [Binding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.html) can implement this interface to gain an additional layer of data source and data source path. These will be used by the binding system to compute the final [BindingContext.dataSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingContext-dataSource.html) and [BindingContext.dataSourcePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingContext-dataSourcePath.html) that will be passed to the [BindingContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingContext.html) during the binding update. 
This dataSource and dataSourcePath will only affect the binding itself and not the hierarchy. 
### Properties
Property | Description  
---|---  
[dataSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDataSourceProvider-dataSource.html) |  Data source object that is local to the binding object.   
[dataSourcePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IDataSourceProvider-dataSourcePath.html) |  Data source path that is local to the binding object.   
* * *
