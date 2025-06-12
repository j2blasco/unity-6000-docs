* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPostRender.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnPostRender()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
[Event function](https://docs.unity3d.com/6000.0/Documentation/Manual/event-functions.html) that Unity calls after a Camera renders the scene.
In the Built-in Render Pipeline, Unity calls `OnPostRender` on MonoBehaviours that are attached to the same GameObject as an enabled [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) component, just after that Camera renders the scene. Use `OnPostRender` to execute your own code at this point in the render loop; for example, if you changed a visual effect in [MonoBehaviour.OnPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreRender.html), you can change it back here. `OnPostRender` can be a coroutine.  
  
For similar functionality that does not require the script to be on the same GameObject as a Camera component, see [Camera.onPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html). For similar functionality in the Scriptable Render Pipeline, see [RenderPipelineManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html).  
  
To execute code after Unity renders all Cameras and GUI, use [WaitForEndOfFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html) or a [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).
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
            var shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Hidden/Internal-Colored");
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
Additional resources: [Camera.onPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-onPostRender.html), [MonoBehaviour.OnPreRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreRender.html), [MonoBehaviour.OnPreCull](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnPreCull.html), [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html), [Extending the Built-in Render Pipeline using CommandBuffers](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers.html), [WaitForEndOfFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html).
* * *
