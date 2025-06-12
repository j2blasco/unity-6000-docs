* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.TryGetLastBindingToSourceResult.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).TryGetLastBindingToSourceResult
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
public bool TryGetLastBindingToSourceResult(ref [UIElements.BindingId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingId.html) bindingId, out [UIElements.BindingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html) result); 
### Parameters
Parameter | Description  
---|---  
bindingId | The ID of the binding object.  
result | The result of the last binding operation to the data source.  
### Returns
**bool** `true` if the binding object has been updated; `false` otherwise. 
### Description
Returns the last [BindingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html) of a binding object from the UI to the data source. 
* * *
