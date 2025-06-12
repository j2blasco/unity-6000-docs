* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-create.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Cubemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)
  * Create a cubemap


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-introduction.html)
Introduction to cubemaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray-create.html)
Create a cubemap array
# Create a cubemap
## Creating Cubemaps from Textures
The fastest way to create **cubemaps** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) is to import them from specially laid out [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture). Select the Texture in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ProjectView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Projectwindow), to see the Import Settings in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. In the Import Settings, set the **Texture Type** to **Default** , **Normal Map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) or **Single Channel** , and the **Texture Shape** to **Cube**. Unity then automatically sets the Texture up as a Cubemap.
Several commonly-used cubemap layouts are supported (and in most cases, Unity detects them automatically).
Vertical and horizontal cross layouts, as well as column and row of cubemap faces are supported:
![A vertical cross layout where four faces form a column, a horizontal cross layout where four faces form a row, a column layout, and a row layout.](https://docs.unity3d.com/6000.0/Documentation/uploads/Textures/CubeLayout6Faces1.png) A vertical cross layout where four faces form a column, a horizontal cross layout where four faces form a row, a column layout, and a row layout.
Another common layout is `LatLong` (Latitude-Longitude, sometimes called cylindrical). Panorama images are often in this layout:
![A latitude-longitude layout. Four faces form a row, and the two remaining faces stretch along the top and bottom of the texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Textures/CubeLayoutLatLong.png) A latitude-longitude layout. Four faces form a row, and the two remaining faces stretch along the top and bottom of the texture.
`SphereMap` (spherical environment map) images can also be found:
![A spherical environment map. The texture is circular, with one face in the centre and four faces surrounding it in a ring. The sixth face is the outer shell of the texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Textures/CubeLayoutSphereMap.png) A spherical environment map. The texture is circular, with one face in the centre and four faces surrounding it in a ring. The sixth face is the outer shell of the texture.
By default Unity looks at the **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio) of the imported texture to determine the most appopriate layout from the above. When imported, a cubemap is produced which can be used for skyboxes and reflections:
Selecting `Glossy Reflection` option is useful for cubemap textures that will be used by [Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe). It processes cubemap mipmap levels in a special way (specular convolution) that can be used to simulate reflections from surfaces of different smoothness:
![A cubemap used in a Reflection Probe to create reflections on surfaces of varying smoothnesses.](https://docs.unity3d.com/6000.0/Documentation/uploads/Textures/CubeOptionGlossyReflections.png) A cubemap used in a Reflection Probe to create reflections on surfaces of varying smoothnesses.
## Other Techniques
Another useful technique is to generate the cubemap from the contents of a Unity **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) using a script. The [Camera.RenderToCubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderToCubemap.html) function can record the six face images from any desired position in the scene; the code example on the function’s script reference page adds a menu command to make this task easy.
## Legacy Cubemap Assets
Unity also supports creating cubemaps out of six separate [textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html). Select **Assets > Create > Legacy > Cubemap** from the menu, and drag six textures into empty slots in the inspector.
**_Property:_** | **_Function:_**  
---|---  
**Right..Back Slots** | Textures for the corresponding cubemap face.  
**Face Size** | Width and Height of each Cubemap face in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel). The textures will be scaled automatically to fit this size.  
**Mipmap** | Should mipmaps be created?  
**Linear** | Should the cubemap use linear color?  
**Readable** | Should the cubemap allow **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) to access the pixel data?  
Note that it is preferred to create cubemaps using the Cubemap texture import type (see above) - this way cubemap texture data can be compressed; edge fixups and glossy reflection convolution be performed; and **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) cubemaps are supported.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-introduction.html)
Introduction to cubemaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray-create.html)
Create a cubemap array
