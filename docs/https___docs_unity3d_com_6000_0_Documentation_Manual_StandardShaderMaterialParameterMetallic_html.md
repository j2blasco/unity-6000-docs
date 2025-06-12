* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterMetallic.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp.html)
  * [Standard Shader in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader-landing.html)
  * [Configuring material properties in the Standard Shader in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderChangeProperties.html)
  * Configure reflections with the Standard Shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterAlbedoColor.html)
Set the color of a material in the Standard Shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderFresnel.html)
Configure edge reflections (Fresnel effect)
# Configure reflections with the Standard Shader
When working in the **Metallic workflow** (as opposed to the Specular workflow), the reflectivity and light response of the surface are modified by the **Metallic** level and the [Smoothness](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterSmoothness.html) level.
Specular reflections are still generated when using this workflow but they arise naturally depending on the settings you give for the **Metallic** and Smoothness levels, rather than being explicitly defined.
**Metallic mode is not just for materials which are supposed to look metallic!** This mode is known as **Metallic** because of the way you have control over how metallic or non-metallic a surface is.
### Metallic Property
The **Metallic** Property of a material determines how “metal-like” the surface is. When a surface is more metallic, it reflects the environment more and its albedo colour becomes less visible. At full metallic level, the surface colour is entirely driven by reflections from the environment. When a surface is less metallic, its albedo colour is more clear and any surface reflections are visible on top of the surface colour, rather than obscuring it.
![A range of Metallic values from 0 to 1 \(with smoothness at a constant 0.8 for all samples\)](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderMetallicGraduationTable.jpg) A range of Metallic values from 0 to 1 (with smoothness at a constant 0.8 for all samples)
By default, with no texture assigned, the **Metallic** and Smoothness Properties are controlled by a slider each. This is enough for some materials. However if your model’s surface has areas with a mixture of surface types in the albedo texture, you can use a texture map to control how the metallic and smoothness levels vary across the surface of the material. For instance if your texture contains a character’s clothing including some metal buckles and zips. You would want the buckles and zips to have a higher **Metallic** value than the fabric of the clothes. To achieve this, instead of using a single slider value, a texture map can be assigned which contains lighter **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) colours in the areas of the buckles and zips, and darker values for the fabric.
With a texture assigned to the **Metallic** Property, both the **Metallic** and **Smoothness** sliders disappear. Instead, the **Metallic** levels for the material are controlled by the values in the Red channel of the texture, and the [Smoothness](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterSmoothness.html) levels for the material are controlled by the Alpha channel of the texture. (This means the Green and Blue channels are ignored). This means you have a single texture which can define areas as being rough or smooth, and metallic or non-metallic, which is very useful when working texture maps that cover many areas of a model with varying requirements - for example a single character texture map often includes multiple surface requirements - leather shoes, cloth clothes, skin for the hands and face and metal buckles.
![A spaceship model with no metallic map.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderNoMetallicMap.jpg) A spaceship model with no metallic map.
In the example above, the spaceship has an albedo map, but no texture for **Metallic**. This means the whole object has a single **Metallic** and **Smoothness** value, which is not ideal.
![A spaceship model with a metallic map applied.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderMetallicMap.jpg) A spaceship model with a metallic map applied.
In this example, a **Metallic** /**Smoothness** texture map has been assigned. Part of the spaceship now has a high **Metallic** value and responds to light accordingly.
![The metallic map this part of the spaceship model uses. The lighter areas are metal, and the mid to low greys are non-metal.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderMetallicMap_map.png) The metallic map this part of the spaceship model uses. The lighter areas are metal, and the mid to low greys are non-metal.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterAlbedoColor.html)
Set the color of a material in the Standard Shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderFresnel.html)
Configure edge reflections (Fresnel effect)
