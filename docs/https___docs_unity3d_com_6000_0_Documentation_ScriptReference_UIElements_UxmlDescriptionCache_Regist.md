* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlDescriptionCache.RegisterType.html

#  [UxmlDescriptionCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlDescriptionCache.html).RegisterType
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
public static void RegisterType(Type type, UxmlAttributeNames[] attributeNames); 
### Parameters
Parameter | Description  
---|---  
type | The type to register.  
attributeNames | The pre-processed UXML attribute information.  
### Description
Registers pre-processed UXML attribute descriptions. 
This is used by the code generator when a control is using [UxmlElementAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlElementAttribute.html) and [UxmlAttributeAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeAttribute.html). 
* * *
