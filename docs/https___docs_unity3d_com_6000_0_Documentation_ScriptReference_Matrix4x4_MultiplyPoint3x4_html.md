* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.MultiplyPoint3x4.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).MultiplyPoint3x4
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) MultiplyPoint3x4([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point); 
### Description
Transforms a position by this matrix (fast).
Returns a position `v` transformed by the current transformation matrix. This function is a faster version of [MultiplyPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.MultiplyPoint.html); but it can only handle regular 3D transformations. `MultiplyPoint` is slower, but can handle projective transformations as well.  
  
Additional resources: [MultiplyPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.MultiplyPoint.html), [MultiplyVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.MultiplyVector.html).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Stretch a mesh at an arbitrary angle around the X axis.  
  
    // Angle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Angle.html) and amount of stretching.
    float rotAngle;
    float stretch;  
  

    MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) mf;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] origVerts;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] newVerts;  
  

    void Start()
    {
        // Get the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) Filter component, save its original vertices
        // and make a new vertex array for processing.
        mf = GetComponent< MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) > ();
        origVerts = mf.mesh.vertices;
        newVerts = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[origVerts.Length];
    }  
  

    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Create a rotation matrix from a Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rot = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(rotAngle, 0, 0);
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) m = Matrix4x4.TRS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), rot, Vector3.one[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-one.html));  
  
        // Get the inverse of the matrix (ie, to undo the rotation).
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) inv = m.inverse;  
  
        // For each vertex...
        for (var i = 0; i < origVerts.Length; i++)
        {
            // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the vertex and scale it along its new Y axis.
            var pt = m.MultiplyPoint3x4(origVerts[i]);
            pt.y *= stretch;  
  
            // Return the vertex to its original rotation (but with the
            // scaling still applied).
            newVerts[i] = inv.MultiplyPoint3x4(pt);
        }  
  
        // Copy the transformed vertices back to the mesh.
        mf.mesh.vertices = newVerts;
    }
}

```

* * *
