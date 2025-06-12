* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlTypeAttributeDescription_1.GetValueFromBag.html

#  [UxmlTypeAttributeDescription<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlTypeAttributeDescription_1.html).GetValueFromBag
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
public Type GetValueFromBag([UIElements.IUxmlAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IUxmlAttributes.html) bag, [UIElements.CreationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CreationContext.html) cc); 
### Parameters
Parameter | Description  
---|---  
bag | The attribute bag.  
cc | The context in which the method retrieves attribute values.  
### Returns
**Type** The attribute's value. If the method cannot find the value, returns defaultValue. 
### Description
Method that retrieves an attribute's value from an attribute bag. Returns it if it is found, otherwise return defaultValue. 
* * *
