* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeDescription.TryGetValueFromBag.html

#  [UxmlAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeDescription.html).TryGetValueFromBag
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
protected bool TryGetValueFromBag([UIElements.IUxmlAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IUxmlAttributes.html) bag, [UIElements.CreationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CreationContext.html) cc, Func<string,T,T> converterFunc, T defaultValue, ref T value); 
### Parameters
Parameter | Description  
---|---  
bag | A bag contains attributes and their values as strings.  
cc | The context in which the values are retrieved.  
converterFunc | A function to convert a string value to type T.  
defaultValue | The value to return if the attribute is not found in the bag.  
value | If the attribute could be retrieved, the retrieved value converted by the conversion function or the default value if the retrieved value could not de converted.  
### Returns
**bool** True if the value is found, false otherwise. 
### Description
Tries to get the attribute value from the attribute bag. 
* * *
