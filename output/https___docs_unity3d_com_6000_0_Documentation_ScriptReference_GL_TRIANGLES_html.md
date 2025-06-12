* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TRIANGLES.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).TRIANGLES
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
TRIANGLES; 
### Description
Mode for [Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html): draw triangles.
Draws triangles using each set of 3 vertices passed. If you pass 3 vertices, one triangle is drawn, where each vertex becomes one corner of the triangle. If you pass 6 vertices, 2 triangles will be drawn.  
  
To set up the screen for drawing in 2D, use [GL.LoadOrtho](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html) or [GL.LoadPixelMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadPixelMatrix.html). To set up the screen for drawing in 3D, use [GL.LoadIdentity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadIdentity.html) followed by [GL.MultMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultMatrix.html) with the desired transformation matrix.  
  
Additional resources: [GL.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html), [GL.End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a triangle that covers the middle of the screen
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
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.TRIANGLES[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TRIANGLES.html));
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 0, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(1, 1, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 1, 0);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

* * *
