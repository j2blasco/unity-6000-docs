* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.TryGetDataSourceContext.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).TryGetDataSourceContext
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
public bool TryGetDataSourceContext([UIElements.BindingId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingId.html) bindingId, out [UIElements.DataSourceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataSourceContext.html) context); 
### Parameters
Parameter | Description  
---|---  
bindingId | The binding ID to query.  
context | The resulting context object.  
### Returns
**bool** Returns `true` if a binding with the provided id was registered on the element; `false` otherwise. 
### Description
Queries the dataSource and dataSourcePath of a binding object. 
* * *
