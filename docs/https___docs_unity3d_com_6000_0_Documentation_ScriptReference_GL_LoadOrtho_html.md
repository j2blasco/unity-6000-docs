* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).LoadOrtho
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
public static void LoadOrtho(); 
### Description
Helper function to set up an orthograhic projection.
Loads an orthographic projection into the projection matrix and loads an identity into the model and view matrices.  
  
The resulting projection performs the following mappings:  
**1.** x = 0..1 to x = -1..1 (left..right)  
**2.** y = 0..1 to y = -1..1 (bottom..top)  
**3.** z = 1..-100 to z = -1..1 (near..far)  
  
This is equivalent to the following operations:
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnPostRender()
    {
        // ...  
  
        GL.LoadOrtho[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html)();  
  
        // is equivalent to:  
  
        GL.LoadIdentity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadIdentity.html)();
        var proj = Matrix4x4.Ortho[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Ortho.html)(0, 1, 0, 1, -1, 100);
        GL.LoadProjectionMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadProjectionMatrix.html)(proj);  
  
        // ...
    }
}

```

Changing the model, view or projection matrices overrides the current rendering matrices. It is good practice to save and restore these matrices using [GL.PushMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html) and [GL.PopMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a triangle under an already drawn triangle
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;  
  
    void OnPostRender()
    {
        if (!mat)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Please Assign a material on the inspector");
            return;
        }
        GL.PushMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html)();
        mat.SetPass(0);
        GL.LoadOrtho[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html)();
        GL.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Color.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.TRIANGLES[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TRIANGLES.html));
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.25f, 0.1351f, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.25f, 0.3f, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.5f, 0.3f, 0);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();  
  
        GL.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Color.html)(Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html));
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.TRIANGLES[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TRIANGLES.html));
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.5f, 0.25f, -1);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.5f, 0.1351f, -1);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.1f, 0.25f, -1);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();  
  
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

Additional resources: [GL.LoadProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadProjectionMatrix.html), [Matrix4x4.Ortho](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Ortho.html).
* * *
