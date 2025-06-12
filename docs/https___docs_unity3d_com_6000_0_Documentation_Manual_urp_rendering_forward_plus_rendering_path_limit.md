* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-plus-rendering-path-limitations.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * Troubleshooting the Forward+ rendering path in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
Make a shader compatible with the Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
Installing and upgrading URP
# Troubleshooting the Forward+ rendering path in URP
## Reduce build time
Due to the wide variety of use cases, target platforms, renderers, and features used in projects, certain URP configurations can result in a large number of **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variants. That can lead to long compilation times.
Long shader compilation time affects both player build time and the time for a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) to render in the Editor.
The per-camera visible light limit value affects the compilation time for each **Lit** and **Complex Lit** shader variant. In the Forward+ **Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath), on desktop platforms, that limit is 256.
This section describes how to reduce the shader compilation time by changing the default maximum per-camera visible light count.
### Change the maximum number of visible lights
**Note:** This instruction describes a workaround for a limitation in the URP design. This limitation will be mitigated in one of the future Unity versions.
The [Universal Render Pipeline Config package](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/URP-Config-Package.html) contains the settings that define the number of maximum visible light. The following instructions describe how to change those settings.
**Note:** If you upgrade the Unity version of your project, repeat this procedure.
  1. In your project folder, copy the **URP Config Package** folder from `/Library/PackageCache/com.unity.render-pipelines.universal-config` to `/Packages/com.unity.render-pipelines.universal-config`.
  2. Open the file `/com.unity.render-pipelines.universal-config/Runtime/ShaderConfig.cs.hlsl`.
The file contains multiple definitions that start with `MAX_VISIBLE_LIGHT_COUNT` and end with the target platform name. Change the value in brackets to a suitable maximum in-frustum per-camera light count for your project, for example, `MAX_VISIBLE_LIGHT_COUNT_DESKTOP (32)`.
For the **Forward+** Rendering Path, the value includes the Main Light. For the **Forward** Rendering Path, the value does not include the Main Light.
  3. Open the file `/com.unity.render-pipelines.universal-config/Runtime/ShaderConfig.cs`.
The file contains multiple definitions that start with `k_MaxVisibleLightCount` and end with the platform name. Change the value so that it matches the value set in the `ShaderConfig.cs.hlsl` file, for example `k_MaxVisibleLightCountDesktop = 32;`.
  4. Save the edited files and restart the Unity Editor. Unity automatically configures your project and shaders to use the new configuration.


Now the Player build time should be shorter due to the reduced compilation time for each shader variant.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
Make a shader compatible with the Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/InstallingAndConfiguringURP.html)
Installing and upgrading URP
