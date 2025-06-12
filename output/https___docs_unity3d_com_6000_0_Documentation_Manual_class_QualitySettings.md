* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)
  * Quality settings tab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PresetManager.html)
Preset Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoManager.html)
Script Execution Order settings
# Quality settings tab reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html "Go to QualitySettings page in the Scripting Reference")
To configure the levels of graphical quality that Unity uses to render your project for different platforms, go to **Edit** > **Project Settings** > **Quality**.
A higher quality usually results in a lower frame rate. It’s best to use lower quality on mobile devices and older platforms, to avoid having a detrimental effect on gameplay.
![Edit the settings for a specific Quality level](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/quality-settings-panel.png)  

The **Quality** tab contains the following sections:
  * **A** : The matrix of quality levels and build platforms in this project.
  * **B** : The active build platform.
  * **C** : The active quality level.
  * **D** : The configuration of the active quality level.


## Quality levels matrix
**Property** | **Description**  
---|---  
**Levels** | Lists the quality levels in the project, and the platforms they apply to when Unity builds your project. To make a quality level active in the Editor and the configuration section, select it to highlight it. To apply a quality level to a build platform, enable the checkbox under the platform.  
  
To rename a level, under **Current Active Quality Level** , select **Name**.  
  
To delete a quality level, select the trashcan icon next to the quality level.  
**Default** | Sets the default quality level for each platform. The checkbox for the default platform displays green.  
**Add Quality Level** | Adds a quality level by duplicating the highlighted quality level.  
## Configuration section
The configuration section contains the following sections:
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#Rendering)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#Textures)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture)
  * [Particles](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#Particles)A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particle)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#Terrain)The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain)
  * [Shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#Shadows)A UI component that adds a simple outline effect to graphic components such as Text or Image. It must be on the same GameObject as the graphic component. [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Shadow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadow)
  * [Async Asset Upload](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#AsyncAssetUpload)
  * [Level of Detail](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#LevelOfDetail)The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#levelofdetail)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#Meshes)


### Rendering
**Property** | **Description**  
---|---  
****Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline)** | Sets the Render Pipeline Asset to use at this quality level.  
****Pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) Light Count** | Sets the maximum number of per-pixel lights if you use a forward **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath). For more information, refer to [Per-pixel and per-vertex lights](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights.html).  
**Anti Aliasing** | Smooths edges using multisample anti-aliasing (MSAA). The higher the **antialiasing** A technique for decreasing artifacts, like jagged lines (jaggies), in images to make them appear smoother.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Antialiasing) level, the smoother the appearance of the edges of polygons, but the more processing time needed on the GPU. MSAA is supported only in [forward rendering paths](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-paths-introduction.html#forward). For the dropdown options, refer to [Anti Aliasing dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#anti-aliasing-dropdown).  
**Realtime Reflection Probes** | Indicates whether to update [reflection probes](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) at runtime.  
**Resolution Scaling Fixed DPI Factor** | Increases or decreases the screen resolution of the device. For more information, refer to [Android Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Scaling) and [iOS Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsiOS.html#Scaling).  
****VSync** Vertical synchronization (VSync) is a display setting that caps a game’s frame rate to match the refresh rate of a monitor, to prevent image tearing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VSync) Count** | Synchronizes rendering with the refresh rate of the display device to avoid [tearing artifacts](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraTroubleshooting.html#tearing). For the dropdown options, refer to [VSync Count dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#vsync-count-dropdown).  
**Realtime GI CPU Usage** | Controls how much CPU capacity Unity can use to calculate [Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html). Higher settings make the system react faster to changes in lighting. For more information, refer to [Realtime GI CPU Usage dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#realtime-gi-cpu-usage-dropdown)  
  
This property is available in the **Quality** window only if your project uses the Universal Render Pipeline (URP) or the High Definition Render Pipeline (HDRP). For the Built-In Render Pipeline, refer to [graphics settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html).  
#### Anti Aliasing dropdown
**Value** | **Description**  
---|---  
**Disabled** | Disables MSAA.  
**2x Multi Sampling** | Samples twice per pixel.  
**4x Multi Sampling** | Samples four times per pixel.  
**8x Multi Sampling** | Samples eight times per pixel.  
#### VSync Count dropdown
**Value** | **Description**  
---|---  
**Don’t Sync** | Disables synchronizing rendering with the display device.  
**Every V Blank** | Synchronizes rendering so that Unity switches frames every time the display isn’t updating.  
**Every Second V Blank** | Synchronizes rendering so that Unity switches frames every second time the display isn’t updating.  
#### Realtime GI CPU Usage dropdown
**Value** | **Description**  
---|---  
**Low** | Limits **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) to a low amount of CPU capacity.  
**Medium** | Limits Enlighten Realtime Global Illumination to a medium amount of CPU capacity.  
**High** | Limits Enlighten Realtime Global Illumination to a high amount of CPU capacity.  
**Unlimited** | Uses no CPU capacity limit for Enlighten Realtime Global Illumination. **Note:** Some platforms have their own limit on how many CPU threads or cores Unity can use. For example, Android might limit Unity to one less than the total number of CPUs, or to only little CPUs on devices with big/little CPUs. For more information, refer to [Android thread configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/android-thread-configuration.html)  
### Textures
**Property** | **Description**  
---|---  
**Global Mipmap Limit** | Limits the mipmap resolution level that Unity uses when it renders textures. To use lower resolutions that require less GPU memory and processing time, set this property to a higher mipmap level. For the dropdown options, refer to [Global Mipmap Limit dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#global-mipmap-limit-dropdown).  
  
This property only affects textures with a [texture shape](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html#textureshape) of 2D or 2D Array.  
**Mipmap Limit Groups** | Lists the custom groups that you can add textures to so they override the **Global Mipmap Limit**. Use Mipmap Limit Groups to allocate more memory for important textures, and less memory for less important textures. For more information, refer to [Mipmap Limit Groups properties](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#mipmap-limit-groups-properties)  
  
This property affects only textures with a [texture shape](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html#textureshape) of 2D or 2D Array.  
**Anisotropic Textures** | Controls which textures use anisotropic filtering, which improves the visual quality when you view a texture at a steep angle. Anisotropic filtering increases rendering time. For dropdown options, refer to [Anisotropic Textures dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#anisotropic-textures-dropdown).  
**Mipmap Streaming** | Limits the size of textures in GPU memory by using [mipmap streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html). Disable this setting to reduce processing time. For dropdown options, refer to [Mipmap Streaming dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#mipmap-streaming-dropdown).  
#### Global Mipmap Limit dropdown
For more information about mipmaps and mipmap limits, refer to [Mipmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-mipmaps-introduction.html).
**Value** | **Description**  
---|---  
**0: Full Resolution** | Uses no limit for texture resolution. Unity can use mipmap level 0, which is the full resolution of the texture.  
**1: Half Resolution** | Limits the highest resolution to mipmap level 1, which is half resolution.  
**2: Quarter Resolution** | Limits the highest resolution to mipmap level 2, which is quarter resolution.  
**3: Eighth Resolution** | Limits the highest resolution to mipmap level 3, which is eighth resolution.  
#### Mipmap Limit Groups properties
To create a new group, select the **Add** (**+**) button. To delete a group, select the **Remove** (**−**) button. If you delete a group, a dialog appears that checks if you want to remove the textures from the group and reimport them. You can’t undo this.
The dropdown for each group contains the following options.
**Group property** | **Description**  
---|---  
**Offset Global Mipmap Limit: –3** | Allows the textures in this group to use eight times the resolution of **Global Mipmap Limit**. This results in Unity using higher resolution textures and more memory. For example, if **Global Mipmap Limit** is **3: Eighth Resolution** , Unity limits this group of textures to **0: Full Resolution**.  
**Offset Global Mipmap Limit: –2** | Allows the textures in this group to use four times the resolution of **Global Mipmap Limit**.  
**Offset Global Mipmap Limit: –1** | Allows the textures in this group to use two times the resolution of **Global Mipmap Limit**.  
**Use Global Mipmap Limit** | Uses **Global Mipmap Limit** for the textures in this group.  
**Offset Global Mipmap Limit: +1** | Limits the textures in this group to half the resolution of **Global Mipmap Limit**. This results in Unity using lower resolution textures and less memory. For example, if **Global Mipmap Limit** is **1: Half Resolution** , Unity limits this group of textures to **2: Quarter Resolution**.  
**Offset Global Mipmap Limit: +2** | Limits the textures in this group to a quarter of the resolution of **Global Mipmap Limit**.  
**Offset Global Mipmap Limit: +3** | Limits the textures in this group to an eighth of the resolution of **Global Mipmap Limit**.  
**Override Global Mipmap Limit: Full Resolution** | Limits the textures in this group to mipmap level 0, which is full resolution.  
**Override Global Mipmap Limit: Half Resolution** | Limits the textures in this group to mipmap level 1, which is half resolution.  
**Override Global Mipmap Limit: Quarter Resolution** | Limits the textures in this group to mipmap level 2, which is quarter resolution.  
**Override Global Mipmap Limit: Eighth Resolution** | Limits the textures in this group to mipmap level 3, which is eighth resolution.  
Open the **More** (**⋮**) menu for additional properties.
**Additional property** | **Description**  
---|---  
**Identify textures** | Selects all the textures that belong to the group in the **Project** window. For more information about adding textures to a Mipmap Limit Group, refer to [Texture Import Settings window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).  
**Duplicate Group** | Duplicate the group.  
**Rename Group** | Rename the group. If you rename a group, a dialog appears that checks if you want to reassign the textures from the old group to the new group, and reimport them. You can’t undo this.  
#### Anisotropic Textures dropdown
For more detail about anisotropic texture filtering levels, refer to the [`Texture-anisoLevel`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-anisoLevel.html) API.
**Value** | **Description**  
---|---  
**Disabled** | Disables anisotropic filtering.  
**Per Texture** | Uses the ****Aniso Level** The anisotropic filtering (AF) level of a texture. Allows you to increase texture quality when viewing a texture at a steep angle. Good for floor and ground textures. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AnisoLevel)** each texture is set to in its [texture import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).  
**Forced On** | Uses anisotropic filtering for all textures.  
### Mipmap Streaming dropdown
**Property** | **Description**  
---|---  
**Add All Cameras** | Indicates whether to use mipmap streaming for all active cameras in the project. If you disable this setting, Unity calculates mipmap streaming only for cameras that have a **Streaming Controller** component.  
  
For more information, refer to [Configure mipmap streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-configure.html).  
**Memory Budget** | Limits the total amount of memory for loaded textures, in MB. The default is 512 MB. For more information, refer to [Set the memory budget for textures](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-configure.html#memory-budget).  
**Renderers Per Frame** | Limits how many renderers mipmap streaming processes per frame. A lower number decreases the processing time on the CPU, but increases texture loading times. The default is 512.  
**Max Level Reduction** | Sets the number of mipmap levels that the mipmap streaming system can discard if it reaches the **Memory Budget**. The default is 2.  
  
This value is also the mipmap level that the mipmap streaming system initially loads at startup. For example, when **Max Level Reduction** is set to 2, Unity skips mipmap level 0 and 1 on first load.  
  
For more information, refer to [Set the memory budget for textures](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-configure.html#memory-budget).  
**Max IO Requests** | Limits the maximum number of file requests the mipmap streaming system makes at any one time. Lower values avoid the system trying to load too many textures if the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) changes quickly, but reduce how quickly the system reacts to texture changes. The default is 1024, which is high enough to prevent any limit outside the [Async Upload pipeline](https://unity.com/blog/engine-platform/understanding-the-async-upload-pipeline) and the file system itself.  
### Particles
**Property** | **Description**  
---|---  
**Soft Particles** | Indicates whether to fade particles as they approach the edges of opaque **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). For more information, refer to [Soft particles](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-color.html#soft-particles)Particles that create semi-transparent effects like smoke, fog or fire. Soft particles fade out as they approach an opaque object, to prevent intersections with the geometry. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SoftParticles). This property is only available if your project uses the Built-In Render Pipeline. For the Universal Render Pipeline, refer to [Universal Render Pipeline asset reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html).  
**Particle Raycast Budget** | Sets the maximum number of raycasts to use for **particle system** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) collisions if ****Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) Quality** is set to **Medium** or **Low**. For more information, refer to [Particle collisions](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-collisions.html).  
### Terrain
**Property** | **Description**  
---|---  
****Billboards** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) Face **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) Position** | Enable this option to force billboards to face the camera while rendering instead of the camera plane. This produces a better, more realistic image, but is more expensive to render.  
**Use Legacy Details Distribution** | Enable this option to use the previously supported scattering algorithm that often resulted in overlapping details. Included for backward compatibility with Terrains authored in Unity 2022.1 and earlier.  
**Terrain Setting Overrides** | Various override settings that, when enabled, override the value of all active terrains (except those with the “Ignore Quality Settings” setting enabled). For more information about these settings, see [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Pixel Error | Value set to Terrain Pixel Error. See [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Base Map Dist. | Value set to Terrain Basemap Distance. See [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Detail Density Scale | Value set to Terrain Density Scale. See [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Detail Distance | Value set to Terrain Detail Distance. See [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Tree Distance | Value set to Terrain Tree Distance. See [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Billboard Start | Value set to Terrain Billboard Start. See [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Fade Length | Value set to Terrain Fade Length. See [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
Max **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Trees | Value set to Terrain Max Mesh Trees. See [Terrain Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html).  
### Shadows
**Property** | **Description**  
---|---  
****Shadowmask** A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadowmask) Mode** | Controls when Unity uses baked shadows and real-time shadows if you set **Lighting Mode** to **Shadowmask**. For the dropdown options, refer to [Shadowmask mode dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#shadowmask-mode-dropdown).  
The following properties are only available if your project uses the Built-In Render Pipeline. For the Universal Render Pipeline, refer to [Universal Render Pipeline asset reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html).
**Property** | **Description**  
---|---  
**Shadows** | Identifies whether to render soft or hard shadows, or no shadows.  
**Shadow Resolution** | Controls the visual fidelity of shadows. The higher the resolution, the greater the processing overhead, and the memory used on the GPU.  
**Shadow Projection** | Controls the quality and stability of shadows from the directional light. For the dropdown settings, refer to [Shadows Projection dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#shadows-projection-dropdown).  
**Shadow Distance** | Sets the distance away from the camera where Unity no longer renders shadows, in meters.  
**Shadow Near Plane Offset** | Sets how far to pull back the near clip plane of a shadow map. Use this setting to fix distorted shadows cast by large triangles. For more information, refer to [Shadow pancaking](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html#shadow-pancaking).  
**Shadow Cascades** | Choose the number of shadow cascades to use. A higher number of shadow cascades results in higher-quality shadows but a longer processing time. For more information, refer to [Shadow cascades](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-landing.html).  
**Cascade splits** | Controls the distance where each shadow cascade starts and ends. To adjust the distances, select and drag the vertical lines between each pair of cascades. This property is only available if you set **Shadow Cascades** to **Two Cascades** or **Four Cascades**. For more information, refer to [Shadow cascades](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-landing.html).  
#### Shadowmask mode dropdown
For more information, refer to [Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html).
**Value** | **Description**  
---|---  
**Shadowmask** | Casts baked shadows from static GameObjects at all distances.  
****Distance Shadowmask** A version of the Shadowmask lighting mode that includes high quality shadows cast from static GameObjects onto dynamic GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DistanceShadowmask)** | Casts baked shadows only from static GameObjects beyond the distance set in **Shadow Distance**. Other GameObjects cast real-time shadows.  
#### Shadows Projection dropdown
**Value** | **Description**  
---|---  
**Close Fit** | Renders higher resolution shadows that might sometimes wobble slightly if the camera moves.  
**Stable Fit** | Renders lower resolution shadows that don’t wobble.  
### Async Asset Upload
For more information about the asynchronous upload pipeline, refer to [Texture and mesh loading](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingTextureandMeshData.html).
**Property** | **Description**  
---|---  
**Time Slice** | Sets the amount of CPU time in ms per frame Unity spends uploading buffered texture and mesh data to the GPU.  
**Buffer Size** | Sets the size in MB of the asynchronous upload buffer Unity uses to stream texture and mesh data to the GPU.  
**Persistent Buffer** | Indicates whether the upload buffer persists when there’s nothing left to upload.  
### Level of Detail
For more information, refer to [Simplifying distant meshes with level of detail (LOD)](https://docs.unity3d.com/6000.0/Documentation/Manual/simplifying-distant-meshes-with-level-of-detail-lod.html).
**Property** | **Description**  
---|---  
**LOD Bias** | Adjusts the detail level of GameObjects by scaling the distances where Unity transitions between different level of detail (LOD) meshes. A **LOD Bias** value between 0 and 1 results in Unity selecting lower-quality LODs at closer distances than normal. A value of 1 or more results in Unity selecting lower-quality LODs at farther distances than normal, so GameObjects retain higher quality for longer. For example, if you set **LOD Bias** to 2, a transition to a lower-quality LOD level that usually happens at 50% distance now happens at 25% distance (50% / 2 = 25%).  
**Maximum LOD Level** | Sets the lowest LOD level the project uses. Unity removes LOD meshes below the **Maximum LOD level** from the build, which makes the build smaller, and reduces memory use at runtime. If you have different quality levels that use different **Maximum LOD Level** values, Unity uses the smallest value. For example, if any quality level uses a **Maximum LOD Level** of 0, Unity includes all LOD levels in the build.  
**LOD Cross Fade** | Smooths the transition between LOD meshes by fading between two LOD levels using a dithering pattern. This property is only available if your project uses the Built-In Render Pipeline. For the Universal Render Pipeline, refer to [Universal Render Pipeline asset reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html).  
### Meshes
**Property** | **Description**  
---|---  
**Skin Weights** | Sets the number of bones that can affect a vertex during an animation. For more information, refer to [Skinned Mesh Renderer component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html).  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PresetManager.html)
Preset Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoManager.html)
Script Execution Order settings
