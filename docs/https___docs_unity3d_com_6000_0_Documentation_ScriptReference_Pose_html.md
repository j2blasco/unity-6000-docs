* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose.html

# Pose
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Representation of a Position, and a Rotation in 3D Space
This structure is used primarily in XR applications to describe the current "pose" of a device in 3D space.
### Static Properties
Property | Description  
---|---  
[identity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-identity.html) | Shorthand for pose which represents zero position, and an identity rotation.  
### Properties
Property | Description  
---|---  
[forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-forward.html) | Returns the forward vector of the pose.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-position.html) | The position component of the pose.  
[right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-right.html) | Returns the right vector of the pose.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-rotation.html) | The rotation component of the pose.  
[up](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-up.html) | Returns the up vector of the pose.  
### Constructors
Constructor | Description  
---|---  
[Pose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-ctor.html) | Creates a new pose with the given vector, and quaternion values.  
### Public Methods
Method | Description  
---|---  
[GetTransformedBy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose.GetTransformedBy.html) | Transforms the current pose into the local space of the provided pose.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-operator_ne.html) | Returns true if two poses are not equal.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose-operator_eq.html) | Returns true if two poses are equal.  
* * *
