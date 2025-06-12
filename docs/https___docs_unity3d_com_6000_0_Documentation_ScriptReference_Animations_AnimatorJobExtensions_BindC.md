* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.BindCustomStreamProperty.html

#  [AnimatorJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorJobExtensions.html).BindCustomStreamProperty
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
public static [Animations.PropertyStreamHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.PropertyStreamHandle.html) BindCustomStreamProperty([Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) animator, string property, [Animations.CustomStreamPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CustomStreamPropertyType.html) type); 
### Parameters
Parameter | Description  
---|---  
animator | The [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html) instance that calls this method.  
name | The name of the property.  
type | The type of property to create (float, integer or boolean).  
### Returns
**PropertyStreamHandle** Returns the PropertyStreamHandle that represents the new binding. 
### Description
Create a custom property in the [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) to pass extra data to downstream animation jobs in your graph. Custom properties created in the [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) do not exist in the scene.
You can create custom properties in the [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) that do not exist in the scene. This can be useful when you want to communicate extra data to downstream animation jobs in your graph.
* * *
