* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterSpecular.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp.html)
  * [Standard Shader in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader-landing.html)
  * [Configuring material properties in the Standard Shader in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderChangeProperties.html)
  * Configure specular reflections in the Standard Shader 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderFresnel.html)
Configure edge reflections (Fresnel effect)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterSmoothness.html)
Configure smoothness with the Standard Shader
# Configure specular reflections in the Standard Shader
The **Specular** Property is only visible when using the **Specular setup**
Specular effects are essentially the direct reflections of light sources in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), which typically show up as bright highlights and shine on the surface of objects (although specular highlights can be subtle or diffuse too).
Both the **Specular setup** and **Metallic setup** produce specular highlights, so the choice of which to use is more a matter of setup and your artistic preference. In the **Specular setup** you have direct control over the brightness and tint colour of specular highlights, while in the **Metallic setup** you control other Properties and the intensity and colour of the specular highlights emerge as a natural result of the other Property settings.
When working in Specular mode, the RGB colour in the **Specular** Property controls the strength and colour tint of the specular reflectivity. This includes shine from light sources and reflections from the environment. The [Smoothness](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterSmoothness.html) Property controls the clarity of the specular effect. With a low **Smoothness** value, even strong specular reflections appear blurred and diffuse. With a high **Smoothness** value, specular reflections are crisper and clearer.
![The Specular Smoothness values from 0 to 1](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderReflectivityGraduationTable.svg) The Specular Smoothness values from 0 to 1
You might want to vary the **Specular** values across the surface of your material - for example, if your Texture contains a character’s coat that has some shiny buttons. You would want the buttons to have a higher specular value than the fabric of the clothes. To achieve this, assign a Texture map instead of using a single slider value. This allows greater control over the the strength and colour of the specular light reflections across the surface of the material, according to the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) colours of your specular map.
When a Texture is assigned to the **Specular** Property, both the **Specular** Property and **Smoothness** slider disappear. Instead, the specular levels for the material are controlled by the values in the **Red** , **Green** and **Blue** channels of the Texture itself, and the [Smoothness](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterSmoothness.html) levels for the material are controlled by the Alpha channel of the same Texture. This provides a single Texture which defines areas as being rough or smooth, and have varying levels and colors of specularity. This is very useful when working Texture maps that cover many areas of a model with varying requirements; for example, a single character Texture map often includes multiple surface requirements such as leather shoes, fabric of the clothes, skin for the hands and face, and metal buckles.
![An example of a 1000kg weight with a strong specular reflection from a directional light.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderSpecularCol1000kgWeight.jpg) An example of a 1000kg weight with a strong specular reflection from a directional light.
Here, the specular reflection and smoothness are defined by a colour and the **Smoothness** slider. No Texture has been assigned, so the specular and smoothness level is constant across the whole surface. This is not always desirable, particularly in the case where your Albedo Texture maps to a variety of different areas on your model (also known as a Texture atlas).
![The same model, but with a specular map assigned, instead of using a constant value.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderSpecularMap1000kgWeight.jpg) The same model, but with a specular map assigned, instead of using a constant value.
Here, a Texture map controls the specularity and smoothness. This allows the specularity to vary across the surface of the model. Notice the edges have a higher specular effect than the centre, there are some subtle colour responses to the light, and the area inside the lettering no longer has specular highlights. Pictured to the right are the RGB channels controlling the specular colour and strength, and the Alpha channel controlling the smoothness.
**Note** : A black **specular color** The color of a specular highlight.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#specularcolor) (0,0,0) results in nulling out the specular effect.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderFresnel.html)
Configure edge reflections (Fresnel effect)
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterSmoothness.html)
Configure smoothness with the Standard Shader
