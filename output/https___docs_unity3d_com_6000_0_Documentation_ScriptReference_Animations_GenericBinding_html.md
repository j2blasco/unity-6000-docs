* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html

# GenericBinding
struct in UnityEngine.Animations
/
Implemented in:[UnityEngine.AnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AnimationModule.html)
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
### Description
Defines an animatable property on a Unity Component.
[GenericBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding.html) and [BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html) are classes for animating properties on objects in a completely generic way.  
  
See also [GenericBindingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.html).
### Properties
Property | Description  
---|---  
[customTypeID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding-customTypeID.html) | The internal ID for custom animation bindings.  
[isDiscrete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding-isDiscrete.html) | This property is true when the GenericBinding target is an animatable public integer.  
[isObjectReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding-isObjectReference.html) | This property is True when this GenericBinding target is an animatable Unity object reference, such as a sprite.  
[isSerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding-isSerializeReference.html) | This property is True when this GenericBinding target is a serialized reference property.  
[propertyNameHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding-propertyNameHash.html) | Hash ID that represents the name of the property.  
[scriptInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding-scriptInstanceID.html) | The instance ID of the script.  
[transformPathHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding-transformPathHash.html) | Hash ID that represents the transform path. Use this property to locate the component in the transform hierarchy.  
[typeID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBinding-typeID.html) | The Unity component type ID.  
* * *
