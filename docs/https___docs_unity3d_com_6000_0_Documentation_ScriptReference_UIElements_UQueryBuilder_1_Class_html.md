* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Class.html

#  [UQueryBuilder<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.html).Class
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
public UQueryBuilder<T> Class(string classname); 
### Parameters
Parameter | Description  
---|---  
classname | The class to use in the query.  
### Description
Selects all elements with the specified class in the class list, as specified with the `class` attribute in a UXML file or added with [VisualElement.AddToClassList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.AddToClassList.html) method. 
This method can be called multiple times in order to select elements with multiple classes. To select elements by their C# type, use OfType_1. 
* * *
