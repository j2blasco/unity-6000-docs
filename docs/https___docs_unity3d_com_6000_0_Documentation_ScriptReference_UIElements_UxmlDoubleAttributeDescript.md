* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlDoubleAttributeDescription.TryGetValueFromBag.html

#  [UxmlDoubleAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlDoubleAttributeDescription.html).TryGetValueFromBag
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
public bool TryGetValueFromBag([UIElements.IUxmlAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IUxmlAttributes.html) bag, [UIElements.CreationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CreationContext.html) cc, ref double value); 
### Parameters
Parameter | Description  
---|---  
bag | The bag of attributes.  
cc | The context in which the values are retrieved.  
value | The value of the attribute.  
### Returns
**bool** True if the value is found, false otherwise. 
### Description
Attempts to retrieve the value of this attribute from the attribute bag and returns true if found, otherwise false. 
* * *
