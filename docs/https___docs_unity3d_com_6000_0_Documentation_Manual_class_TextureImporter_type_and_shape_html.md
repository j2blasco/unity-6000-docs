* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter-type-and-shape.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Textures reference](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-reference.html)
  * [Texture Import Settings window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)
  * Texture type and shape settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)
Texture Import Settings window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter-type-specific.html)
Platform-specific texture overrides panel reference
# Texture type and shape settings reference
![The Texture Import Settings window with all the settings up to the Advanced section highlighted.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/texture-import-settings-top.png) The Texture Import Settings window with all the settings up to the **Advanced** section highlighted.
**Note:** Some of the less commonly used properties are hidden by default. Expand the [Advanced](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter-type-and-shape.html#advanced) section in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window to view these properties.
## Texture Type
Use the **Texture Type** property to select the type of Texture you want to create from the source image file. The other properties in the Texture Import settings window change depending on the value you set.
**Property** | **Function**  
---|---  
**Default** | This is the most common setting used for all Textures. It provides access to most of the properties for Texture importing. For more information, see the [Default](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-default.html) Texture type.  
**Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) | The **Normal map** texture type formats the texture asset so it’s suitable for real-time normal mapping. For more information, see the [Normal map](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-normal-map.html) texture type documentation.   
  
For more information on normal mapping in general, see [Importing Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-normal-map.html).  
**Editor GUI and Legacy GUI** | The **Editor GUI and Legacy GUI** texture type formats the texture asset so it’s suitable for HUD and GUI controls. For more information, see the [Editor GUI and Legacy GUI](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-editor-gui-and-legacy-gui.html) texture type documentation.  
**Sprite (2D and UI)** | The **Sprite (2D and UI)** texture type formats the texture asset so it’s suitable to use in 2D applications as a [Sprite](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite). For more information, see the [Sprite (2D and UI)](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html) texture type documentation.  
**Cursor** | The **Cursor** texture type formats the texture asset so it’s suitable to use as a custom mouse cursor. For more information, see the [Cursor](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cursor.html) texture type documentation.  
**Cookie** | The **Cookie** texture type formats the texture asset so it’s suitable to use as a [light cookie](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html) in the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline). For more information, see the [Cookie](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cookie.html) texture type documentation.  
**Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) | The **Lightmap** texture type formats the texture asset so it’s suitable to use as a [Lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html). This option enables encoding into a specific format (RGBM or dLDR depending on the platform) and a **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) step on texture data (a push-pull dilation pass). For more information, see the [Lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-lightmap.html) texture type documentation.  
**Directional Lightmap** | The **Directional Lightmap** texture type formats the texture asset so it’s suitable to use as a directional [Lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html). For more information, see the [Directional Lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-directional-lightmap.html) texture type documentation.  
**Shadowmask** | The **Shadowmask** texture type formats the texture asset so it’s suitable to use as a [shadowmask](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadowmask). For more information, see the [Shadowmask](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-shadowmask.html) texture type documentation.  
**Single Channel** | The **Single Channel** texture type formats the texture asset so it only has one channel. For information on the properties available only for the this type, see the [Single Channel](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-singlechannel.html) texture type documentation.  
## Texture Shape
Use the **Texture Shape** property to select and define the shape and structure of the Texture. There are four shape types:
  * **2D** is the most common setting for all Textures; it defines the image file as a 2D Texture. These are used to map Textures to 3D Meshes and GUI elements, among other Project elements.
  * **Cube** defines the Texture as a [cubemap](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap). You could use this for Skyboxes or **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe), for example. This type is only available with the [Default](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-default.html), [Normal Map](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-normal-map.html), and [Single Channel](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-singlechannel.html) Texture types.
  * **2D Array** defines the Texture as a [2D array texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html). This is commonly used as an optimization for some rendering techniques, where many textures of the same size & format are used.
  * **3D** defines the Texture as a [3D texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D.html). 3D textures are used by some rendering techniques to represent volumetric data.


### 2D Array and 3D columns and rows
When you set the **Texture Shape** property to **2D Array** or **3D** , Unity displays the **Columns** and **Rows** properties. Use these to tell Unity how to divide the flipbook texture into cells.
**Property:** | **Function:**  
---|---  
**Columns** | The number of columns that the source flipbook texture is divided into.  
**Rows** | The number of rows that the source flipbook texture is divided into.  
## Other settings
Depending on which **Texture Type** you select, different properties can appear in the Texture Import Settings window. Some of these properties are specific to the Texture Type itself, such as **Sprite Mode** available with the [Sprite (2D and UI)](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html) type.
Use Advanced settings to make finer adjustments to the way Unity handles the Texture. The order and availability of these settings can vary depending on the **Texture Type** you choose.
For information on the properties for each texture type, refer to the documentation for that texture type:
  * [Default](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-default.html)
  * [Normal map](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-normal-map.html)
  * [Editor GUI and Legacy GUI](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-editor-gui-and-legacy-gui.html)
  * [Sprite (2D and UI)](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html)
  * [Cursor](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cursor.html)
  * [Cookie](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-cookie.html)
  * [Lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-lightmap.html)
  * [Directional Lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-directional-lightmap.html)
  * [Shadowmask](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-shadowmask.html)
  * [Single Channel](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-singlechannel.html)


## Additional resources
  * [Platform-specific texture overrides panel reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter-type-specific.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)
Texture Import Settings window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter-type-specific.html)
Platform-specific texture overrides panel reference
