* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).TRS
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
public static [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) TRS([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) q, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) s); 
### Description
Creates a translation, rotation and scaling matrix.
The returned matrix is such that it places objects at position `pos`, oriented in rotation `q` and scaled by `s`.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Translate.html), rotate and scale a mesh. Try altering
    // the parameters in the inspector while running
    // to see the effect they have.  
  
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) translation;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) eulerAngles;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 1, 1);  
  

    MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) mf;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] origVerts;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] newVerts;  
  

    void Start()
    {
        // Get the Mesh[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) Filter component, save its original vertices
        // and make a new vertex array for processing.
        mf = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)> ();
        origVerts = mf.mesh.vertices;
        newVerts = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[origVerts.Length];
    }  
  

    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Set a Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) from the specified Euler angles.
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(eulerAngles.x, eulerAngles.y, eulerAngles.z);  
  
        // Set the translation, rotation and scale parameters.
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) m = Matrix4x4.TRS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html)(translation, rotation, scale);  
  
        // For each vertex...
        for (int i = 0; i < origVerts.Length; i++)
        {
            // Apply the matrix to the vertex.
            newVerts[i] = m.MultiplyPoint3x4(origVerts[i]);
        }  
  
        // Copy the transformed vertices back to the mesh.
        mf.mesh.vertices = newVerts;
    }
}

```

Additional resources: [TRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html), [Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Rotate.html), [Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Scale.html), [Translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html), [SetTRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.SetTRS.html) functions.
* * *
