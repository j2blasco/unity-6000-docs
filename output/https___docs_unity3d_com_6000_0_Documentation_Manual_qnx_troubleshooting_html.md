* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-troubleshooting.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Embedded systems](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-systems.html)
  * [QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx.html)
  * [Develop for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-develop.html)
  * Troubleshooting the QNX Player


[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-optional-features.html)
Enable optional features for QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-and-deliver.html)
Build and deliver for QNX
# Troubleshooting the QNX Player
This page lists the common problems and limitations that might occur when using the QNX Player.
## The QNX Player fails to enumerate all display resolutions
Due to an ABI breakage in the QNX 7.1 screen system headers, the Player might not be able to query all available display modes. For more information, refer to the [QNX Article - Ref# J2941150](https://www.qnx.com/developers/articles/rel_6934_0.html).
### Solution
The `-nographics commandline` argument in the Player build of the Unity Editor is the root cause of this problem, because it generates sky ambient probe and **reflection probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) that require loading a gfx device, otherwise these probes include uninitialized data. To prevent this from happening, run the Player build without `-nographics`, or generate lighting in the Editor for each **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) included in the build. That is, don’t add lights or generate **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap), and instead generate lighting that will automatically bake the sky probes. When `-nographics` is set, no probes will be rendered.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-optional-features.html)
Enable optional features for QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-and-deliver.html)
Build and deliver for QNX
