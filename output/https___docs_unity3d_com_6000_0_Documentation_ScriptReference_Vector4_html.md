* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html

# Vector4
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
Representation of four-dimensional vectors.
This structure is used in some places to represent four component vectors (e.g. mesh tangents, parameters for shaders). In the majority of other cases a [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) is used.
### Static Properties
Property | Description  
---|---  
[negativeInfinity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-negativeInfinity.html) | Shorthand for writing Vector4(float.NegativeInfinity, float.NegativeInfinity, float.NegativeInfinity, float.NegativeInfinity).  
[one](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-one.html) | Shorthand for writing Vector4(1,1,1,1).  
[positiveInfinity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-positiveInfinity.html) | Shorthand for writing Vector4(float.PositiveInfinity, float.PositiveInfinity, float.PositiveInfinity, float.PositiveInfinity).  
[zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-zero.html) | Shorthand for writing Vector4(0,0,0,0).  
### Properties
Property | Description  
---|---  
[magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-magnitude.html) | Returns the length of this vector (Read Only).  
[normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-normalized.html) | Returns a normalized vector based on the current vector. The normalized vector has a magnitude of 1 and is in the same direction as the current vector. Returns a zero vector If the current vector is too small to be normalized.  
[sqrMagnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-sqrMagnitude.html) | Returns the squared length of this vector (Read Only).  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Index_operator.html) | Access the x, y, z, w components using [0], [1], [2], [3] respectively.  
[w](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-w.html) | W component of the vector.  
[x](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-x.html) | X component of the vector.  
[y](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-y.html) | Y component of the vector.  
[z](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-z.html) | Z component of the vector.  
### Constructors
Constructor | Description  
---|---  
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-ctor.html) | Creates a new vector with given x, y, z, w components.  
### Public Methods
Method | Description  
---|---  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Equals.html) | Returns true if the given vector is exactly equal to this vector.  
[Set](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Set.html) | Set x, y, z and w components of an existing Vector4.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.ToString.html) | Returns a formatted string for this vector.  
### Static Methods
Method | Description  
---|---  
[Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Distance.html) | Returns the distance between a and b.  
[Dot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Dot.html) | Dot Product of two vectors.  
[Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Lerp.html) | Linearly interpolates between two vectors.  
[LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.LerpUnclamped.html) | Linearly interpolates between two vectors.  
[Max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Max.html) | Returns a vector that is made from the largest components of two vectors.  
[Min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Min.html) | Returns a vector that is made from the smallest components of two vectors.  
[MoveTowards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.MoveTowards.html) | Moves a point current towards target.  
[Normalize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Normalize.html) | Makes this vector have a magnitude of 1.  
[Project](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Project.html) | Projects a vector onto another vector.  
[Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Scale.html) | Multiplies two vectors component-wise.  
### Operators
Operator | Description  
---|---  
[operator -](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_subtract.html) | Subtracts one vector from another.  
[operator *](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_multiply.html) | Multiplies a vector by a number.  
[operator /](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_divide.html) | Divides a vector by a number.  
[operator +](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_add.html) | Adds two vectors.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_eq.html) | Returns true if two vectors are approximately equal.  
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_Vector4.html) | Converts a Vector4 to a Vector2.  
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_Vector4.html) | Converts a Vector4 to a Vector3.  
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_Vector3.html) | Converts a Vector3 to a Vector4.  
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4-operator_Vector2.html) | Converts a Vector2 to a Vector4.  
* * *
