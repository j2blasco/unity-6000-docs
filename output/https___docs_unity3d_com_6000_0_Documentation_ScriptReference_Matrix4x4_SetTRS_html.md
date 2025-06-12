* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.SetTRS.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).SetTRS
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
public void SetTRS([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) q, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) s); 
### Description
Sets this matrix to a translation, rotation and scaling matrix.
The current matrix is modified so that it places objects at position `pos`, oriented in rotation `q` and scaled by `s`.
```
// Translate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Translate.html), rotate and scale a mesh. Try varying
// the parameters in the inspector while running
// to see the effect they have.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) translation;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) eulerAngles;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1, 1, 1);
    private MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) mf;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] origVerts;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] newVerts;  
  
    void Start() {
        mf = GetComponent<MeshFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html)>();
        origVerts = mf.mesh.vertices;
        newVerts = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[origVerts.Length];
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() {
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(eulerAngles.x, eulerAngles.y, eulerAngles.z);
        Matrix4x4[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) m = Matrix4x4.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-identity.html);
        m.SetTRS(translation, rotation, scale);
        int i = 0;
        while (i < origVerts.Length) {
            newVerts[i] = m.MultiplyPoint3x4(origVerts[i]);
            i++;
        }
        mf.mesh.vertices = newVerts;
    }
}

```

Additional resources: [TRS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.TRS.html), [Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Rotate.html), [Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Scale.html), [Translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Translate.html) functions.
* * *
