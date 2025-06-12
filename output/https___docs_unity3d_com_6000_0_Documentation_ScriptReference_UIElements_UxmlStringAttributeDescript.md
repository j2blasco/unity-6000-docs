* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlStringAttributeDescription.GetValueFromBag.html

#  [UxmlStringAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlStringAttributeDescription.html).GetValueFromBag
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
public string GetValueFromBag([UIElements.IUxmlAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IUxmlAttributes.html) bag, [UIElements.CreationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CreationContext.html) cc); 
### Parameters
Parameter | Description  
---|---  
bag | The bag of attributes.  
cc | The context in which the values are retrieved.  
### Returns
**string** The value of the attribute. 
### Description
Retrieves the value of this attribute from the attribute bag. Returns the value if found; otherwise, it returns defaultValue. 
* * *
