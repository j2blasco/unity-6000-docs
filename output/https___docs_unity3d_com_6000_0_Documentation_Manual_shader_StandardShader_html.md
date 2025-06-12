* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp.html)
  * [Standard Shader in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader-landing.html)
  * Introduction to the Standard Shader in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader-landing.html)
Standard Shader in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMetallicVsSpecular.html)
Choose a metallic or specular shader in the Built-In Render Pipeline
# Introduction to the Standard Shader in the Built-In Render Pipeline
The Unity Standard **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) is a built-in shader with a comprehensive set of features. It can be used to render “real-world” objects such as stone, wood, glass, plastic and metal, and supports a wide range of shader types and combinations. Its features are enabled or disabled by simply using or not using the various texture slots and parameters in the material editor.
The Standard Shader also incorporates an advanced lighting model called **Physically Based Shading**. Physically Based Shading (PBS) simulates the interactions between materials and light in a way that mimics reality. PBS has only recently become possible in real-time graphics. It works at its best in situations where lighting and materials need to exist together intuitively and realistically.
The idea behind our Physically Based Shader is to create a user-friendly way of achieving a consistent, plausible look under different lighting conditions. It models how light behaves in reality, without using multiple ad-hoc models that may or may not work. To do so, it follows principles of physics, including energy conservation (meaning that objects never reflect more light than they receive), Fresnel reflections (all surfaces become more reflective at grazing angles), and how surfaces occlude themselves (what is called Geometry Term), among others.
The Standard Shader is designed with hard surfaces in mind (also known as “architectural materials”), and can deal with most real-world materials like stone, glass, ceramics, brass, silver or rubber. It will even do a decent job with non-hard materials like skin, hair and cloth.
![A scene rendered using the standard shader on all models](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderIntroVikingScene.jpg) A scene rendered using the standard shader on all models
With the Standard Shader, a large range of shader types (such as Diffuse, Specular, Bumped Specular, Reflective) are combined into a single shader intended to be used across all material types. The benefit of this is that the same lighting calculations are used in all areas of your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), which gives a realistic, consistent and believable distribution of light and shade across all models that use the shader.
The Standard Shader lighting math implementation uses the Disney model for diffuse component, [GGX model](https://www.cs.cornell.edu/~srm/publications/EGSR07-btdf.pdf) for specular, with [Smith Joint GGX visibility term](http://jcgt.org/published/0003/02/03/paper.pdf) and [Schlick Fresnel appromixation](https://en.wikipedia.org/wiki/Schlick%27s_approximation).
## Terminology
There are a number of concepts that are very useful when talking about Physically Based Shading in Unity. These include:
  * **Energy conservation** - This is a physics-based concept that ensures objects never reflect more light than they receive. The more specular a material is, the less diffuse it should be; the smoother a surface is, the stronger and smaller the highlight gets.

![The light rendered at each point on a surface is calculated to be the same as the amout of light received from its environment. The microfacets of rough surfaces are affected by light from a wider area. Smoother surfaces give stronger and smaller highlights. Point A reflects light from the source towards the camera. Point B takes on a blue tint from ambient light from the sky. Point C takes its ambient and reflective lighting from the surrounding ground colours.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderEnergyConservation.jpg) The light rendered at each point on a surface is calculated to be the same as the amout of light received from its environment. The microfacets of rough surfaces are affected by light from a wider area. Smoother surfaces give stronger and smaller highlights. Point A reflects light from the source towards the camera. Point B takes on a blue tint from ambient light from the sky. Point C takes its ambient and reflective lighting from the surrounding ground colours.
  * **High Dynamic Range (HDR)** - This refers to colours outside the usual 0–1 range. For instance, the sun can easily be ten times brighter than a blue sky. For an in-depth discussion, see the Unity Manual [HDR](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) page.

![A scene using High Dynamic Range. The sunlight reflecting in the car window appears far brighter than other objects in the scene, because it has been processed using HDR](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/GlowWithHdrAdjusted.jpg) A scene using High Dynamic Range. The sunlight reflecting in the car window appears far brighter than other objects in the scene, because it has been processed using HDR
StandardShader
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader-landing.html)
Standard Shader in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMetallicVsSpecular.html)
Choose a metallic or specular shader in the Built-In Render Pipeline
