* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.OrthoNormalize.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).OrthoNormalize
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
public static void OrthoNormalize(ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal, ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) tangent); 
### Description
Makes vectors normalized and orthogonal to each other.
Normalizes `normal`. Normalizes `tangent` and makes sure it is orthogonal to `normal` (that is, angle between them is 90 degrees).  
  
Additional resources: [Normalize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Normalize.html) function.
* * *
## Declaration
public static void OrthoNormalize(ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal, ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) tangent, ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) binormal); 
### Description
Makes vectors normalized and orthogonal to each other.
Normalizes `normal`. Normalizes `tangent` and makes sure it is orthogonal to `normal`. Normalizes `binormal` and makes sure it is orthogonal to both `normal` and `tangent`.  
  
Points in space are usually specified with coordinates in the standard XYZ axis system. However, you can interpret any three vectors as "axes" if they are normalized (ie, have a magnitude of 1) and are orthogonal (ie, perpendicular to each other).  
  
Creating your own coordinate axes is useful, say, if you want to scale a mesh in arbitrary directions rather than just along the XYZ axes - you can transform the vertices to your own coordinate system, scale them and then transform back. Often, a transformation like this will be carried out along only one axis while the other two are either left as they are or treated equally. For example, a stretching effect can be applied to a mesh by scaling up on one axis while scaling down proportionally on the other two. This means that once the first axis vector is specified, it doesn't greatly matter what the other two are as long as they are normalized and orthogonal. OrthoNormalize can be used to ensure the first vector is normal and then generate two normalized, orthogonal vectors for the other two axes.
```
// Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) "stretch" effect along a chosen axis.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The axis and amount of scaling.
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) stretchAxis;
    public float stretchFactor = 1.0F;  
  
    // MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) component and arrays for the original and transformed vertices.
    private MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) mf;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] origVerts;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] newVerts;  
  
    // Our new basis vectors.
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) basisA;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) basisB;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) basisC;  
  
    void Start()
    {
        // Get the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) Filter, then make a copy of the original vertices
        // and a new array to calculate the transformed vertices.
        mf = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>();
        origVerts = mf.mesh.vertices;
        newVerts = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[origVerts.Length];
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // BasisA is just the specified axis for stretching - the
        // other two are just arbitrary axes generated by OrthoNormalize.
        basisA = stretchAxis;
        Vector3.OrthoNormalize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.OrthoNormalize.html)(ref basisA, ref basisB, ref basisC);  
  
        // Copy the three new basis vectors into the rows of a matrix
        // (since it is actually a 4x4 matrix, the bottom right corner
        // should also be set to 1).
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) toNewSpace = new Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)();
        toNewSpace.SetRow(0, basisA);
        toNewSpace.SetRow(1, basisB);
        toNewSpace.SetRow(2, basisC);
        toNewSpace[3, 3] = 1.0F;  
  
        // The scale values are just the diagonal entries of the scale
        // matrix. The vertices should be stretched along the first axis
        // and squashed proportionally along the other two.
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) scale = new Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html)();
        scale[0, 0] = stretchFactor;
        scale[1, 1] = 1.0F / stretchFactor;
        scale[2, 2] = 1.0F / stretchFactor;
        scale[3, 3] = 1.0F;  
  
        // The inverse of the first matrix transforms the vertices back to
        // the original XYZ coordinate space(transpose is the same as inverse
        // for an orthogonal matrix, which this is).
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) fromNewSpace = toNewSpace.transpose;  
  
        // The three matrices can now be combined into a single symmetric matrix.
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) trans = toNewSpace * scale * fromNewSpace;  
  
        // Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) each of the mesh's vertices by the symmetric matrix.
        int i = 0;
        while (i < origVerts.Length)
        {
            newVerts[i] = trans.MultiplyPoint3x4(origVerts[i]);
            i++;
        }  
  
        // ...and finally, update the mesh with the new vertex array.
        mf.mesh.vertices = newVerts;
    }
}

```

Additional resources: [Normalize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Normalize.html) function.
* * *
