* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-global-settings.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Universal Render Pipeline reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-reference-landing.html)
  * Graphics settings window reference for URP 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html)
Universal Renderer asset reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/high-definition-render-pipeline.html)
Using the High Definition Render Pipeline
# Graphics settings window reference for URP
If a project has the Universal Render Pipeline (URP) package installed, Unity shows URP-specific graphics settings in **Project Settings** > **Graphics** > **Pipeline Specific Settings** > **URP**.
The section contains the following settings that let you define project-wide settings for URP.
You can also add your own settings. Refer to [Add custom settings](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/add-custom-graphics-settings) in the Scriptable **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (SRP) Core manual for more information.
## Default Volume Profile
Use this section to assign and edit a [Volume Profile](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html) for the default volume that all **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) use. Refer to [Understand Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volumes.html) for more information.
**Property** | **Description**  
---|---  
**Volume Profile** | Set the [Volume Profile](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html) the global default volume uses. You can’t set **Volume Profile** to **None**.  
URP displays all the properties for all the possible [Volume Overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html). To edit or override the properties, use [the global volume for a quality level](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/set-up-a-volume.html#configure-the-global-volume-for-a-quality-level) or [create a volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/set-up-a-volume.html#add-a-volume).
## Adaptive Probe Volumes
**Property** | **Description**  
---|---  
**Probe Volume Disable Streaming Assets** | When enabled, URP uses [streaming assets](https://docs.unity3d.com/6000.0/Documentation/Manual/StreamingAssets.html) to optimize [Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html). Disable this setting if you use Asset Bundles and Addressables, which aren’t compatible with streaming assets.  
## Additional Shader Stripping Settings
The check boxes in this section define which **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variants Unity strips when you build the Player.
**Property** | **Description**  
---|---  
**Export Shader Variants** | Output two log files with shader compilation information when you build your project. For more information, refer to [Shader stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shader-stripping.html).  
**Shader Variant Log Level** | Select what information about Shader variants Unity saves in logs when you build your Unity Project.  
Options:  
• Disabled: Unity doesn’t save any shader variant information.  
• Only SRP Shaders: Unity saves only shader variant information for URP shaders.  
• All Shaders: Unity saves shader variant information for every shader type.  
**Strip Debug Variants** | When enabled, Unity strips all debug view shader variants when you build the Player. This decreases build time, but prevents the use of Rendering Debugger in Player builds.  
**Strip Unused Post Processing Variants** | When enabled, Unity assumes that the Player does not create new [Volume Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html) at runtime. With this assumption, Unity only keeps the shader variants that the existing [Volume Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html) use, and strips all the other variants. Unity keeps shader variants used in Volume Profiles even if the scenes in the project do not use the Profiles.  
**Strip Unused Variants** | When enabled, Unity performs shader stripping in a more efficient way. This option reduces the amount of shader variants in the Player by a factor of 2 if the project uses the following URP features:
  * Rendering Layers
  * Native Render Pass
  * Reflection Probe Blending
  * Reflection Probe Box Projection
  * SSAO Renderer Feature
  * Decal Renderer Feature
  * Certain post-processing effects

Disable this option only if you notice issues in the Player.  
**Strip Screen Coord Override Variants** | When enabled, Unity strips Screen Coordinates Override shader variants in Player builds.  
## Render Graph
Use this section to enable, disable or configure the render graph system. Refer to [Render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html) for more information.
**Property** | **Description**  
---|---  
**Compatibility Mode (Render Graph Disabled)** | When enabled, URP doesn’t use the render graph system. For more information, refer to [Compatibility Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html). **Note:** Unity only develops or improves **rendering paths** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) that use the render graph API. Disable this setting and use the render graph API when developing new graphics features.  
**Enable Compilation Caching** | When enabled, URP uses the compiled render graph from the previous frame when it can, instead of compiling the render graph again. This speeds up rendering.  
**Enable Validity Checks** | When enabled, URP validates aspects of a render graph in the Editor and in a **development build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/https:/docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild). **Enable Validity Checks** is disabled automatically in final builds.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html)
Universal Renderer asset reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/high-definition-render-pipeline.html)
Using the High Definition Render Pipeline
