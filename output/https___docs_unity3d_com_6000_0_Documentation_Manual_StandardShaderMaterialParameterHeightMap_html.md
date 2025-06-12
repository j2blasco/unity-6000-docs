* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterHeightMap.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
  * [Texture maps](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderTextureMaps.html)
  * Height maps


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMapImport.html)
Import a normal map
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterOcclusionMap.html)
Occlusion maps
# Height maps
Height mapping (also known as parallax mapping) is a similar concept to normal mapping, however this technique is more complex - and therefore also more performance-expensive. **Heightmaps** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap) are usually used in conjunction with normalmaps, and often they are used to give extra definition to surfaces where the texture maps are responsible for rendering large bumps and protrusions.
While normal mapping modifies the lighting across the surface of the texture, parallax height mapping goes a step further and actually shifts the areas of the visible surface texture around, to achieve a kind of surface-level occlusion effect. This means that apparent bumps will have their near side (facing the camera) expanded and exaggerated, and their far side (facing away from the camera) will be reduced and seem to be occluded from view.
This effect, while it can produce a very convincing representation of 3D geometry, is still limited to the surface of the flat polygons of an object’s **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh). This means that while surface bumps will appear to protrude and occlude each other, the “silhouette” of the model will never be modified, because ultimately the effect is drawn onto the surface of the model and does not modify the actual geometry.
A heightmap should be a greyscale image, with white areas representing the high areas of your texture and black representing the low areas. Here’s a typical albedo map and a heightmap to match.
![An albedo colour map, and a heightmap to match.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderHeightmapTexture.jpg) An albedo colour map, and a heightmap to match. ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderParallaxMap.jpg)
From left to right in the above image: 1. A rocky wall material with albedo assigned, but no normalmap or heightmap. 2. The normal assigned. Lighting is modified on the surface, but rocks do not occlude each other. 3. The final effect with normalmap and heightmap assigned. The rocks appear to protrude out from the surface, and nearer rocks seem to occlude rocks behind them.
Often (but not always) the greyscale image used for a heightmap is also a good image to use for the occlusion map. For information on occlusion maps, see the next section.
* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMapImport.html)
Import a normal map
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterOcclusionMap.html)
Occlusion maps
