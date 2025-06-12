* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterEmission.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
  * [Texture maps](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderTextureMaps.html)
  * Add light emission to a material


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterOcclusionMap.html)
Occlusion maps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterDetail.html)
Secondary Maps (Detail Maps) and Detail Mask
# Add light emission to a material
Adding emission to a Material makes it appear as a visible source of light in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). The Material emission properties control the color and intensity of light that the surface of a Material emits.
Emission is useful when you want some part of a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to appear lit from the inside, such as the screen of a monitor, the disc brakes of a car braking at high speed, or glowing buttons on a control panel. GameObjects that use emissive Materials appear to remain bright even in dark areas of your Scene.
![Red, Green, and Blue spheres using emissive Materials. Even though they are in a dark Scene, they appear to be lit from an internal light source.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderEmissiveFlatColour.jpg) Red, Green, and Blue spheres using emissive Materials. Even though they are in a dark Scene, they appear to be lit from an internal light source.
## Use Emission
You can define basic emissive Materials with a single color and emission level. To make a Material emissive, enable the **Emission** checkbox. This exposes the **Color** and ****Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination)** properties. 
## Examples
![In this image, there are areas of high and low levels of light, and shadows falling across the emissive areas which gives a full representation of how emissive Materials look under varying light conditions.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderEmissiveInLightAndShadow.jpg) In this image, there are areas of high and low levels of light, and shadows falling across the emissive areas which gives a full representation of how emissive Materials look under varying light conditions. ![Baked emissive values from the computer terminals emission map light up the surrounding areas in this dark Scene](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderEmissiveBakedEffect.jpg) Baked emissive values from the computer terminal’s emission map light up the surrounding areas in this dark Scene
## Additional resources
  * [Emit light from a GameObject in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-emissive-materials.html)
  * [Surface Inputs in the Lit shader for the Universal Render Pipeline (URP)](https://docs.unity3d.com/Manual/urp/lit-shader.html#surface-inputs)
  * [Emission inputs in the Lit material for the High Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/lit-material-inspector-reference.html#emission-inputs)
  * [Create and calibrate an illuminated object using HDRP](https://learn.unity.com/tutorial/create-and-calibrate-an-illuminated-object-using-hdrp)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterOcclusionMap.html)
Occlusion maps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterDetail.html)
Secondary Maps (Detail Maps) and Detail Mask
