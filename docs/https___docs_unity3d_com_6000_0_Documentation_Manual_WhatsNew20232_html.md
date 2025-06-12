* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20232.html

  * [What's new in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew.html)
  * New in Unity 2023.2


[](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNewUnity6Preview.html)
New in Unity 6.0 Preview
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20231.html)
New in Unity 2023.1
# New in Unity 2023.2
## Release Notes
To find out more about the new features, changes, and improvements to this Unity version, refer to the [2023.2 Release Notes](https://unity3d.com/unity/whats-new/2023.2.0).
To find the release notes for other releases, refer to the [Unity download archive](https://unity.com/releases/editor/archive).
## Upgrade Guide
If you are upgrading existing projects from 2023.1, read the [Upgrade Guide to 2023.2](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuide20232.html) for information about how your project might be affected.
# What’s new
Find out what’s changed in Unity 2023.2 since 2023.1 and view the documentation for the affected areas.
## Accessibility
Added a new Editor window, the Accessibility Hierarchy Viewer, that displays the active accessibility hierarchy and its nodes. To access the Accessibility Hierarchy viewer, go to **Window > Accessibility > Accessibility Hierarchy viewer** in the main menu.
## Audio
  * Added the [Audio Random Container](https://docs.unity3d.com/6000.0/Documentation/Manual/Create-randomized-playlist.html) to randomize audio and ensure that volume, pitch, time and triggers can be set to non-repetitive intervals, so your game never sounds the same twice.
  * Added a VU meter to the Audio Random Container.


## Authoring Tools
### 2D
Added overlay support to the **Tile Palette** editor window. 
### Editor and Workflow
  * Added the [Scene view context menu](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewContextMenu.html). You can now access new context menus in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view by right-clicking or using a customizable keyboard shortcut. These menus, created with the UI Toolkit and extensible in C#, offer easy access to frequently used commands.
  * Added the **Refresh the**Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) only when the Editor is in focus** option to the [Scene view preferences](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html#scene-view). Enable this option to refresh the Scene view only when the Editor is in focus.
  * Added the ability to bind a keyboard shortcut to make transitions between Animator states.
  * Added basic OpenType font feature support. Currently, only kerning is enabled.
  * Added a new [Cameras overlay](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-overlay.html) to replace the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) preview. You can use the Cameras overlay to take [first-person control of cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/control-camera.html) and manage cameras in the Scene view.
  * Replaced most OS contextual menus with the UI Toolkit version.
  * Added the Color Checker, which is a tool used to calibrate lighting and post process. The Color Checker is an object that the user can add through **GameObject** > **Rendering** > **Color Checker Tool**. The tool is meant only as a production tool for lighting artists and won’t be saved in Build.
  * Enabled the Editor to show different license notification modals.
  * Added a `PropertyCollectionAttribute`, which you can use to implement custom drawers for collections.
  * Added a new tool for light placement using the pan, zoom, and orbit controls of the Camera. For more information, refer to [View and control a light from its perspective](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/lights-placement-tool.html).


### UI Toolkit
  * You can now use a new and flexible [runtime binding system](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-runtime-binding.html) to effortlessly connect data values to UI element properties when you create the Editor or runtime UI. You can configure data binding in either UI Builder or C# code.
  * Added new controls such as the [ToggleButtonGroup](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ToggleButtonGroup.html), [Tab](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Tab.html), and [TabViews](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TabView.html), and made improvements to existing controls.
  * Added icon support to the [Button](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-Button.html), ListView, and TreeView controls.
  * Added new UxmlElement and UxmlAttribute attributes. These attributes replace the existing UxmlFactory and UxmlTraits when you [create custom controls](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-custom-controls.html). This streamlines the creation of custom controls, offering an efficient alternative through C# attributes, and eliminating the need for extensive code writing. Additionally, you can now create [custom property drawers](https://docs.unity3d.com/6000.0/Documentation/Manual/ui-systems/custom-control-customize-uxml-attributes.html#add-custom-property-drawer-in-ui-builder) for fields in the same manner as the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)**.
  * Enhanced UI Builder with improvements to display what drives style properties, refined canvas manipulation, and made other enhancements. The updated UI Builder now also supports the authoring of UXML Objects, enabling the editing of the MultiColumnTreeView and MultiColumnListView.
  * Added the Emojis Fallback Support field to [TextElement](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextElement.html) and [TextField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TextField.html) to control the ordering of where to search for the glyph in the emoji range (primary font vs global fallback). Additionally, added basic support for the OpenType font features, with the current focus on enabling kerning.
  * Added a new Spacing field with a box model widget in the UI Builder’s Inspector.


### TextMeshPro
  * Added basic Emoji support.
  * Added basic OpenType font feature support, only kerning has been enabled for now.


## Graphics
  * Batched Compute **Skinning** The process of binding bone joints to the vertices of a character’s mesh or ‘skin’. Performed with an external tool, such as Blender or Autodesk Maya. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingHumanoidChars.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skinning): Unity’s Skinned **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer component uses compute dispatches for parallelizing vertex transformations on the GPU. Unity 2023.2 introduces optimizations to Skinned **Mesh Renderers** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) across all supported platforms. These optimizations aim to batch compute skinning and blendshape dispatches. This can increase the amount of vertices deformed in parallel and improve the GPU performance of character and skinned mesh rendering.
  * The Progressive GPU **Lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) is now out of preview and fully supported.
  * Added APIs to move **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) positions at runtime.
  * Removed the **Auto Generate** setting in the Lighting window. Related APIs are now obsolete. To check **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) while you’re editing, you can now select a Scene View Draw Mode and set **Lighting Data** to **Preview**. This displays a preview of the baked lighting. The preview lightmaps are non-destructive, and you can use them after you’ve baked the scene.
  * Added `BatchCullingContext.cullingFlags` to specify whether to cull lightmapped shadow casters.
  * Added `rendererPriority` support for `BatchRendererGroup`.
  * Added support for building **ray tracing** The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Raytracing) acceleration structures asynchronously on a compute queue. AsyncCompute CommandBuffers can now run `CommandBuffer.BuildRayTracingAccelerationStructure` commands. Added support for `RayTracingAccelerationStructure` to RenderGraph and Render Graph Viewer.
  * Added mipmap limit support for Texture2DArrays.
  * Added mipmap stripping support for Texture2DArrays.
  * Added support for providing tiled EXR images to LoadImage.
  * Enabled exposing raytracing acceleration structure build flags for balancing build times versus ray tracing speed and memory consumption on the GPU. You can customize flags from C# when creating and building a `RayTracingAccelerationStructure`, or via the Renderer settings.
  * Added Native Render Pass support for Vulkan for Android, Metal for iOS/MacOS (Apple Sillicon), and DirectX12 for Windows on ARM.
  * Added support for GPU batched skinning for D3D12 (Windows and XBox platforms).
  * Added the Custom Vertex Streams feature for particle trails.
  * Added `BakeTexture` and `BakeTrailsTexture` scripting methods.


### Universal Render Pipeline (URP)
For a complete description of new features and improvements in URP, refer to [What’s new in URP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@15.0/manual/whats-new/urp-whats-new.html). 
  * Added cross-platform **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) display support. HDR displays are capable of reproducing images in the higher range of difference in luminance closer to natural lighting conditions. HDR output preserves the contrast and quality of the linear lighting renders and HDR images displayed on these devices. The Editor and Standalone Players now provide full HDR tone mapping and display support, across all rendering pipelines and capable platforms, including mobile and **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR).
  * Added per-vertex quality levels for indirect lighting from Probe Volumes so that URP renders lit environments more efficiently. You might need to do further optimization on mobile because URP doesn’t support Lighting Scenario blending or Lighting Normalization for **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe).
  * Added a new option in the Motion Blur volume component called **Camera And Objects** that uses motion vectors to blur objects that move faster than the camera’s exposure time.
  * Added support for additional directional light cookies.
  * Added the Default Volume Profile field to URP Global Settings.
  * Added the Volume Profile field to the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) Asset.
  * Added Alembic velocity motion vector support for URP materials.
  * Added automatic **TimeBased** motion vector generation for ShaderGraphs with vertex animation based only on the **Time** node. All other data which affects position must be constant between frames.
  * Added support for XR rendering and cameras using orthographic projection to Forward+ **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath).
  * Added support for foveated rendering in the Forward+ rendering path.


### High Definition Render Pipeline (HDRP)
For a complete description of new features and improvements in URP, refer to [What’s new in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@16.0/manual/whats-new-16.html).
  * Added HDRP path tracer support for Decals projectors. The path tracer does not support emission from decals.
  * Added the ability to stream Probe Volume data from disk at runtime. You can enable or disable disk streaming for different quality levels.
  * Made HDRP **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph decals compatible with transparent objects. This means you can use decals created with Shader Graph to affect transparent objects to build procedural effects like rain drops, ripples, custom engravings, dirt effects on glass.
  * Added a night sky with stars and celestial bodies to the HDRP physical sky.
  * Added a Shader Graph output for the physically based sky and added controls to create a moon.
  * Added visualization of async compute passes and their synchronization points to the Render Graph Viewer.
  * Added beer shadow maps for volumetric clouds.
  * Added a Volume Profile field to HD Render Pipeline Asset.
  * Added a material type for thin objects with colored transmission.
  * Added the option to disable clear coat on the material for Lit ShaderGraphs.
  * Added the Global Pass API that you can use to inject custom passes in the render pipeline without any **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in a scene.
  * Added the volumetric fog fullscreen debug mode output for Arbitrary Output Variables (AOV).
  * Added Adaptive Probe Volumes (APV) ability to stream data directly from the disk. This feature is only available on devices with compute shader compatibility.
  * Added the ability to use the baking API to bake Adaptive Probe Volumes (APV) independently from lightmaps or reflection probes.


## Multiplayer
### Netcode for GameObjects
  * Added the **Refresh In-Scene**Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) Instances** option in the Network Object component context menu. Use this property to update the `GlobalObjectIdHash` value for prefab instances in the scene that existed before they had a `NetworkObject` component. This property affects all scenes included in the build list.
  * Added the `NetworkManager` methods `SetPeerMTU` and `GetPeerMTU` to give full control over Maximum Transmission Unit (MTU) sizes. Use this for custom protocols in Netcode for GameObjects.
  * Improved network prefab identification generation (for example, `GlobalObjectIdHash`) to fix issues where Unity assigned invalid values.
  * Improved the serialization API and codegen pipelines in the following ways: 
    * Added the `GenerateSerializationForTypeAttribute` method that you can apply to any class or method to ensure the specific type is included in the codegen serialization process.
    * Added the `GenerateSerializationForGenericParameterAttribute` method that you can use to include generic type(s) wrapped by a `NetworkVariable` type in the codegen process.
    * Exposed additional `NetworkVariableSerialization` methods to improve custom `NetworkVariable` creation without any boxing cost. You can use the `NetworkVariableBase.MarkNetworkBehaviourDirty` method to mark NetworkVariables as dirty.
  * RPCs in generic `NetworkBehaviour` types can now serialize parameters of the class’s generic types.
  * Improved support for 32-bit ARMv7 in Netcode.
  * Added additional `NetworkManager` events `OnServerStarted`, `OnServerStopped`, `OnClientStarted`, and `OnClientStopped` to provide better notification of the `NetworkManager` initialization process.


### Dedicated server platform
  * Added the **Dedicated Server Optimizations** option in the **player settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) that, when enabled, strips all shaders from server builds. Enable this option to considerably reduce the build time.


## Unity Transport
  * Unity Transport 2.X is the now the default and recommended version of [Unity Transport](https://docs-multiplayer.unity3d.com/transport/current/about/index.html).
  * It is now possible to configure the maximum message size that the transport sends through a new `maxMessageSize` parameter in `NetworkSettings.WithNetworkConfigParameters`. This is useful for environments where network equipment mishandles larger packets (like some mobile networks or VPNs). The value excludes IP and UDP headers, but includes headers added by the transport itself (for example, reliability headers). The default value is 1400. Note that both client and server should use the same value.


## Package Manager
### Changes to package cache management
  * Changed the default location and structure of the [global cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-cache.html).
  * The registry data cache is now limited to a default maximum size of 10 GB. You can override the default by [customizing the global cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-config-cache.html).


### Changes to the Package Manager window
  * Added a [navigation panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-nav.html): 
    * Added a panel to improve the navigation between views of package subsets. In earlier versions, these contexts were stored in the **Packages** dropdown menu.
    * Added **Services** as a dedicated entry in the Package Manager navigation panel.
    * Added **Updates** as a nested entry beneath **In Project** in the navigation panel. This nested view lists all the packages in your project that have updates available.
    * Added individual scoped registries as nested entries beneath My Registries in the navigation panel.
  * Enhancements to the [list panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-list.html): 
    * Added a **Packages -**Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore)** expander in the list panel of the **In Project** context, so you can view and manage Asset Store packages from the **In Project** view.
    * Relocated the [search box](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-search.html) and changed its behavior so it recalls your search terms on a per-context basis.
  * Enhancements to the [details panel](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-details.html): 
    * Improved the flow for managing packages in the **My Assets** context by streamlining the action buttons in the details panel. The most common action appears as the default action in a menu button, with additional actions listed in the menu. Also added an **In Project** label to clearly indicate when an Asset Store package is already imported into your project and up-to-date.
    * Updated the label of the **Import** button when viewing an Asset Store package. After you [download an updated Asset Store package](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-update2.html), the main action button label is **Import update #.# to project** , so it’s clear that you need to import the update to your project.
    * Updated the behavior of the [Documentation](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-docs.html#Editor) link for packages that you installed from a registry. You can now right-click the link and choose to **Open in browser** or **Open locally**.
    * Added a button to sign in with your Unity ID when you’re logged out and try to view the details of an Asset Store package.
  * Other enhancements: 
    * Updated the values in the [Filters](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-filter2.html) menu when you’re viewing the My Assets context.
    * Updated the label for the [Filters](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-ui-filter2.html) control so it shows the selected value rather than the parent category.


## Android
  * Added Addressables for Android package (`com.unity.addressables.android`) to provide Play Asset Delivery support for Addressables.
  * Added texture **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) format targeting support through Addressables for Android package to pack multiple **texture compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureCompression) formats to Android asset packs. At install-time, an **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#APK) is built only using the optimal texture compression formats based on the device’s mobile GPU to load and **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) quicker and with less memory.
  * Added `ApplicationExitInfo` API to provide information on application crashes and application not responding (ANR) errors.
  * Made these improvements: 
    * Made `GameActivity` as the default application entry point to provide more control over the interaction between Android and your application.
    * Raised the minimum supported Android version to 6.0 (API level 23).


## Physics
  * Added `ArticulationBody.jointPosition` pointer lines to the ****Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) Angular Limits** **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) to show the exact position of the joint in the Scene view.


## Profiler
  * Added metadata support for AudioClip and Shader in Memory **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler).
  * Added a Highlights module to the Profiler window.
  * Added a new Inverted Hierarchy view for the CPU Profiler.


## Raytracing API
  * Ray Tracing Acceleration Structure Build Flags: New Raytracing Acceleration Structure build flags were introduced to Unity’s renderers and RTAS API. These flags allow you to control the tradeoffs between ray tracing memory usage, RTAS build time and ray tracing performance. Developers and artists can use the new flags to fine tune the ray tracing performance in their scenes and renderers.
  * Inline Ray Tracing in Shaders: You can now use in-line ray tracing in **rasterization** The process of generating an image by calculating pixels for each polygon or triangle in the geometry. This is an alternative to ray tracing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rasterization) and compute shaders when targeting DXR1.1-capable Windows platforms, Xbox Series X/S, and Playstation 5. You can issue ray queries from within shaders to traverse the bound Raytracing Acceleration Structure and perform intersection testing. This allows you to implement all kinds of hardware accelerated raytracing effects and simulations.


## Shader Graph
  * Added UGUI support for Shader Graph. Shader Graph now has subtargets for Canvas in both URP and HDRP. UI artists can create custom shaders for their UI elements using Shader Graph. Define the overall look and style of UI elements, create animated UI effects, and define custom button states while using less texture memory.
  * Enabled Shader Graph Canvas Master Node to allow users to create UI shaders for Canvas in HDRP, URP, and Built-in.


## SpeedTree
Improved SpeedTree visual quality in HDRP using a Transmission Mask to apply subsurface scattering only on leaves. HDRP/Nature/SpeedTree8.shadergraph to use its Subsurface Map for the Transmission Mask node to remove the unintended light transmission from tree barks and twigs. This also fixes the overly bright **billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) lighting not matching the 3D geometry’s lighting.
## Splines
You can now store personalized data on Spline objects. Additionally, the interface for editing points in the Inspector has been enhanced and certain APIs have been made available to the public. When you work on splines, you can now use the new [Scene view context menu](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewContextMenu.html).
## Test Framework
  * Enabled retrying and repeating tests based on test level. Soon as the test finishes running its first iteration, the Editor now retries or repeats the test. Pass the command line arguments to the Editor to: 
    * Repeat x runs the test x amount of times or until it fails. This is useful for testing unstable tests.
    * Retry x if a test fails. This run the test x amount of times or until it succeeds.
  * You can now run the tests in a randomized order, by using the Editor command line new argument `-randomOrderSeed x`, where `x` is an integer different from 0. If a new test is added to the project, the Test Framework keeps the random order passing the same seed, and places the new test in the random list accordingly.
  * Added `TestFileReferences.json` to generate on a build step of the player, so that **Test runners** The Test Framework package (formerly called the Test Runner) is a Unity tool that tests your code in both Edit mode and Play mode, and also on target platforms such as Standalone, Android, or iOS. [More info](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TestRunner) can consume it to enrich data for the run step.
  * The UTF version now automatically updates for SRP tests.


## Version control
Added a project option to support tracking packages that exist on disk outside of the project’s root folder.
## VFX Graph
  * Added VFX Graph assets with a predefined effect to the template window. You can use these templates as a starting point for your own effects.
  * Added Custom HLSL blocks and operators. Custom HLSL nodes let you execute your own code during particle simulation. You can use an operator for horizontal flow or a block for vertical flow in the VFX Graph context.
  * Added URP Decals with VFX Graph. URP Lit decal output are now supported in VFX Graph, making it possible to create stunning decal effects on URP that matches correctly your scene lighting and materials
  * Added lighting for Shader Graph smoke effects in HDRP and URP. This means that you can create custom smoke shaders that use six-way lighting in lit shaders.
  * Extended the Camera Depth and Color buffer behavior in URP. This means you can use the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer) for depth-based **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) or sample the color buffer to create custom effects.
  * Added support for motion vectors in URP.
  * Added support for motion vectors with Shader Graph.
  * Added the ability to use VFX Graph’s Shade Graph integration to use the material variant workflow to override settings in the VFX Output.
  * Enabled VFX instancing with exposed textures, meshes, or graphic buffers.


## Web platform (previously WebGL)
  * Unity web builds now take advantage of the latest size and performance optimizations in the Emscripten toolchain.
  * Added support to specify the browser type and its executable path that you want your application to launch at runtime. You can specify this either using the command line or the GUI setting in the **Build Settings** window.


## XR
  * Added Hololens Automation Support.
  * Extended Unity’s integrated support for tone-mapping and outputting to HDR Displays in URP, HDRP and the built-in render pipeline to provide support for XR devices that have a HDR display.


## Additional resources
  * [New in Unity 6.0](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNewUnity6.html)
  * [New in Unity 6.0 Preview](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNewUnity6Preview.html)
  * [New in Unity 2023.1](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20231.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNewUnity6Preview.html)
New in Unity 6.0 Preview
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WhatsNew20231.html)
New in Unity 2023.1
