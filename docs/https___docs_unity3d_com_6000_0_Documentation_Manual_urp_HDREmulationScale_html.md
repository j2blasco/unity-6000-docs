* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/HDREmulationScale.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [2D lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-index.html)
  * [Blend Modes in 2D lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-light-blending.html)
  * HDR emulation scale


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/SecondaryTextures.html)
Add normal map and mask textures to a sprite in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DShadows.html)
Create shadows with Shadow Caster 2D in URP
# HDR emulation scale
All Lights in the 2D lighting system support **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR). While a typical RGBA32 color channel has the range of zero to one, a HDR channel can go beyond one.
![Light RGB\(1,1,1\)](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_32.png) | ![HDR Light RGB\(1,1,1\) + Light RGB\(2,2,2\)](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_33.png)  
---|---  
Light RGB(1,1,1) | HDR Light RGB(1,1,1) + Light RGB(2,2,2)  
However, not all platforms natively support HDR textures. HDR Emulation Scale allows those platforms to use HDR lighting by compressing the number of expressible colors in exchange for extra intensity range. Scale describes this extra intensity range. Increasing this value too high may cause undesirable banding to occur.
Light Intensity scale examples:
![HDR Reference](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_34.png) | ![Light Intensity Scale 1 \(No HDR\)](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_35.png)  
---|---  
HDR Reference | Light Intensity Scale 1 (No HDR)  
![Light Intensity Scale 4](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_36.png) | ![Light Intensity Scale 12](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/image_37.png)  
Light Intensity Scale 4 | Light Intensity Scale 12  
When choosing a value for HDR Emulation Scale, the developer should choose the combined maximum brightness for the lights in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) as the value.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/SecondaryTextures.html)
Add normal map and mask textures to a sprite in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2DShadows.html)
Create shadows with Shadow Caster 2D in URP
