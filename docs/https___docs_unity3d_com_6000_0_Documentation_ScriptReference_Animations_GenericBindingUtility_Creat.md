* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.CreateGenericBinding.html

#  [GenericBindingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.html).CreateGenericBinding
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
public static bool CreateGenericBinding([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObject, string property, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) root, bool isObjectReference, out [Animations.GenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html) genericBinding); 
### Parameters
Parameter | Description  
---|---  
targetObject | The target [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to extract the bindings from.  
property | The name of the property.  
root | A [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) ancestor of targetObject. Use the ancestor to locate the targetObject within a transform hierarchy.  
genericBinding | Returns the [GenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html) representing the property on the GameObject to animate.  
isObjectReference | Specifies whether the property is an object reference. If you do not identify the property correctly, the method fails. Set this parameter to True if the property references an object. Set to False if the property is a float or an integer.  
### Returns
**bool** Returns True if the operation is successful, otherwise False. 
### Description
Retrieves the [GenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html) that represents a specific property associated with a GameObject or one of its components.
* * *
