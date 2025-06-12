* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.GetAnimatableBindings.html

#  [GenericBindingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.html).GetAnimatableBindings
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
public static GenericBinding[] GetAnimatableBindings([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) targetObject, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) root); 
### Parameters
Parameter | Description  
---|---  
targetObject | The target [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to extract the bindings from.  
root | A [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) ancestor of targetObject. Use the ancestor to locate the targetObject within a transform hierarchy.  
### Returns
**GenericBinding[]** Returns an array of [GenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html). Returns an empty array if the targetObject has no animatable properties. 
### Description
Retrieves the animatable bindings for a specific GameObject.
* * *
