* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ViewModes.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * Scene view Draw Modes and View Options overlays


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html)
Scene visibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-and-handles.html)
Gizmos and handles
# Scene view Draw Modes and View Options overlays
Use the **Draw Modes** and **View Options** overlays to change how the ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)** view displays your scene.
These controls only affect the **Scene** view during development and have no effect on the built game.
## The Draw Modes overlay
Change the way meshes render in the **Scene** view.
![The Draw Modes overlay with the Unlit Draw Mode selected](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/DrawModesOverlay.png) The Draw Modes overlay with the Unlit Draw Mode selected **Draw Mode** |  | **Description**  
---|---|---  
**Shading Mode** |  |   
| Wireframe | Draw meshes with a wireframe representation.  
| Shaded Wireframe | Show meshes textured and with wireframes overlaid.  
| Unlit | Don’t use scene lighting.  
| Shaded | Show surfaces with their textures visible.  
| **Debug** | Refer to the Debug Mode options.  
### The Debug Mode options
The Debug Draw Mode has several options that help you unerstand your graphics and lighting better.
**Debug Mode option** |  | **Description**  
---|---|---  
**Lighting** |  |   
| **Contributors / Receivers** | Show the **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) contributors and receivers for the selected **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).  
| **Shadow Cascades** | Show directional light [shadow cascades](shadow-cascades.  
**Realtime**Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination)** |  | Visualize aspects of the [Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten.html) system. Refer to [GI Visualisations](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html) for information about each of these modes.  
**Baked Global Illumination** |  | Visualize aspects of the Baked Global Illumination system. For more information about each of these modes, refer to [GI Visualisations](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html).  
**Deferred** |  | View each of the elements of the G-buffer in isolation. For more information, refer to [Deferred Shading](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading).  
**Miscellaneous** |  |   
| **Render Paths** | Show the [rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) for each GameObject using a color code:   
  
Blue indicates [deferred shading](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
Yellow indicates [forward rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering)  
Red indicates [vertex lit](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-VertexLit.html)  
| **Alpha Channel** | Render colors with alpha.  
| **Overdraw** | Render GameObjects as transparent “silhouettes”. The transparent colors accumulate, making it easy to spot places where one object is drawn over another.  
| **Mipmaps** | Show ideal texture sizes using a color code:   
  
Red indicates that the texture is larger than necessary (at the current distance and resolution)  
Blue indicates that the texture might be larger. The ideal texture sizes depend on the resolution at which your application will run and how close the Camera can get to particular surfaces.  
| **Texture Mipmap Streaming** | Tint GameObjects green, red, or blue, depending on their status in the [Texture Mipmap Streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html) system. For more information, see documentation on [Analyze mipmap streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-analyze.html).  
| ****Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) Mask** | Sprite Masks are used to either hide or reveal parts of a Sprite or group of Sprites. For more information, refer to [Sprite Masks](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/mask/mask-landing.html)A texture which defines which areas of an underlying image to reveal or hide. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/mask/mask-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteMask).  
**Validate Albedo** and **Vadlidate Metal Sepcular** |  | Check whether your physically-based materials use values within the recommended ranges. For more information, refer to [Physically Based Material Validator](https://docs.unity3d.com/6000.0/Documentation/Manual/MaterialValidator.html).  
## The View Options overlay
Change what the **Scene** view displays.
![The View Options overlay with all effects, hidden objects, and gizmos selected](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ViewOptionsOverlay.png) The View Options overlay with all effects, hidden objects, and gizmos selected **View option** |  | **Description**  
---|---|---  
**2D** |  | View the scene in 2D or 3D. In 2D mode, the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) looks towards positive z, with the x-axis pointing right and the y-axis pointing up.  
**Audio** |  | Enable or disable audio.  
**Effects** |  | Enable or disable rendering effects. Use the dropdown to select individual effects, or the **Effects** * button for all effects.  
| ****Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox)** | Show a skybox texture as the scene’s background.  
| **Clouds** | Shows cloud layers and volumetric clouds. Only available when using an SRP that supports clouds.  
| **Fog** | Gradualy fade the view to a flat color with distance from the camera.  
| **Flares** |  **Lens flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) on lights.  
| **Always Refresh** | Display the animation of animated materials, such as grass waving on a **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain).  
| **Post Processing** | Show [Post-processing](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects.  
| **Particle Systems** | Show [Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) effects.  
**Scene Visibility** |  | Show or hide all hidden GameObjects (GameObjects marked as not visible in the **Hierarchy** windw). For more information, refer to [Scene Visibility](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html). "  
**Layers** |  | Select which layers to display. For more information, refer to [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer).  
**Camera Settings** |  | Configure the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) Camera. For more information, refer to [Scene view Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewCamera.html).  
****Gizmos** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo)** |  | Enable or disable gizmos. Use the dropdown to select individual gizmos, or the **Gizmos** * button for all gizmos. For more information, refer to [Gizmos Menu](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html).  
## Additional resources
  * [Overlays](https://docs.unity3d.com/6000.0/Documentation/Manual/overlays.html)
  * [Display or hide an overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/display-and-hide-overlay.html)
  * [Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneVisibility.html)
Scene visibility
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-and-handles.html)
Gizmos and handles
