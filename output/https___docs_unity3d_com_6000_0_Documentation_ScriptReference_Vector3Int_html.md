* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html

# Vector3Int
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
Representation of 3D vectors and points using integers.
This structure is used in some places to represent 3D positions and vectors that don't require the precision of floating-point.
### Static Properties
Property | Description  
---|---  
[back](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-back.html) | Shorthand for writing Vector3Int(0, 0, -1).  
[down](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-down.html) | Shorthand for writing Vector3Int(0, -1, 0).  
[forward](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-forward.html) | Shorthand for writing Vector3Int(0, 0, 1).  
[left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-left.html) | Shorthand for writing Vector3Int(-1, 0, 0).  
[one](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-one.html) | Shorthand for writing Vector3Int(1, 1, 1).  
[right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-right.html) | Shorthand for writing Vector3Int(1, 0, 0).  
[up](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-up.html) | Shorthand for writing Vector3Int(0, 1, 0).  
[zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-zero.html) | Shorthand for writing Vector3Int(0, 0, 0).  
### Properties
Property | Description  
---|---  
[magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-magnitude.html) | Returns the length of this vector (Read Only).  
[sqrMagnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-sqrMagnitude.html) | Returns the squared length of this vector (Read Only).  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.Index_operator.html) | Access the x, y or z component using [0], [1] or [2] respectively.  
[x](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-x.html) | X component of the vector.  
[y](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-y.html) | Y component of the vector.  
[z](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-z.html) | Z component of the vector.  
### Constructors
Constructor | Description  
---|---  
[Vector3Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-ctor.html) | Initializes and returns an instance of a new Vector3Int with x, y, z components.  
### Public Methods
Method | Description  
---|---  
[Clamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.Clamp.html) | Clamps the Vector3Int to the bounds given by min and max.  
[Equals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.Equals.html) | Returns true if the objects are equal.  
[GetHashCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.GetHashCode.html) | Gets the hash code for the Vector3Int.  
[Set](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.Set.html) | Set x, y and z components of an existing Vector3Int.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.ToString.html) | Returns a formatted string for this vector.  
### Static Methods
Method | Description  
---|---  
[CeilToInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.CeilToInt.html) | Converts a Vector3 to a Vector3Int by doing a Ceiling to each value.  
[Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.Distance.html) | Returns the distance between a and b.  
[FloorToInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.FloorToInt.html) | Converts a Vector3 to a Vector3Int by doing a Floor to each value.  
[Max](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.Max.html) | Returns a vector that is made from the largest components of two vectors.  
[Min](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.Min.html) | Returns a vector that is made from the smallest components of two vectors.  
[RoundToInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.RoundToInt.html) | Converts a Vector3 to a Vector3Int by doing a Round to each value.  
[Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.Scale.html) | Multiplies two vectors component-wise.  
### Operators
Operator | Description  
---|---  
[operator -](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-operator_subtract.html) | Subtracts one vector from another.  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-operator_ne.html) | Returns true if vectors different.  
[operator *](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-operator_multiply.html) | Multiplies a vector by a number.  
[operator /](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-operator_divide.html) | Divides a vector by a number.  
[operator +](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-operator_add.html) | Adds two vectors.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-operator_eq.html) | Returns true if the vectors are equal.  
[Vector2Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-operator_Vector2Int.html) | Converts a Vector3Int to a Vector2Int.  
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int-operator_Vector3Int.html) | Converts a Vector3Int to a Vector3.  
* * *
