* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html

# GL
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Low-level graphics library.
Use this class to manipulate active transformation matrices, issue rendering commands similar to OpenGL's immediate mode and do other low-level graphics tasks. Note that in almost all cases using [Graphics.RenderMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html) or [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) is more efficient than using immediate mode drawing.  
  
GL immediate drawing functions use whatever is the "current material" set up right now (see [Material.SetPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetPass.html)). The material controls how the rendering is done (blending, textures, etc.), so unless you explicitly set it to something before using GL draw functions, the material can happen to be anything. Also, if you call any other drawing commands from inside GL drawing code, they can set material to something else, so make sure it's under control as well.  
  
GL drawing commands execute immediately. That means if you call them in Update(), they will be executed before the camera is rendered (and the camera will most likely clear the screen, making the GL drawing not visible).  
  
The usual place to call GL drawing is most often in [OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPostRender.html)() from a script attached to a camera, or inside an image effect function ([OnRenderImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnRenderImage.html)).  
  
**Note:** The High Definition Render Pipeline (HDRP) and the Universal Render Pipeline (URP) do not support [OnPostRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.OnPostRender.html). Instead, use [RenderPipelineManager.endCameraRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endCameraRendering.html) or [RenderPipelineManager.endFrameRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager-endFrameRendering.html).  
  

```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // When added to an object, draws colored rays from the
    // transform position.
    public int lineCount = 100;
    public float radius = 3.0f;  
  
    static Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) lineMaterial;
    static void CreateLineMaterial()
    {
        if (!lineMaterial)
        {
            // Unity has a built-in shader that is useful for drawing
            // simple colored things.
            Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Hidden/Internal-Colored");
            lineMaterial = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(shader);
            lineMaterial.hideFlags = HideFlags.HideAndDontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideAndDontSave.html);
            // Turn on alpha blending
            lineMaterial.SetInt("_SrcBlend", (int)UnityEngine.Rendering.BlendMode.SrcAlpha);
            lineMaterial.SetInt("_DstBlend", (int)UnityEngine.Rendering.BlendMode.OneMinusSrcAlpha);
            // Turn backface culling off
            lineMaterial.SetInt("_Cull", (int)UnityEngine.Rendering.CullMode.Off);
            // Turn off depth writes
            lineMaterial.SetInt("_ZWrite", 0);
        }
    }  
  
    // Will be called after all regular rendering is done
    public void OnRenderObject()
    {
        CreateLineMaterial();
        // Apply the line material
        lineMaterial.SetPass(0);  
  
        GL.PushMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html)();
        // Set transformation matrix for drawing to
        // match our transform
        GL.MultMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultMatrix.html)(transform.localToWorldMatrix);  
  
        // Draw lines
        GL.Begin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html)(GL.LINES[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LINES.html));
        for (int i = 0; i < lineCount; ++i)
        {
            float a = i / (float)lineCount;
            float angle = a * Mathf.PI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.PI.html) * 2;
            // Vertex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) colors change from red to green
            GL.Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Color.html)(new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(a, 1 - a, 0, 0.8F));
            // One vertex at transform position
            GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(0, 0, 0);
            // Another vertex at edge of circle
            GL.Vertex3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html)(Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(angle) * radius, Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(angle) * radius, 0);
        }
        GL.End[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html)();
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

**Note:** This class is almost always used when you need to draw a couple of lines or triangles, and don't want to deal with meshes. If you want to avoid surprises the usage pattern is this:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnPostRender()
    {
        // Set your materials
        GL.PushMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html)();
        // yourMaterial.SetPass( );
        // Draw your stuff
        GL.PopMatrix[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html)();
    }
}

```

Where at the "// Draw your stuff" you should do SetPass() on some material previously declared, which will be used for drawing. If you dont call SetPass, then you'll get basically a random material (whatever was used before) which is not good. So do it.
### Static Properties
Property | Description  
---|---  
[invertCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-invertCulling.html) | Select whether to invert the backface culling (true) or not (false).  
[LINE_STRIP](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LINE_STRIP.html) | Mode for Begin: draw line strip.  
[LINES](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LINES.html) | Mode for Begin: draw lines.  
[modelview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-modelview.html) | Gets or sets the modelview matrix.  
[QUADS](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.QUADS.html) | Mode for Begin: draw quads.  
[sRGBWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-sRGBWrite.html) | Controls whether Linear-to-sRGB color conversion is performed while rendering.  
[TRIANGLE_STRIP](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TRIANGLE_STRIP.html) | Mode for Begin: draw triangle strip.  
[TRIANGLES](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TRIANGLES.html) | Mode for Begin: draw triangles.  
[wireframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL-wireframe.html) | Should rendering be done in wireframe?  
### Static Methods
Method | Description  
---|---  
[Begin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Begin.html) | Begin drawing 3D primitives.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Clear.html) | Clear the current render buffer.  
[ClearWithSkybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.ClearWithSkybox.html) | Clear the current render buffer with camera's skybox.  
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Color.html) | Sets current vertex color.  
[End](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.End.html) | End drawing 3D primitives.  
[Flush](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Flush.html) | Sends queued-up commands in the driver's command buffer to the GPU.  
[GetGPUProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.GetGPUProjectionMatrix.html) | Compute GPU projection matrix from camera's projection matrix.  
[InvalidateState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.InvalidateState.html) | Invalidate the internally cached render state.  
[IssuePluginEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.IssuePluginEvent.html) | Send a user-defined event to a native code plugin.  
[LoadIdentity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadIdentity.html) | Load an identity into the current model and view matrices.  
[LoadOrtho](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadOrtho.html) | Helper function to set up an orthograhic projection.  
[LoadPixelMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadPixelMatrix.html) | Setup a matrix for pixel-correct rendering.  
[LoadProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.LoadProjectionMatrix.html) | Load an arbitrary matrix to the current projection matrix.  
[MultiTexCoord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord.html) | Sets current texture coordinate (v.x,v.y,v.z) to the actual texture unit.  
[MultiTexCoord2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord2.html) | Sets current texture coordinate (x,y) for the actual texture unit.  
[MultiTexCoord3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultiTexCoord3.html) | Sets current texture coordinate (x,y,z) to the actual texture unit.  
[MultMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.MultMatrix.html) | Sets the current model matrix to the one specified.  
[PopMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PopMatrix.html) | Restores the model, view and projection matrices off the top of the matrix stack.  
[PushMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.PushMatrix.html) | Saves the model, view and projection matrices to the top of the matrix stack.  
[RenderTargetBarrier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.RenderTargetBarrier.html) | Resolves the render target for subsequent operations sampling from it.  
[TexCoord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TexCoord.html) | Sets current texture coordinate (v.x,v.y,v.z) for all texture units.  
[TexCoord2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TexCoord2.html) | Sets current texture coordinate (x,y) for all texture units.  
[TexCoord3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.TexCoord3.html) | Sets current texture coordinate (x,y,z) for all texture units.  
[Vertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex.html) | Submit a vertex.  
[Vertex3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Vertex3.html) | Submit a vertex.  
[Viewport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.Viewport.html) | Set the rendering viewport.  
* * *
