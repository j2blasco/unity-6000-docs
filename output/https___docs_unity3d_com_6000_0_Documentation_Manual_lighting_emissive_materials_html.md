* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-emissive-materials.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * Emit light from a GameObject in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html)
Per-pixel and per-vertex lights in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-cookies-built-in-render-pipeline.html)
Create cookies in the Built-In Render Pipeline
# Emit light from a GameObject in the Built-In Render Pipeline
![A scene with a glowing Unity logo on a wall illuminating a dark room.](https://docs.unity3d.com/6000.0/Documentation/uploads/GlobalIllumination/EmissiveMaterial.png) A scene with a glowing Unity logo on a wall illuminating a dark room.
Like area lights, emissive materials emit light across their surface area. They contribute to bounced light in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and associated properties such as color and intensity can be changed during gameplay. Whilst area lights are not supported by **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination), similar soft lighting effects in real-time are still possible using emissive materials.
‘Emission’ is a property of the Standard **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) which allows static objects in our scene to emit light. By default the value of ‘Emission’ is set to zero. This means no light will be emitted by objects assigned materials using the Standard Shader. 
There is no range value for emissive materials but light emitted will again falloff at a quadratic rate. Emission will only be received by objects marked as ‘Static’ or “**Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) Static’ from the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector). Similarly, emissive materials applied to non-static, or dynamic geometry such as characters will not contribute to scene lighting.
However, materials with an emission above zero will still appear to glow brightly on-screen even if they are not contributing to scene lighting. This effect can also be produced by selecting ‘None’ from the Standard Shader’s ‘Global Illumination’ Inspector property. Self-illuminating materials like these are a useful way to create effects such as neons or other visible light sources.
Emissive materials only directly affect static geometry in your scene. If you need dynamic, or non-static geometry - such as characters, to pick up light from emissive materials, **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) must be used.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html)
Per-pixel and per-vertex lights in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-cookies-built-in-render-pipeline.html)
Create cookies in the Built-In Render Pipeline
