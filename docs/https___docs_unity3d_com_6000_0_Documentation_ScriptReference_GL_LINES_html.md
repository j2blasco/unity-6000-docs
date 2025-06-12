* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LINES.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).LINES
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
LINES; 
### Description
Mode for [Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html): draw lines.
Draws lines between each pair of vertices passed. If you pass four vertices, A, B, C and D, two lines are drawn: one between A and B, and one between C and D.  
  
To set up the screen for drawing in 2D, use [GL.LoadOrtho](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html) or [GL.LoadPixelMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadPixelMatrix.html). To set up the screen for drawing in 3D, use [GL.LoadIdentity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadIdentity.html) followed by [GL.MultMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultMatrix.html) with the desired transformation matrix.  
  
Additional resources: [GL.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html), [GL.End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) component  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draws a line from "startVertex" var to the curent mouse position.
    public Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) startVertex;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) mousePos;  
  
    void Start()
    {
        startVertex = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        mousePos = Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html);
        // Press space to update startVertex
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            startVertex = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(mousePos.x / Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), mousePos.y / Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html), 0);
        }
    }  
  
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
        GL.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Color.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
        GL.Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex.html)(startVertex);
        GL.Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex.html)(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(mousePos.x / Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html), mousePos.y / Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html), 0));
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();  
  
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

* * *
