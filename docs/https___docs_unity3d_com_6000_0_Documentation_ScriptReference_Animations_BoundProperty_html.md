* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html

# BoundProperty
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
A BoundProperty is a safe handle to read and write value in a generic way from any Unity components.
### Static Properties
Property | Description  
---|---  
[Null](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.Null.html) | An empty BoundProperty object that does not refer to a property.  
### Properties
Property | Description  
---|---  
[index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty-index.html) | The index of this BoundProperty to the internal list of bound properties.  
[version](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty-version.html) | The version of the BoundProperty.  
### Public Methods
Method | Description  
---|---  
[CompareTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.CompareTo.html) | Compares this BoundProperty to a specific BoundProperty.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.Equals.html) | Checks if this BoundProperty equals a specified BoundProperty object.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.GetHashCode.html) | Retrieves a unique hash based on this BoundProperty.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty-operator_ne.html) | BoundProperty objects are not equal if they refer to different properties.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty-operator_eq.html) | BoundProperty objects are equal if they refer to the same property.  
* * *
