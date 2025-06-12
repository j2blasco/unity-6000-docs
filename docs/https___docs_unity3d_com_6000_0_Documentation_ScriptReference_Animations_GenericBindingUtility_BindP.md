* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.BindProperties.html

#  [GenericBindingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.html).BindProperties
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
public static void BindProperties([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rootGameObject, NativeArray<GenericBinding> genericBindings, out NativeArray<BoundProperty> floatProperties, out NativeArray<BoundProperty> discreteProperties, [Unity.Collections.Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) allocator); 
### Parameters
Parameter | Description  
---|---  
rootGameObject | The root GameObject.  
genericBindings | The list of [GenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html) to bind. See [GenericBindingUtility.GetAnimatableBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.GetAnimatableBindings.html), [GenericBindingUtility.GetCurveBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.GetCurveBindings.html).  
floatProperties | Returns the list of float bound properties for all valid generic binding. If there is an invalid binding, this param returns [BoundProperty.Null](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.Null.html).  
discreteProperties | Returns the list of discrete bound properties for all valid generic bindings. If there is an invalid binding, this param returns [BoundProperty.Null](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.Null.html)  
allocator | Allocator for allocating NativeArray memory.  
### Description
Retrieves the list of [BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html) defined by the list of [GenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html).
BoundProperty allocates resources that must be unallocated. See [GenericBindingUtility.UnbindProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.UnbindProperties.html).  
  
This method throws an ArgumentException if the genericBindings NativeArray is not created.
* * *
