* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyBagVisitor.Visit.html

#  [IPropertyBagVisitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Properties.IPropertyBagVisitor.html).Visit
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
public void Visit(IPropertyBag<TContainer> properties, ref TContainer container); 
### Parameters
Parameter | Description  
---|---  
properties | The properties of the container.  
container | The container being visited.  
### Description
Implement this method to accept visitation for a property bag and container. 
This method is invoked by IPropertyBag_1.Accept. 
* * *
