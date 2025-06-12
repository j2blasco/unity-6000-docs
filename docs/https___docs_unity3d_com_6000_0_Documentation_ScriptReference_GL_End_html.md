* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).End
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
public static void End(); 
### Description
End drawing 3D primitives.
In OpenGL this matches `glEnd`; on other graphics APIs the same functionality is emulated.  
  
Additional resources: [GL.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a Triangle, a Quad and a line
    // with different colors  
  
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;
    void  OnPostRender()
    {
        if (!mat)
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Please Assign a material on the inspector");
            return;
        }
        GL.PushMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html)();
        mat.SetPass(0);
        GL.LoadOrtho[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html)();  
  
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.TRIANGLES[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TRIANGLES.html)); // Triangle
        GL.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Color.html)(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(1, 1, 1, 1));
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.50f, 0.25f, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.25f, 0.25f, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.375f, 0.5f, 0);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)(); // End drawing Triangle  
  
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.QUADS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.QUADS.html)); // Quad
        GL.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Color.html)(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.5f, 0.5f, 0.5f, 1));
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.5f, 0.5f, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.5f, 0.75f, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.75f, 0.75f, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.75f, 0.5f, 0);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)(); // End drawing quad  
  
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.LINES[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LINES.html)); // Line
        GL.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Color.html)(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0, 0, 0, 1));
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 0, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.75f, 0.75f, 0);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)(); // End drawing Line  
  
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

* * *
