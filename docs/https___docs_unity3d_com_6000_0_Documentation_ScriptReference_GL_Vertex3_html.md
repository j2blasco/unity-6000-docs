* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).Vertex3
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
public static void Vertex3(float x, float y, float z); 
### Description
Submit a vertex.
In OpenGL this matches `glVertex3f(x,y,z)`; on other graphics APIs the same functionality is emulated.  
  
This function can only be called between [GL.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html) and [GL.End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html) functions.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a line from the bottom right
    // to the top left of the Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html)
    // Using GL.Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex.html)
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
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.LINES[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LINES.html));
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 0, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(1, 1, 0);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

* * *
