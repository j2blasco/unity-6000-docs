* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).MultiTexCoord3
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
public static void MultiTexCoord3(int unit, float x, float y, float z); 
### Description
Sets current texture coordinate (x,y,z) to the actual texture `unit`.
In OpenGL this matches `glMultiTexCoord` for the given texture unit if multi-texturing is available. On other graphics APIs the same functionality is emulated.  
  
The Z component is used only when:  
**1.** You access a cubemap (which you access with a vector coordinate, hence x,y & z).  
**2.** You do "projective texturing", where the X & Y coordinates are divided by Z to get the final coordinate. This would be mostly useful for water reflections and similar things.  
  
This function can only be called between [GL.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html) and [GL.End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html) functions.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Changes between two textures assigned to a material
    // When pressed space
    Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;
    bool flagTex = true;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
        {
            if (flagTex)
            {
                flagTex = false;
            }
            else
            {
                flagTex = true;
            }
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
        mat.SetPass(1);
        GL.LoadOrtho[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html)();
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.QUADS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.QUADS.html));
        if (flagTex)
        {
            GL.MultiTexCoord3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html)(0, 0, 0, 0); // main texture
        }
        else
        {
            GL.MultiTexCoord3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html)(1, 0, 0, 0); // second texture
        }
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.25f, 0.25f, 0);
        if (flagTex)
        {
            GL.MultiTexCoord3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html)(0, 0, 1, 0);
        }
        else
        {
            GL.MultiTexCoord3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html)(1, 0, 1, 0);
        }
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.25f, 0.75f, 0);
        if (flagTex)
        {
            GL.MultiTexCoord3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html)(0, 1, 1, 0);
        }
        else
        {
            GL.MultiTexCoord3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html)(1, 1, 1, 0);
        }
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.75f, 0.75f, 0);
        if (flagTex)
        {
            GL.MultiTexCoord3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html)(0, 1, 0, 0);
        }
        else
        {
            GL.MultiTexCoord3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html)(1, 1, 0, 0);
        }
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0.75f, 0.25f, 0);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

* * *
