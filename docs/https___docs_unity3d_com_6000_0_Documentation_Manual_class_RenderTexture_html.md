* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Textures reference](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)
  * Render Texture Inspector window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MovieTexture.html)
Movie Texture Inspector window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture.html)
Custom Render Texture Inspector window reference
# Render Texture Inspector window reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html "Go to RenderTexture page in the Scripting Reference")
The **Render Texture** **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) is similar to the [Texture Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
The Render Texture inspector displays the current contents of Render Texture in real-time and can be an invaluable debugging tool for effects that use render textures.
**Property** | **Description**  
---|---  
**Dimension** | Set the number of dimensions of the Render Texture. For more information, refer to [Dimension dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html#dimension-dropdown).  
**Size** | Set the size of the Render Texture in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel).  
**Anti-Aliasing** | Set the number of **antialiasing** A technique for decreasing artifacts, like jagged lines (jaggies), in images to make them appear smoother.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Antialiasing) samples Unity applies. The options are **None** , **2 samples** , **4 samples** , or **8 samples**. If you select **None** , Unity doesn’t apply antialiasing.  
**Enable Compatible Format** | If you enable this property, Unity converts the **Color Format** and **Depth Stencil Format** to compatible formats, if the platform doesn’t support the formats you select.  
**Color Format** | Set the [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) of the color buffer of the Render Texture. If you select **None** , Unity doesn’t allocate a color buffer for this Render Texture.  
**Depth Stencil Format** | Set the [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) of the depth/**stencil buffer** of the Render Texture. If you select **None** , Unity doesn’t allocate a depth/stencil buffer for this Render Texture. The stencil buffer is a general purpose buffer that allows you to store an additional unsigned 8-bit integer (0 to 255) for each pixel Unity draws to the screen.  
**Mipmap** | Allocate a [mipmap](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-mipmaps-introduction.html) for the Render Texture.  
**Auto-generate** | Automatically generate a mipmap. If you disable this property, use the [`RenderTexture.GenerateMips`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.GenerateMips.html) API to generate a mipmap manually. Alternatively, choose which mipmap level to render into when you use [`Graphics.SetRenderTarget`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.SetRenderTarget.html) and [`Rendering.CommandBuffer.SetRenderTarget`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetRenderTarget.html). This property is visible only if you enable **Enable Mip Maps**.  
**Dynamic Scaling** | Use [dynamic resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution) to resize the Render Texture. If you disable this property, the Render Texture stays the same size regardless of the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s **Dynamic Resolution** setting.  
**Random Write** | Allow **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to write into arbitrary locations of the color buffer of the Render Texture. Refer to [`RenderTexture.enableRandomWrite`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-enableRandomWrite.html) for more information.  
**Wrap Mode** | Control how Unity wraps the texture. For more information, refer to [Wrap Mode dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html#wrap-mode-dropdown).  
**Filter Mode** | Control how the sampling of the texture uses nearby pixels. For more information, refer to [Filter Mode dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html#filter-mode-dropdown).  
****Aniso Level** The anisotropic filtering (AF) level of a texture. Allows you to increase texture quality when viewing a texture at a steep angle. Good for floor and ground textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnisoLevel)** | Set the anisotropic filtering level of the texture. This increases texture quality when you view the texture at a steep angle. Use anisotropic filtering for floor, ground, and road textures. This property is visible only if you set **Depth Stencil Format** to **None**.  
**Shadow Sampling Mode** | Select the sampling technique the GPU uses if the render texture is used as a [shadow map](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-mapping.html). This property is only visible if **Depth Stencil Format** is not set to **None** , and only has an effect if you set **Color Format** to **None**.  
## Dimension dropdown
**Value** | **Description**  
---|---  
**2D** | Set the Render Texture as a 2D texture.  
**2D Array** | Set the Render Texture as a 2D texture array.  
**Cube** | Set the Render Texture as a **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap).  
**3D** | Set the Render Texture as 3D texture.  
## Wrap Mode dropdown
**Value** | **Description**  
---|---  
**Repeat** | Tile the texture to create a repeating pattern.  
**Clamp** | Stretch the edges of the texture. This is useful for preventing wrapping artifacts when you map an image onto a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), and you don’t want the texture to tile.  
**Mirror** | Tile the texture to create a repeating pattern that mirrors the texture at every integer boundary.  
**Mirror Once** | Mirror the texture once, then fall back to clamping.  
**Per-axis** | Set different **Wrap Mode** values for the u-axis and v-axis. For example, when you use latitude-longitude environment maps for **reflection probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe), you can use **Repeat** for the u-axis and **Clamp** for the v-axis.  
## Filter Mode dropdown
**Value** | **Description**  
---|---  
**Point** | Use the nearest pixel. This makes the texture appear pixelated.  
**Bilinear** | Use a weighted average of the four nearest texels. This makes the texture appear blurry when you magnify it.  
**Trilinear** | Use a weighted average of the two nearest mipmap levels, which Unity filters using bilinear filtering. This creates a soft transition between mipmap levels, but the texture is slightly more blurry.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MovieTexture.html)
Movie Texture Inspector window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture.html)
Custom Render Texture Inspector window reference
