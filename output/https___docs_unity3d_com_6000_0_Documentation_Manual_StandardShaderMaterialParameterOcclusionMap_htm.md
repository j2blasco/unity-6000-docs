* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterOcclusionMap.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
  * [Texture maps](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderTextureMaps.html)
  * Occlusion maps


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterHeightMap.html)
Height maps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterEmission.html)
Add light emission to a material
# Occlusion maps
The occlusion map is used to provide information about which areas of the model should receive high or low indirect lighting. Indirect lighting comes from ambient lighting and reflections, so steep concave parts of your model like a crack or a fold would not realistically receive much indirect light.
Occlusion texture maps are normally calculated by 3D applications directly from the 3D model using the modeller or third party software.
An occlusion map is a greyscale image, with white indicating areas that should receive full indirect lighting, and black indicating no indirect lighting. Sometimes this is as simple as a greyscale **heightmap** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap) for simple surfaces.
At other times, generating the correct occlusion texture is slightly more complex. For example, if a character in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) is wearing a hood, the inside edges of the hood should be set to very low indirect lighting, or none at all. In these situations occlusion maps will often be produced by artists using 3D applications to automatically generate an occlusion map based on the model.
![This occlusion map identifies areas on a characters sleeve that are exposed or hidden from ambient lighting. It is used on the model pictured below.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderOcclusionMapTexture.jpg) This occlusion map identifies areas on a character’s sleeve that are exposed or hidden from ambient lighting. It is used on the model pictured below. ![Before and after applying an occlusion map. The areas that are partially obscured, particularly in the folds of fabric around the neck, are lit too brightly on the left. After the ambient occlusion map is assigned, these areas are no longer lit by the green ambient light from the surrounding wooded environment.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderOcclusionMap.jpg) Before and after applying an occlusion map. The areas that are partially obscured, particularly in the folds of fabric around the neck, are lit too brightly on the left. After the ambient occlusion map is assigned, these areas are no longer lit by the green ambient light from the surrounding wooded environment.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterHeightMap.html)
Height maps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterEmission.html)
Add light emission to a material
