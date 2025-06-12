* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetPass.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).SetPass
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
## Declaration
public bool SetPass(int pass); 
### Parameters
Parameter | Description  
---|---  
pass | Shader pass number to setup.  
### Returns
**bool** If false is returned, no rendering should be done. 
### Description
Activate the given `pass` for rendering.
Pass indices start from zero and go up to (but not including) [passCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-passCount.html).  
  
This is mostly used in direct drawing code. For example, drawing 3D primitives with [GL.Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html), [GL.End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html), and also drawing meshes using [Graphics.DrawMeshNow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawMeshNow.html).  
  
If SetPass returns false, you should not render anything. This is typically the case for special pass types that aren't meant for rendering, like [GrabPass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GrabPass.html).
```
using UnityEngine;  
  
// A script that when attached to the camera, makes the resulting
// colors inverted. See its effect in play mode.
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat;  
  
    // Will be called from camera after regular rendering is done.
    public void OnPostRender()
    {
        if (!mat)
        {
            // Unity has a built-in shader that is useful for drawing
            // simple colored things. In this case, we just want to use
            // a blend mode that inverts destination colors.
            Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Hidden/Internal-Colored");
            mat = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(shader);
            mat.hideFlags = HideFlags.HideAndDontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html);
            // Set blend mode to invert destination colors.
            mat.SetInt("_SrcBlend", (int)UnityEngine.Rendering.BlendMode.OneMinusDstColor);
            mat.SetInt("_DstBlend", (int)UnityEngine.Rendering.BlendMode.Zero);
            // Turn off backface culling, depth writes, depth test.
            mat.SetInt("_Cull", (int)UnityEngine.Rendering.CullMode.Off);
            mat.SetInt("_ZWrite", 0);
            mat.SetInt("_ZTest", (int)UnityEngine.Rendering.CompareFunction.Always);
        }  
  
        GL.PushMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html)();
        GL.LoadOrtho[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html)();  
  
        // activate the first shader pass (in this case we know it is the only pass)
        mat.SetPass(0);
        // draw a quad over whole screen
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.QUADS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.QUADS.html));
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 0, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(1, 0, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(1, 1, 0);
        GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 1, 0);
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();  
  
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

Additional resources: [passCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-passCount.html) property, [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html) class, [ShaderLab documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
* * *
