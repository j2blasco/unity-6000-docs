* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html

# Vector3
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
Representation of 3D vectors and points.
This structure is used throughout Unity to pass 3D positions and directions around. It also contains functions for doing common vector operations.  
  
Besides the functions listed below, other classes can be used to manipulate vectors and points as well. For example the [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) and the [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) classes are useful for rotating or transforming vectors and points.
### Static Properties
Property | Description  
---|---  
[back](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-back.html) | Shorthand for writing Vector3(0, 0, -1).  
[down](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-down.html) | Shorthand for writing Vector3(0, -1, 0).  
[forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) | Shorthand for writing Vector3(0, 0, 1).  
[left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-left.html) | Shorthand for writing Vector3(-1, 0, 0).  
[negativeInfinity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-negativeInfinity.html) | Shorthand for writing Vector3(float.NegativeInfinity, float.NegativeInfinity, float.NegativeInfinity).  
[one](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html) | Shorthand for writing Vector3(1, 1, 1).  
[positiveInfinity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-positiveInfinity.html) | Shorthand for writing Vector3(float.PositiveInfinity, float.PositiveInfinity, float.PositiveInfinity).  
[right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) | Shorthand for writing Vector3(1, 0, 0).  
[up](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) | Shorthand for writing Vector3(0, 1, 0).  
[zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html) | Shorthand for writing Vector3(0, 0, 0).  
### Properties
Property | Description  
---|---  
[magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-magnitude.html) | Returns the length of this vector (Read Only).  
[normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-normalized.html) | Returns a normalized vector based on the current vector. The normalized vector has a magnitude of 1 and is in the same direction as the current vector. Returns a zero vector If the current vector is too small to be normalized.  
[sqrMagnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-sqrMagnitude.html) | Returns the squared length of this vector (Read Only).  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Index_operator.html) | Access the x, y, z components using [0], [1], [2] respectively.  
[x](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-x.html) | X component of the vector.  
[y](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-y.html) | Y component of the vector.  
[z](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-z.html) | Z component of the vector.  
### Constructors
Constructor | Description  
---|---  
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-ctor.html) | Creates a new vector with given x, y, z components.  
### Public Methods
Method | Description  
---|---  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Equals.html) | Returns true if the given vector is exactly equal to this vector.  
[Set](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Set.html) | Set x, y and z components of an existing Vector3.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ToString.html) | Returns a formatted string for this vector.  
### Static Methods
Method | Description  
---|---  
[Angle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Angle.html) | Calculates the angle between two vectors.  
[ClampMagnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ClampMagnitude.html) | Returns a copy of vector with its magnitude clamped to maxLength.  
[Cross](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Cross.html) | Cross Product of two vectors.  
[Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Distance.html) | Returns the distance between a and b.  
[Dot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Dot.html) | Dot Product of two vectors.  
[Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html) | Linearly interpolates between two points.  
[LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.LerpUnclamped.html) | Linearly interpolates between two vectors.  
[Max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Max.html) | Returns a vector that is made from the largest components of two vectors.  
[Min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Min.html) | Returns a vector that is made from the smallest components of two vectors.  
[MoveTowards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.MoveTowards.html) | Calculate a position between the points specified by current and target, moving no farther than the distance specified by maxDistanceDelta.  
[Normalize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Normalize.html) | Makes this vector have a magnitude of 1.  
[OrthoNormalize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.OrthoNormalize.html) | Makes vectors normalized and orthogonal to each other.  
[Project](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Project.html) | Projects a vector onto another vector.  
[ProjectOnPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ProjectOnPlane.html) | Projects a vector onto a plane.  
[Reflect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Reflect.html) | Reflects a vector off the plane defined by a normal.  
[RotateTowards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.RotateTowards.html) | Rotates a vector current towards target.  
[Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Scale.html) | Multiplies two vectors component-wise.  
[SignedAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SignedAngle.html) | Calculates the signed angle between vectors from and to in relation to axis.  
[Slerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Slerp.html) | Spherically interpolates between two vectors.  
[SlerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SlerpUnclamped.html) | Spherically interpolates between two vectors.  
[SmoothDamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SmoothDamp.html) | Gradually changes a vector towards a desired goal over time.  
### Operators
Operator | Description  
---|---  
[operator -](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_subtract.html) | Subtracts one vector from another.  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_ne.html) | Returns true if vectors are different.  
[operator *](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_multiply.html) | Multiplies a vector by a number.  
[operator /](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_divide.html) | Divides a vector by a number.  
[operator +](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_add.html) | Adds two vectors.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-operator_eq.html) | Returns true if two vectors are approximately equal.  
* * *
