* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterDetail.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
  * [Texture maps](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderTextureMaps.html)
  * Secondary Maps (Detail Maps) and Detail Mask


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterEmission.html)
Add light emission to a material
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
Legacy prebuilt shaders
# Secondary Maps (Detail Maps) and Detail Mask
Secondary Maps (or Detail maps) allow you to overlay a second set of textures on top of the main textures listed above. You can apply a second Albedo colour map, and a second **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap). Typically, these would be mapped on a much smaller scale repeated many times across the object’s surface, compared with the main Albedo and Detail maps.
The reason for this is to allow the material to have sharp detail when viewed up close, while also having a normal **level of detail** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#levelofdetail) when viewed from further away, without having to use a single extremely high texture map to achieve both goals.
Typical uses for detail textures would be:
  * Adding skin detail, such as pores and hairs, to a character’s skin
  * Adding tiny cracks and lichen growth to a brick wall
  * adding small scratches and scuffs to a large metal container

![This character has a skin texture map, but no detail texture yet. We will add skin pores as a detail texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderDetailNotAppliedYet.jpg) This character has a skin texture map, but no detail texture yet. We will add skin pores as a detail texture. ![The Albedo skin pore detail texture](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderDetailSkin.jpg) The Albedo skin pore detail texture ![The normal map for the skin pore detail](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderDetailSkinNormal.jpg) The normal map for the skin pore detail ![The end result, the character now has subtle skin pore detail across her skin, at a much higher resolution than the base Albedo or Normal map layer would have allowed.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderDetailApplied.jpg) The end result, the character now has subtle skin pore detail across her skin, at a much higher resolution than the base Albedo or Normal map layer would have allowed. ![Detail textures can have a subtle but striking effect on the way light hits a surface. This is the same character in a different lighting context.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderDetailDifferentContext.jpg) Detail textures can have a subtle but striking effect on the way light hits a surface. This is the same character in a different lighting context.
If you use a single normal map do ALWAYS plug it into the primary channel. The Secondary normal map channel is more expensive than the primary one but has the exact same effect.
### Detail Mask
The detail mask texture allows you to mask off certain areas of your model to have the detail texture applied. This means you can show the detail texture in certain areas, and hide it in others. In the example of the skin pores above, you might want to create a mask so the pores are not shown on the lips or eyebrows.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterEmission.html)
Add light emission to a material
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
Legacy prebuilt shaders
