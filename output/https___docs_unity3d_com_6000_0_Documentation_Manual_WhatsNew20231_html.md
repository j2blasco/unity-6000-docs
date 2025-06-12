* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20231.html

  * [What's new in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew.html)
  * New in Unity 2023.1


[](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20232.html)
New in Unity 2023.2
[](https://docs.unity3d.com/6000.0/Documentation/Manual/install-and-upgrade.html)
Install and upgrade
# New in Unity 2023.1
## Release Notes
To find out more about the new features, changes, and improvements to this Unity version, refer to the [2023.1 Release Notes](https://unity3d.com/unity/whats-new/2023.1.0).
To find the release notes for other releases, refer to the [Unity download archive](https://unity.com/releases/editor/archive).
## Upgrade Guide
If you are upgrading existing projects from 2022 LTS, read the [Upgrade Guide to 2023.1](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20231.html) for information about how your project might be affected.
# What’s new
Find out what’s changed in Unity 2023.1 since 2022 LTS and view the documentation for the affected areas.
## Adaptive Performance
  * Added [Lifecycle controls and a general Android provider](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance@5.0/manual/samples-guide.html#lifecycle-management).
  * Added an [Adaptive Performance Android Provider](https://docs.unity3d.com/Packages/com.unity.adaptiveperformance.google.android@1.0/manual/index.html) that extends the Adaptive Performance package to Android Devices.
  * Added new `IPerformanceModeStatus` to retrieve performance mode and listen to performance mode changes.


## Artist and Cinematic tools
### Shader Graph
Variant Keyword Prefiltering introduces the early exclusion of “multi_compile” keywords, based on Prefiltering Attributes driven by **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) settings. This greatly reduces the amount of variants being enumerated for potential stripping and compilation. The result is a significant reduction in **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) processing time.
## Asset Store
Added [Verified Solutions](https://docs.unity3d.com/6000.0/Documentation/Manual/verifiedsolutions.html) program, a library of third-party assets and solutions that Unity curates.
## Asset bundles
Added capability to Asset Bundles that target Windows, OSX, and Linux platforms and the Dedicated Server subtarget so that they’re now built with the same Dedicated Server optimizations that built Dedicated Server Players receive (removing texture data and non-collision mesh data).
## Asset pipeline
Implemented accessor for saving data to .meta files.
## Authoring Tools
### 2D
  * Added API to allow **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sprite-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Sprite) to get and set references to ScriptableObjects.
  * Added Brush Picks to the Tile Palette window.
  * Added options to create WhiteBox Tile Palettes.
  * Added preference option to Tile Palette Preferences for users to choose where they would want to position their mouse cursor when painting on **Tilemaps** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap) with Z Position.
  * Added Sample for Custom Geometry Generation and Vertex Colors.
  * Added Sprite/SpriteShape/TilemapRenderer as mask sources for SpriteMask.
  * Added SRP Batching for 2D Renderers and Particle Renderer to support URP.
  * Added support for **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) frustum culling to Inverse **Kinematics** The geometry that describes the position and orientation of a character’s joints and bodies. Used by inverse kinematics to control character movement.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#kinematics) Manager 2D.
  * Enabled opening Sprite Editor Window from SpriteRenderer **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) to edit the Sprite that is assigned to the SpriteRenderer.
  * Enabled ScriptablePacker to add custom packing algorithm for SpriteAtlas.


### 2D Physics
  * Added a `Rigidbody2D.Slide` method which allows a Rigidbody2D to move with a specific velocity over a specific integration time and perform various slide, gravity, slip, direction-change, and surface-anchoring behaviors automatically. This method works on all **body types** Defines a fixed behavior for a 2D Rigidbody. Can be Dynamic (the body moves under simulation and is affected by forces like gravity), Kinematic (the body moves under simulation, but and isn’t affected by forces like gravity) or Static (the body doesn’t move under simulation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#BodyType), including Static bodies. It can simply calculate a new position, change the Rigidbody2D position immediately (supports interpolation), or defer the movement by automatically calling `Rigidbody2D.MovePosition()`. This feature makes **Character Controllers** A simple, capsule-shaped collider component with specialized features for behaving as a character in a game. Unlike true collider components, a Rigidbody is not needed and the momentum effects are not realistic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CharacterController) easier to create.
  * Added the ability to use sub-stepping simulation when Simulation Mode is Update.
  * Enabled CompositeCollider2D to allow each Collider2D to select one of four composite operations: Merge (OR), Intersect (AND), Difference (NOT), and Flip (XOR), and a composite order for controlling the order that each Collider2D will be composited.


### Terrain
  * Migrated **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) Tools to the Overlays **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) framework to ensure that users have consistent and predictable Editor **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) authoring workflows.
  * Added Quality Settings to control various Terrain settings at different quality levels.


## Core
Merged the APV window with the Lighting window.
## Editor and Workflow
  * Improved and standardized right-click context menus across items and workflows. Improvements include more consistent interactions, sorting optimizations, and an optional search field.
  * Added a new launch screen for the Linux Editor.
  * Added [async test support](https://docs.unity3d.com/Packages/com.unity.test-framework@1.3/manual/reference-async-tests.html) with documentation and support for SetUp and TearDown to the test-framework.
  * Added Editor **analytics** Abbreviation of **Unity Analytics**  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Analytics) event tracking for Refresh access and New link button clicks.
  * Added the Enable PlayMode Tooltips** **toggle to the preferences window. This toggle enables tooltips in the Editor while it’s in Play mode.
  * Added the Helper Bar, which displays useful keyboard shortcuts, to the status bar. Enable the Helper Bar from the General tab of the Preferences window.
  * Added the option for **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) preferences to only refresh the Scene view when the Editor is in focus.
  * Added an optional priority argument to [Shortcut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutAttribute-ctor.html) and [ClutchShortcut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ClutchShortcutAttribute-ctor.html) attributes.
  * Added a rebindable shortcut possibility for the Game view Stats button to the Shortcuts manager.
  * Added Stage, Scope, and Dynamic information to keywords for the Frame Debugger.
  * Added the possibility of running tests in a specified order from a test list.
  * Added the `focusedWindowChanged` callback to the `EditorWindow` class.
  * Changed to title bars on Windows for Editor. Improves upon the existing title bar feature by adding to it.
  * Displayed `OneTimeSetup` and `OneTimeTearDown` durations in the XML result under outputs.
  * Enabled adding a shortcut to enable or disable a capture for the Frame Debugger.
  * Enabled connection to **Perforce** A version control system for file change management. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/perForceIntegration.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Perforce) servers using accounts with MFA.
  * Enabled copying a foldout or an entire event for the Frame Debugger.
  * Enabled seeing the Original and Used shaders in an event for the Frame Debugger. This is useful for events that use USEPASS or fall back to an assigned fallback shader.
  * Enabled setting the minimum and maximum values for the Levels slider for the Frame Debugger.
  * Enabled shortcut binding to mouse wheel turns for Shortcut Manager.
  * Enabled viewing the individual meshes in a SRP Batch inside the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Preview for the Frame Debugger.
  * Split the **texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat) for the Frame Debugger into Color Format and DepthStencil Format.
  * Changed to title bars on Windows for the Editor.


### UI Toolkit for Editor UI
  * Added a Text preview to the UI Builder Inspector.
  * Added an anchor widget to the Position properties in the UI Builder Inspector pane.
  * Added basic analytics in UI Builder.
  * Added space-evenly to Justify Content property.
  * Added support for Bitmap Text.
  * Added Vertex Buffer size configuration.
  * Updated tooltips.


### IMGUI
Removed dependency on Legacy Text stack for IMGUI so that IMGUI now renders and calculates its metrics using TextCore. Some members from TextEditor have been deprecated to accommodate for the new TextUtilities used by both IMGUI and UITK. Their meanings are the same but their names have changed (from field to property):
  * `TextEditor.multiline` is now `TextEditor.isMultiline`.
  * `TextEditor.hasHorizontalCursorPos` is `nowTextEditor.hasHorizontalCursor`.
  * `TextEditor.revealCursor` is now `TextEditor.showCursor`.


### TextMeshPro
Added support for Color Glyphs and extracting OpenType font features.
## Enterprise deployment
  * Added support on Windows for [Automatic proxy configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/ent-proxy-autoconfig.html). With this feature, you can use Unity applications seamlessly in a web proxy environment, with minimal configuration.
  * If you use Unity on a Windows computer that lacks elevated privileges, you can [enable the installation of Unity Editors by standard users](https://docs.unity3d.com/6000.0/Documentation/Manual/ent-unpriv-install.html).


## Graphics
  * Added Screen Space **Lens Flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) that you can generate from all lights visible on the screen (direct, indirect, emissive surfaces, specular highlights) in just a few clicks with a single **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) volume. These lens flares are compatible with both HDRP and URP. This feature complements the Lens Flare (SRP) component, which gives you more advanced artistic control over lens flares from lights, but which you can only use on predefined light sources (directional, point and spot lights), and can only manually associate with each one.
  * Dynamic shader variant loading provides additional user control over shader loading behavior and memory usage. This optimization enables the streaming of shader data chunks into memory, and eviction of shader data that is no longer needed at runtime, based on a user controlled memory budget. This allows to significantly reduce shader memory usage on platforms with limited memory budgets.
  * Added asynchronous compilation of pipeline state objects for shader warmup.
  * Added DirectX Raytracing (DXR) 1.1 support in compute shaders. Added the following APIs: `SystemInfo.supportsInlineRayTracing`, `SystemInfo.supportsRayTracingShaders`, `ComputeShader.SetRayTracingAccelerationStructure`, and `CommandBuffer.SetRayTracingAccelerationStructure`(ComputeShader, …).
  * Added `#pragma require inlineraytracing` to compute shaders.
  * Added new `RayTracingAccelerationStructure.AddInstance` signature that allows adding mesh instances to the acceleration structure for GPU **ray tracing** The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Raytracing). This is the equivalent of `Graphics.RenderMesh` from the **rasterization** The process of generating an image by calculating pixels for each polygon or triangle in the geometry. This is an alternative to ray tracing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rasterization) pipeline.
  * Added foveated rendering support for D3D12/Vulkan.
  * Added foveated rendering support for Metal.
  * Added support for loading EXR data through `ImageConversion.LoadImage()`.
  * Added support for VK_EXT_debug_utils on Vulkan platforms.
  * Added mipmap limit groups, for more fine-grained configurability over the single value that applies to all mipmapped Texture2D assets.
  * Added the ability in the Texture2D importer and constructor to add the texture to a project-defined mipmap limit group for more fine-grained control of how texture quality is affected per quality level.
  * Added the ability in the Texture2D importer and constructor to exclude the texture from mipmap limits, ensuring that all mipmap levels can be uploaded regardless of the quality settings.
  * Added a runtime-modifiable Texture2D property to toggle excluding readable textures from mipmap limits.
  * Added the ability to compute the thickness of an Object.
  * Enabled Ray Tracing Support in Terrain settings by default for new Terrains.
  * Implemented `ScriptableRenderContext.CullShadowCasters` API to kick theBatchRendererGroup culling jobs earlier in URP and HDRP.
  * Added standardized shader variant keyword for native 16-bit shader types.
  * Added standardized shader variant keywords for wave operations.
  * Added debug view to visualize probe sampling.


### Lighting
  * Introduced the new LightBaker v1.0 backend for manual lighting bakes, which makes baking more predictable and stable. Manual bakes no longer restart if you change the scene during baking; therefore, the Editor is more responsive during baking. If you bake with the GPU backend, you can use a Baking Profile to select the tradeoff between performance and GPU memory usage.


### Universal Render Pipeline (URP)
For a complete description of new features and improvements in URP, refer to [What’s new in URP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@15.0/manual/whats-new/urp-whats-new.html). 
#### New features in URP
  * Added [temporal anti-aliasing (TAA)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/manual/anti-aliasing.html#temporal-anti-aliasing-taaa-nametaaa) support which is available from Camera Anti-aliasing settings. Incompatible with MSAA, **Dynamic Resolution** A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution), or Camera stacking. Supports fixed resolution only, so no temporal upsampling is supported.
  * Added support for [High Dynamic Range (HDR) output](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@16.0/manual/post-processing/hdr-output.html).
  * Added Detailed Stats to URP Rendering Debugger.
  * Ported all URP passes to use the RasterCommandBuffer API.
  * Added AO Method dropdown for SSAO to select Interleaved Gradient Noise or Blue Noise.
  * Added Blur Quality dropdown for SSAO to select High (Bilateral), Medium (Gaussian), or Low (Single-Pass Kawase).
  * Added clustered **reflection probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) support to the URP Forward+ **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath). This enables the use of more than two reflection probes per object, allows Unity to skip per-object culling of lights and reflection probes, and enables Entities Graphics and procedural draws to make use of reflection probes.
  * Added Custom Post Processing (zero code path) feature in URP.
  * Added Decal support to Render Graph.
  * Added falloff field for SSAO to control the distance from the camera that the AO should affect.
  * Added RenderGraph support to URP postFX.
  * Added shadow interoperability with Sprite, **Colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider), SpriteShape, and 2D Animation.
  * Added soft shadow rendering. Shadow softness can be set on shadow casting Light2Ds.
  * Added a limited version of Probe Volumes, with no interpolation of lighting data sets, and limited performance on lower end hardware.


#### Improvements in URP
  * Improved FXAA quality. The changes result in an improved edge AA (removing odd edge artifacting seen before) while better retaining texture quality. The performance requirements are expected to be unchanged. Output quality should now be similar to the low and medium SMAA presets while still having better performance.


### High Definition Render Pipeline (HDRP)
For a complete description of new features and improvements in URP, refer to [What’s new in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@15.0/manual/whats-new-15.html).
#### New Features in HDRP
  * Light Layers and Decal Layers are now managed in similar ways in both HDRP and URP. In HDRP they now share the first 16 Rendering Layers, instead of using 8 separate bits each. Additionally, a new option in the HDRP Asset allows access to a full screen buffer that contains the Rendering Layers Masks of rendered Objects. HDRP can sample that buffer from the ShaderGraph through the HD Sample Buffer node, and use it to implement custom effects, like outlining objects on a specific rendering layer.
  * All Ray Tracing HDRP features (raytraced shadows, reflections, AO, global illumination, path tracing, recursive rendering,…) are officially out of experimental in Unity 2023.1.0.
  * Added a foam system to the HDRP Water System.
  * Probe Volumes are out of experimental. Revamped the control interface to provide a better experience when you place Probe Volumes, light dynamic objects and some static objects, stream data from GPU memory, interpolate lighting data sets, and work with volumetric fog and particles.
  * Added a third level of noise for volumetric clouds.
  * Added Generic Rendering Layer mode support.
  * Added [High Quality Line Rendering](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@15.0/manual/Override-High-Quality-Lines.html) which unlocks improved performance and image quality for line topology.
  * Added improvements to the SSS lighting model.
  * Added Ray Tracing Terrain support for HDRP.
  * Added raytraced shadows for Pyramid and Box shaped Spot Lights.
  * Added the Ray Tracing Light Cluster to Path Tracer.
  * Added volumetric material support for local volumetric fog volumes.
  * Exposed Material Type in materials using the Lit Shader Graph.
  * Improved stripping of unused features.
  * **Specular color** The color of a specular highlight.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#specularcolor) on HDRP/Lit and HDRP/StackLit below 2% can be used to suppress specular lighting completely when “Specular Fade” is enabled.


#### Improvements in HDRP
  * Improved the water rendering system in the following ways: 
    * Added functionality to Water Mask so it dynamically removes water from inside a boat or in a cave in the middle of an island.
    * Modified the water deformer to dynamically deform water locally. For example, to deform water around a moving ship, deform waves near shores, or deform water in a vortex.
    * Added flow maps to create local currents, to manage surface waves that follow currents, and the water query API to allow objects to drift.
    * Added a water line to manage the transition for cameras that are half underwater.
    * Improved visual quality of water.
    * Improved the UX of the water system.
  * Added an extra optional pass to compute thickness of transparent objects at runtime to get more accurate refraction and transparency rendering.
  * Improved visual quality when using temporal anti-aliasing (TAA) with two new options to perform sharpening. The first option is a post-process pass that offers higher quality sharpening, control over the amount of sharpening, and an option to reduce possible ringing artifacts. The second option is to run Contrast Adaptive Sharpening from AMD FidelityFX.
  * Specular light can now be completely faded when using a specular color workflow using the HDRP/Lit and HDRP/StackLit shaders by toggling a new option that can be found in the HDRP Global Settings under Miscellaneous/Specular Fade.


## Multiplayer tools
Added [Multiplayer Play Mode as an experimental feature](https://docs-multiplayer.unity3d.com/tools/current/mppm/). Multiplayer Play Mode is a workflow improvement feature from our multiplayer toolset that aims to deliver a user experience that is “single-player like”, but with a focus on the development cycle of multiplayer games. 
## Networking
Added new Dedicated Server Standalone player options to assembly definition exclude and include platform lists.
## Package Manager
  * Added functionality to track assets imported from an **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) package: 
    * Added an **Imported Assets** tab in the [package details view](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html) (My Assets) to visualize imported assets.
    * Added a **Remove** button and window for Asset Store packages, to selectively remove imported assets.
  * Enhanced the user experience for [deprecated packages](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-deprecated.html). The Unity Editor notifies users at startup if their project has any deprecated packages. Updated the Package Manager window to identify two types of package deprecation: 
    * Packages that reach their end of life and are no longer supported in the given Editor.
    * A specific version of a package marked as deprecated.
  * Added **Web3** as a category in the [Filters](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-filter2.html) menu when viewing My Assets.
  * Changed the default sorting in the My Assets view to **Purchased date** , to match the default sort method in Asset Store.
  * Changed the [install menu items](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-actions.html) to start with **Install** instead of **Add**.


## VFX Graph
  * Added a new output to modify the volumetric fog of HDRP.
  * Added VFX integration in Ray Tracing.
  * Fixed the six-way lighting and **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) remapping options.
  * Optimized CPU and GPU VFX runtime in VFX Instancing.


## Platform Graphics
  * Introduced a new graphics jobs threading mode called Split Graphics Jobs that is proven to reduce unnecessary begin and end of frame synchronization between the main and native graphics job threads. The Unity Testing team observed significant performance improvements when targeting DX12 using Split Graphics Jobs over DX11.


### Android
  * Added support for [texture compression targeting](https://developer.android.com/guide/playcore/asset-delivery/texture-compression) which compresses textures multiple times using different formats. This helps to serve optimized **APKs** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#APK) for different Android devices. For more information, refer to [Texture compression targeting](https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution-google-play.html#texture-compression-targeting).
  * Added the Android Project Configuration Manager which is a flexible and robust way to configure Android **Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) settings. This replaces the old method of using templates. For more information, refer to [Android Project Configuration Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-methods.html#agp).
  * Added support for [GameActivity](https://developer.android.com/games/agdk/game-activity), which is an application model available for Android projects powered by [Android’s Game Development Kit](https://developer.android.com/games/agdk). It provides more control over the essential parts of an application, gives more freedom and flexibility in the core code, and minimizes the amount of JNI that an application needs to use. It also improves how games work with Jetpack components, enables you to overlay native elements, and helps you more easily take advantage of new platform features. For more information, refer to [The GameActivity application entry point](https://docs.unity3d.com/6000.0/Documentation/Manual/android-application-entries-game-activity.html).
  * Extended [Unity’s Memory API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-memoryUsageChanged.html) to take advantage of Google Memory Advice library. This provides you with fine-grained information on memory usage which you can use to adjust your application accordingly.
  * Exposed [Android’s reportFullyDrawn API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.DiagnosticsReporting.CallReportFullyDrawn.html) so you can get more accurate information on your application’s startup time, one of the major metrics of user experience. This gives you a better understanding of your application’s cold and warm start rates across devices which you can use to further optimize the application.
  * Added `build_fingerprint` information to Android builds.


### WebGL
  * Extended the diagnostics overlay in web builds with more metrics and graphs.
  * Improved console error message logs when `Content-Encoding: gzip` is not properly set on server, or when a web browser has a bug that prevents it from being able to decompress gzip content.


### Windows
Enabled Windows ARM64 Player compilation. For more information, visit the [System Requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html) page.
## Programmer tools
### Kernel
Added functionality to control player connection listen port.
### Version Control
  * Added a new Branch Name column in the Changesets view.
  * Added changelist related options to pending changes context menu.
  * Added option to enable changelists and display them in pending changes tab.


### Scripting
Added [an option to display C# source code line numbers](https://docs.unity3d.com/6000.0/Documentation/Manual/il2cpp-managed-stack-traces.html) in call stacks in player builds.
## Profiler
  * Added metadata support for RenderTextures in Memory **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler).
  * Improved graphics memory tracking in Memory Profiler.


## Ray tracing API
The Ray Tracing API is officially out of experimental status in Unity 2023.1. This change is introduced after recent improvements to the Ray Tracing API, ranging from stability and performance to additional compatibility with the engine’s existing **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset).
## SpeedTree
`HDRP/Nature/SpeedTree8.shadergraph` now uses its Subsurface Map for the Transmission Mask node to remove the unintended light transmission from tree barks and twigs. This also fixes the overly bright **billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) lighting which didn’t quite match the 3D geometry’s lighting.
## UTP
**Experimental Feature Release**
The Unity Transport Protocol (or UTP) is a lower-level **networking** The Unity system that enables multiplayer gaming across a computer network. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/multiplayer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Networking) infrastructure that handles the transport of data across the network and across connected platforms and devices. In the most recent release we are enabling Web and TCP connections to improve the reach of our netcode solutions (like Netcode for Gameobjects and Netcode for Entities).
## Video
  * Enabled VideoPlayer time update mode for PS4 and PS5.
  * **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) VideoPlayer now has a configurable time update mode, to support game time, unscaled game time and audio dsp time.


## Visual Scripting
  * Added a confirmation dialog when you reset assemblies and types in **Project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings).
  * Added a confirmation dialog when you reset Project settings and Editor preferences.
  * Added Sticky Notes for ScriptGraph and StateGraph.
  * Added support for parameter renaming in code used by API nodes.
  * Added support for nodes to have a button which triggers a custom action in their Inspector description.
  * Added support to convert nodes with an unknown type to placeholder nodes. These nodes return to normal when their original type is redefined, or if you replace the node.


## Additional resources
  * [New in Unity 6.0](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNewUnity6.html)
  * [New in Unity 6.0 Preview](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNewUnity6Preview.html)
  * [New in Unity 2023.2](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20232.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20232.html)
New in Unity 2023.2
[](https://docs.unity3d.com/6000.0/Documentation/Manual/install-and-upgrade.html)
Install and upgrade
