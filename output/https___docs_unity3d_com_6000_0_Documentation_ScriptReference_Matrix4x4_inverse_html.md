* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-inverse.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).inverse
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
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) inverse; 
### Description
The inverse of this matrix. (Read Only)
Inverted matrix is such that if multiplied by the original would result in [identity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-identity.html) matrix.  
  
If as matrix transforms vectors in a particular way, then the inverse matrix can transform them back. For example, Transform's [worldToLocalMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-worldToLocalMatrix.html) and [localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localToWorldMatrix.html) are inverses of each other.  
  
For regular 3D transformation matrices, it can be faster to use [Inverse3DAffine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Inverse3DAffine.html) method.  
  
You can not invert a matrix with a [determinant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-determinant.html) of zero. If you attempt this, `inverse` returns [Matrix4x4.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-zero.html) instead.
```
using UnityEngine;  
  
// Stretch a mesh at an arbitrary angle around the X axis
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)))]
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Angle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Angle.html) and amount of stretching
    public float rotAngle = 30;
    public float stretch = 3;  
  

    MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) mf;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] origVerts;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] newVerts;  
  
    void Start()
    {
        // Get the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) Filter component, save its original vertices
        // and make a new vertex array for processing.
        mf = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>();
        origVerts = mf.mesh.vertices;
        newVerts = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[origVerts.Length];
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Create a rotation matrix from a Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rot = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(rotAngle, 0, 0);
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) m = Matrix4x4.TRS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), rot, Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html));  
  
        // Get the inverse of the matrix: undo the rotation
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) inv = m.inverse;  
  
        // For each vertex:
        for (var i = 0; i < origVerts.Length; i++)
        {
            // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the vertex and scale it along its new Y axis
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pt = m.MultiplyPoint3x4(origVerts[i]);
            pt.y *= stretch;  
  
            // Return the vertex to its original rotation (but with the
            // scaling still applied).
            newVerts[i] = inv.MultiplyPoint3x4(pt);
        }  
  
        // Assign the transformed vertices to the mesh
        mf.mesh.vertices = newVerts;
    }
}
```

Additional resources: [Inverse3DAffine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Inverse3DAffine.html), [determinant](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-determinant.html).
* * *
