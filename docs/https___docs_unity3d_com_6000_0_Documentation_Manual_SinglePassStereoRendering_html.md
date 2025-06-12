* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SinglePassStereoRendering.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * [XR graphics](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-graphics.html)
  * Stereo rendering


[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-render-pipeline-compatibility.html)
Universal Render Pipeline compatibility in XR
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SinglePassInstancing.html)
Single-pass instanced rendering and custom shaders
# Stereo rendering
VR and most **MR** Mixed Reality  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MR) devices require rendering the Unity **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) in stereo. Unity **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) supports two stereo render modes:
  * **Multi-pass** : in this mode, Unity performs a render pass for each eye. Some parts of the render loop are shared between the two passes, so multi-pass rendering is faster than rendering the scene with two unique **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). Multi-pass mode provides the widest compatibility with existing **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) and rendering utilities, but is slower than single pass instanced mode.
  * **Single-pass instanced** : in this mode, Unity renders the scene in a single pass using instanced draw calls. This mode greatly decreases CPU usage and slightly decreases GPU usage compared to the multi-pass mode.
  * **Multiview** : A variation of single-pass instanced rendering supported by some OpenGL and OpenGL ES devices. This option replaces single-pass instanced when available.


**Note:** The earlier technique of rendering the scene into a double-wide texture using a single render pass is no longer available.
Single-pass instanced stereo rendering is now available on most **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) platforms.
## Set the render mode
You can find the **Render mode** setting under **XR**Plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) Management** in ****Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings)**. Each XR provider plug-in provides its own setting, if supported.
To set a render mode:
  1. Open **Project Settings** (menu: **Edit > Project Settings**).
  2. Expand the **XR Plugin Management** section, if necessary.
  3. Select the settings page for the relevant provider plug-in.
  4. Choose a mode from the list.

![Render mode options in the MockHMD provider plug-in](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SinglePassStereoRendering3.png) Render mode options in the MockHMD provider plug-in
**Note:** Some plug-ins name the setting **Stereo Rendering Mode**. 
## Single-pass instanced render mode support
Single-pass instanced render mode is supported on the following platforms and devices:
  * Android devices that support the Multiview extension
  * HoloLens
  * PlayStation VR
  * PC devices (tethered):
  * For DirectX on desktop, the GPU must support Direct3D 11 and the `VPAndRTArrayIndexFromAnyShaderFeedingRasterizer` extension.
  * For OpenGL on desktop, the GPU must support one of the following extensions: 
    * `GL_NV_viewport_array2`
    * `GL_AMD_vertex_shader_layer`
    * `GL_ARB_shader_viewport_layer_array`


If you set the **Render Mode** to **Single Pass Instanced** when that mode is not supported, then rendering falls back to multi-pass mode.
**Notes:**
  * Unity doesn’t support single-pass instanced rendering in the built-in **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) when using Shader Graph.
  * Unity doesn’t support single-pass instanced rendering in the built-in render pipeline when using deferred rendering.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-render-pipeline-compatibility.html)
Universal Render Pipeline compatibility in XR
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SinglePassInstancing.html)
Single-pass instanced rendering and custom shaders
