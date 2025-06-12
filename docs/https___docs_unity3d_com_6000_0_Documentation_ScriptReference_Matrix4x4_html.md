* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html

# Matrix4x4
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
A standard 4x4 transformation matrix.
A transformation matrix can perform arbitrary linear 3D transformations (i.e. translation, rotation, scale, shear etc.) and perspective transformations using homogenous coordinates. You rarely use matrices in scripts; most often using [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)s, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)s and functionality of [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) class is more straightforward. Plain matrices are used in special cases like setting up nonstandard camera projection.  
  
In Unity, several [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html), [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html), [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html), [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html) and [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html) functions use Matrix4x4.  
  
Matrices in Unity are column major; i.e. the position of a transformation matrix is in the last column, and the first three columns contain x, y, and z-axes. Data is accessed as: `row + (column*4)`. Matrices can be indexed like 2D arrays but note that in an expression like `mat[a, b]`, `a` refers to the row index, while `b` refers to the column index.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // get matrix from the Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)
        var matrix = transform.localToWorldMatrix;
        // get position from the last column
        var position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(matrix[0,3], matrix[1,3], matrix[2,3]);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) position from matrix is: " + position);
    }
}

```

### Static Properties
Property | Description  
---|---  
[identity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-identity.html) | Returns the identity matrix (Read Only).  
[zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-zero.html) | Returns a matrix with all elements set to zero (Read Only).  
### Properties
Property | Description  
---|---  
[decomposeProjection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-decomposeProjection.html) | This property takes a projection matrix and returns the six plane coordinates that define a projection frustum.  
[determinant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-determinant.html) | The determinant of the matrix. (Read Only)  
[inverse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-inverse.html) | The inverse of this matrix. (Read Only)  
[isIdentity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-isIdentity.html) | Checks whether this is an identity matrix. (Read Only)  
[lossyScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-lossyScale.html) | Attempts to get a scale value from the matrix. (Read Only)  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-rotation.html) | Attempts to get a rotation quaternion from this matrix.  
[this[int,int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Index_operator.html) | Access element at [row, column].  
[transpose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-transpose.html) | Returns the transpose of this matrix (Read Only).  
### Public Methods
Method | Description  
---|---  
[GetColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.GetColumn.html) | Get a column of the matrix.  
[GetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.GetPosition.html) | Get position vector from the matrix.  
[GetRow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.GetRow.html) | Returns a row of the matrix.  
[MultiplyPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.MultiplyPoint.html) | Transforms a position by this matrix (generic).  
[MultiplyPoint3x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.MultiplyPoint3x4.html) | Transforms a position by this matrix (fast).  
[MultiplyVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.MultiplyVector.html) | Transforms a direction by this matrix.  
[SetColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.SetColumn.html) | Sets a column of the matrix.  
[SetRow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.SetRow.html) | Sets a row of the matrix.  
[SetTRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.SetTRS.html) | Sets this matrix to a translation, rotation and scaling matrix.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.ToString.html) | Returns a formatted string for this matrix.  
[TransformPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TransformPlane.html) | Returns a plane that is transformed in space.  
[ValidTRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.ValidTRS.html) | Checks if this matrix is a valid transform matrix.  
### Static Methods
Method | Description  
---|---  
[Frustum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Frustum.html) | This function returns a projection matrix with viewing frustum that has a near plane defined by the coordinates that were passed in.  
[Inverse3DAffine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Inverse3DAffine.html) | Computes the inverse of a 3D affine matrix.  
[LookAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.LookAt.html) | Create a "look at" matrix.  
[Ortho](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Ortho.html) | Create an orthogonal projection matrix.  
[Perspective](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Perspective.html) | Create a perspective projection matrix.  
[Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Rotate.html) | Creates a rotation matrix.  
[Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Scale.html) | Creates a scaling matrix.  
[Translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html) | Creates a translation matrix.  
[TRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html) | Creates a translation, rotation and scaling matrix.  
### Operators
Operator | Description  
---|---  
[operator *](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-operator_multiply.html) | Multiplies two matrices.  
* * *
