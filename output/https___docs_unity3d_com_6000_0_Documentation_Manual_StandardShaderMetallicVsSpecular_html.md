* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMetallicVsSpecular.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp.html)
  * [Standard Shader in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader-landing.html)
  * Choose a metallic or specular shader in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html)
Introduction to the Standard Shader in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderChangeProperties.html)
Configuring material properties in the Standard Shader in the Built-In Render Pipeline
# Choose a metallic or specular shader in the Built-In Render Pipeline
When you create a material with the Standard **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) you have the choice of using one of two shaders: **Standard** or **Standard (Specular setup)**. They differ in the data they take as follows:
**Standard** : The shader exposes a “metallic” value that states whether the material is metallic or not. In the case of a metallic material, the Albedo color controls the color of the specular reflection and most light reflects as specular reflections. Non-metallic materials have specular reflections that are the same color as the incoming light and barely reflect when looking at the surface face-on.
**Standard (Specular setup)** : Choose this shader for the classic approach. Use a **specular color** The color of a specular highlight.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#specularcolor) to control the color and strength of specular reflections in the material. This makes it possible to have a specular reflection of a different color than the diffuse reflection.
You can achieve a good representation of most common material types using either method, so for the most part choosing one or the other is a matter of personal preference to suit your art workflow. The following example shows a rubbery plastic material created in both Standard and Standard Specular workflows:
![The fresnel effect visible at grazing angles in relation to the viewer is increasingly apparent as the surface of a material becomes smoother](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderRubberAsMetallicOrSpecular.png) The fresnel effect visible at grazing angles in relation to the viewer is increasingly apparent as the surface of a material becomes smoother
The first image represents the metallic workflow, where you set the metallic to zero (non-metallic). The second setup is nearly identical but you set the specular to nearly black (so you don’t get metallic mirror-like reflections).
In the world of ****Physically Based Shading** An advanced lighting model that simulates the interactions between materials and light in a way that mimics reality. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PhysicallyBasedShading)** you can use references from known real-world materials. For some examples of these references, see our [Material Charts](https://docs.unity3d.com/Manual/StandardShaderMaterialCharts.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html)
Introduction to the Standard Shader in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderChangeProperties.html)
Configuring material properties in the Standard Shader in the Built-In Render Pipeline
