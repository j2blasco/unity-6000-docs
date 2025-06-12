* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-skybox-panoramic.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Sky](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)
  * [Skybox Shader Material Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/skybox-material-reference.html)
  * Panoramic Skybox Shader Material Inspector Window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-skybox-cubemap.html)
Cubemap Skybox Shader Material Inspector Window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-skybox-procedural.html)
Procedural Skybox Shader Material Inspector Window reference
# Panoramic Skybox Shader Material Inspector Window reference
For information on how to create a Material that uses this **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), as well as details on how to render the skybox in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), see [Using skyboxes](https://docs.unity3d.com/6000.0/Documentation/Manual/skyboxes-using.html).
## Render pipeline compatibility
**Feature** | **Built-in**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline)** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)**  
---|---|---|---  
**Panoramic skybox** | Yes | Yes | No  
## Properties
**Property** | **Description**  
---|---  
**Tint Color** | The color to tint the skybox to. Unity adds this color to the Textures to change their appearance without altering the base Texture files.  
**Exposure** | Adjusts the skybox’s exposure. This allows you to correct tonal values in the skybox Textures. Larger values produce a more exposed, seemingly brighter, skybox. Smaller values produce a less exposed, seemingly darker, skybox.  
**Rotation** | The rotation of the skybox around the positive y-axis. This changes the orientation of your skybox and is useful if you want a specific section of the skybox to be behind a particular part of your Scene.  
**Spherical (HDR)** | The Texture this Material spherically wraps around the Scene to represent the sky.For information on how to create a **Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) Asset from your input Textures, see [Cubemap Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html).  
**Mapping** | Specifies the method this Material uses to project the Texture to create the skybox. The options are:**6 sided** : Uses a net format to map the Texture to the skybox.**Latitude Longitude Layout** : Uses a cylindrical wrapping method to map the Texture to the skybox.  
**Image Type** | Specifies the angle around the y-axis that this Material projects the skybox to. The options are:**180** : Draws the **Spherical** Texture as a hemisphere with the peak in the direction of the positive z-axis. To change which side of the Scene this Material draws the Texture to, modify the **Rotation** property. By default, the back of the skybox is black, but this Material can draw a duplicate of the **Spherical** Texture on the back instead. To do this, enable **Mirror on Back**.**360** : Draws the Texture as a full sphere representation that wraps around the entire Scene.  
**- Mirror on Back** | Specifies whether the Material should duplicate the **Spherical** Texture on the back of the skybox instead of drawing it as black.This option only appears when **Image Type** is set to **180**.  
**Render Queue** | Determines the order in which Unity draws **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). For more information on **Render Queue** , see [SL-SubShaderTags](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html).  
**Double Sided**Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination)** | Specifies whether the **lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) accounts for both sides of the geometry when it calculates Global Illumination. When `true`, if you use the Progressive Lightmapper, back faces bounce light using the same emission and albedo as front faces.  
## Additional resources
  * [Configure a skybox with a Skybox Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/skybox-shaders.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-skybox-cubemap.html)
Cubemap Skybox Shader Material Inspector Window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-skybox-procedural.html)
Procedural Skybox Shader Material Inspector Window reference
