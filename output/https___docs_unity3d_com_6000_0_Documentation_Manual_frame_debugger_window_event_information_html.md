* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling reference](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-landing.html)
  * Frame Debugger Event Information reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window.html)
Frame Debugger window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html)
Rendering Statistics window reference
# Frame Debugger Event Information reference
The Event Information Panel in the [Frame Debugger window](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window.html) displays information about the event such as geometry details and the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) used for a draw call.
![The Event Information Panel showing the URP sample scene. The top bar has selectors for the render target, color channels, and levels \(A, B, and C\). The central area is the mesh preview \(D\). The bottom area lists event properties \(E\).](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/frame-debugger-window-event-information.png) The Event Information Panel showing the URP sample scene. The top bar has selectors for the render target, color channels, and levels (A, B, and C). The central area is the mesh preview (D). The bottom area lists event properties (E). **Label** | **Description**  
---|---  
**A** |  **Render target selector** : When rendering into multiple render targets (such as multiple [RenderTextures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html) or when also rendering to depth), this specifies which render target to display in the Game view. This is useful for example to view individual render targets in a G-buffer.  
**B** |  **Color channel selector** : Specifies which color channels of the render target to display.  
**C** |  **Levels** : Controls the black and white intensity. Use this to isolate areas of the Game view based on light intensity.  
**D** |  **Output /**Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Preview**: Displays a preview of the selected event output as well as the mesh geometry in the event. For more information, see [Preview](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#preview).  
**E** |  **Event properties** : Contains further information about the selected event. For more information, see [Event properties](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#event-properties).  
## Preview
The preview section consists of two tabs:
  * The **Output** tab displays a preview of the selected event output.
  * The **Mesh Preview** tab displays the mesh geometry Unity rendered in the event.

![The mesh preview tab displaying the power jigsaw mesh from the URP sample scene. The mesh preview \(A\) is in the centre. The bottom bar has the mesh name \(B\), the preview mode \(C\), and the toggle for wireframe \(D\).](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/frame-debugger-mesh-preview.png) The mesh preview tab displaying the power jigsaw mesh from the URP sample scene. The mesh preview (A) is in the centre. The bottom bar has the mesh name (B), the preview mode (C), and the toggle for wireframe (D). **Label** | **Description**  
---|---  
**A** |  **Preview** : A preview of the mesh geometry Unity rendered during the event.  
**B** |  **Mesh name** : The name of the mesh asset in the preview. Click on the mesh name to take see the mesh asset in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow). If the geometry was procedural and there is no mesh asset associated, this is empty (Unity displays **-**).  
**C** |  **Preview mode** : Specifies how the preview renders the mesh. For more information, refer to [Preview mode dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#preview-mode-dropdown).  
**D** |  **Wireframe toggle** : Toggles the mesh wireframe on and off. When enabled, the preview displays the mesh vertices and edges.  
### Preview mode dropdown
**Value** | **Description**  
---|---  
**Shaded** | Renders the mesh using its material and a basic light.  
**UV Checker** | Applies a checkerboard texture to the mesh to visualize how the mesh’s UV map applies textures.  
**UV Layout** | Displays how the vertices of the mesh are organized in the unwrapped UV map. This view disables the Wireframe toggle.  
**Vertex Color** | Visualizes any vertex colors that the vertices in this mesh have. If no vertices have a vertex color, this option is unavailable.  
**Normals** | Visualizes the relative directions of the normals in the mesh with color.  
**Tangents** | Visualizes the tangent data in the mesh with color.  
**Blendshapes** | Visualizes blend shape deformations on the mesh. If the mesh has no blend shapes, this option is unavailable.  
## Event properties
The event properties section contains properties and values for the selected event. It has a **Details** fold-out section that contains information about the event itself and then a fold-out section for each type of shader property. If the fold-out section is grayed-out, it means that the shader in the event didn’t contain any properties of that type. For more information on the information that each section displays, see:
  * [Details](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#details)
  * [Keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#keywords)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#textures)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture)
  * [Ints](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#ints)
  * [Floats](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#floats)
  * [Vectors](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#vectors)
  * [Matrices](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#matrices)
  * [Buffers](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#buffers)
  * [Constant Buffers](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#constant-buffers)


**Note** : When using OpenGL and GLSL shaders, this panel displays all shader properties as being part of the vertex stage.
### Details
The **Details** section displays information about the rendering event, such as the number of draw calls as well as the meshes that Unity rendered and the shader it used to render them.
**Property** | **Description**  
---|---  
**RenderTarget** | The name of the render target  
**Size** | The size of the render target.  
**Format** | The [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) for the render target.  
**Color Actions** | Shows which actions to perform on the color target when:
  * The GPU first loads the color target: For more information, see [RenderBufferLoadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.html).
  * The GPU finishes rendering to the color target: For more information, see [RenderBufferStoreAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.html).

  
**Depth Actions** | Shows which actions to perform on the depth target when:
  * The GPU first loads the depth target: For more information, see [RenderBufferLoadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.html).
  * The GPU finishes rendering to the depth target: For more information, see [RenderBufferStoreAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.html).

  
**Memoryless** | The **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) [memoryless mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureMemoryless.html) mode. For more information, see [memoryless](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor-memoryless.html).  
**ColorMask** | The color channel mask used for the render target. For more information, see [ColorMask](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ColorMask.html).  
**Blend Color** | The [color blending](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Blend.html) method Unity used during the selected event.  
**Blend Alpha** | The [alpha blending](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Blend.html) method Unity used during the selected event.  
**BlendOp Color** | The [color blending operation](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BlendOp.html) Blend Color used.  
**BlendOp Alpha** | The [alpha blending operation](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BlendOp.html) Blend Alpha used.  
**Draw Calls** | The number of draw calls Unity processed during the selected event.  
**Vertices** | The number of vertices Unity processed during the select event.  
**Indices** | The number of indices Unity processed during the select event.  
**Clear Color** | The color Unity used to clear the render target during the selected event. If Unity didn’t clear the render target, the display doesn’t show a color here.  
**Clear Depth** | The color Unity used to clear the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer) during the selected event. If Unity didn’t clear the depth buffer, the display doesn’t show a color here.  
**Clear Stencil** | The color Unity used to clear the **stencil buffer** A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#stencilbuffer) during the selected event. If Unity didn’t clear the stencil buffer, the display doesn’t show a color here.  
**Batch cause** | The reason why the SRP Batcher was unable to batch the selected rendering event with the previous rendering event.   
This is only relevant if your application uses the [SRP Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher.html).  
**Meshes** | The list of meshes that Unity rendered during the selected event.  
**Pass** | The [shader Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html) Unity used.  
**LightMode** | The LightMode [pass tag](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html) Unity used during the selected event.  
**Used Shader** | The [shader asset](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html) Unity used during the selected event. This can sometimes be different than the original shader, for example when the original shader uses a [fallback shader](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html) or [USEPASS](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html).  
**Original Shader** | The original shader Unity used with the pass.  
**ZClip** | The shader’s [depth clip](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ZClip.html) mode.  
**ZTest** | The shader’s [depth test](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ZTest.html) mode.  
**ZWrite** | The shader’s [depth clip](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ZWrite.html) mode.  
**Cull** | The shader’s [cull](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Cull.html) mode.  
**Conservative** | Indicates whether the shader used [conservative rasterization](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Conservative.html).  
**Offset** | The [depth bias](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Offset.html) on the GPU that Unity used during the selected event.  
**Stencil** | Indicates whether Stencil is enabled in the selected event. For more information, see [Stencil](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Stencil.html).  
**Stencil Ref** | The stencil reference value.  
**Stencil ReadMask** | The stencil [readmask](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Stencil.html) value Unity used to perform the stencil test.  
**Stencil WriteMask** | The stencil [writemask](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Stencil.html) value Unity used to write to the stencil buffer.  
**Stencil Comp** | The operation that the GPU performed for the stencil test for all **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel).  
**Stencil Pass** | The operation that the GPU performed on the stencil buffer for pixels that passed both the stencil test and the depth test.  
**Stencil Fail** | The operation that the GPU performed on the stencil buffer for pixels that failed the stencil test.  
**Stencil ZFail** | The operation that the GPU performed on the stencil buffer for pixels that passed the stencil test but failed the depth test.  
### Keywords
This section displays information about the enabled [shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html) Unity used in the rendering event.
**Property** | **Description**  
---|---  
**Name** | The name of the shader keyword.  
**Stage** | The shader stage that Unity used the shader keyword in. Refer to [Stages](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#stages).  
**Scope** | Indicates whether the scope of the keyword is global or local. For more information, refer to [Toggle shader keywords in a script](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-scripts.html).  
**Dynamic** | Indicates whether the keyword is dynamic or not. For more information, see [Declaring and using shader keywords in HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html).  
### Textures
The **Texture** section displays information about the named [textures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTexture.html) Unity used during the rendering event.
**Property** | **Description**  
---|---  
**Name** | The property name for the texture.  
**Stage** | The shader stage that Unity used the texture in. Refer to [Stages](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#stages).  
**Size** | The size of the texture. This is the width and height for 2D textures and width, height, and depth for 3D textures,  
**Sampler Type** | Indicates type of a Texture (such as 2D Texture, cubemap, or 3D volume texture).  
**Color Format** | The color format that the texture uses. For more information on RenderTexture formats, see [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html). For more information on formats for other texture types, see [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html).  
**Depth Stencil Format** | The depth stencil format for the RenderTexture. For more information, see [RenderTexture.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html).   
**Note** : If the texture isn’t a RenderTexture, Unity doesn’t display a [graphics format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) here.  
**Texture** | The texture name.  
### Ints
The **Ints** section displays information about the named [int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetInt.html) values Unity used during the rendering event.
**Property** | **Description**  
---|---  
**Name** | The name of the int property in the shader.  
**Stage** | The shader stage that Unity used the int property in. Refer to [Stages](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#stages).  
**Value** | The value of the int property.  
### Floats
The **Floats** section displays information about the named [float](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetFloat.html) values Unity used during the rendering event.
**Property** | **Description**  
---|---  
**Name** | The name of the float property in the shader.  
**Stage** | The shader stage that Unity used the float property in. Refer to [Stages](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#stages).  
**Value** | The value of the float property.  
### Vectors
**Property** | **Description**  
---|---  
**Name** | The name of the vector property in the shader.  
**Stage** | The shader stage that Unity used the vector property in. Refer to [Stages](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#stages).  
**Value(R)** | The R component of the vector.  
**Value(G)** | The G component of the vector.  
**Value(B)** | The B component of the vector.  
**Value(A)** | The A component of the vector.  
### Matrices
The **Matrices** section displays information about the named [matrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetMatrix.html) values Unity used during the rendering event.
**Property** | **Description**  
---|---  
**Name** | The name of the matrix property in the shader.  
**Stage** | The shader stage that Unity used the matrix property in. Refer to [Stages](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#stages).  
**Column 0** | The values in the first column of the matrix.  
**Column 1** | The values in the second column of the matrix.  
**Column 2** | The values in the third column of the matrix.  
**Column 3** | The values in the fourth column of the matrix.  
### Buffers
The **Buffers** section displays information about the named [ buffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetBuffer.html) Unity used during the rendering event.
**Property** | **Description**  
---|---  
**Name** | The name of the buffer in the shader.  
**Stage** | The shader stage that Unity used the buffer in. Refer to [Stages](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#stages).  
### Constant Buffers
This **Constant Buffers** section displays information about the named [constant buffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetConstantBuffer.html) Unity used during the rendering event.
**Property** | **Description**  
---|---  
**Name** | The name of the constant buffer in the shader.  
**Stage** | The shader stage that Unity used the constant buffer in. Refer to [Stages](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html#stages).  
### Stages
The possible values for **Stage** are:
  * **vs** : Vertex Shader
  * **fs** : Fragment Shader
  * **gs** : Geometry Shader
  * **hs** : Hull Shader
  * **ds** : Domain Shader


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window.html)
Frame Debugger window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingStatistics.html)
Rendering Statistics window reference
