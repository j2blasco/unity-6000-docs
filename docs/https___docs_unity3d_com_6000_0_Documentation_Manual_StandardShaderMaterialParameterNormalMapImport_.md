* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMapImport.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-configure-properties.html)
  * [Texture maps](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderTextureMaps.html)
  * [Normal maps](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMapLanding.html)
  * Import a normal map


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)
Introduction to surface normals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterHeightMap.html)
Height maps
# Import a normal map
A **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) can be imported by placing the texture file in your assets folder, as usual. However, you need to tell Unity that this texture is a normal map. You can do this by changing the “Texture Type” setting to “Normal Map” in the import **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) settings.
To import a black and white **heightmap** A greyscale Texture that stores height data for an object. Each pixel stores the height difference perpendicular to the face that pixel represents.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Heightmap) as a normal map, the process is almost identical, except you need to check the “Create from Greyscale” option.
With “Create From Greyscale” selected, a Bumpiness slider will appear in the inspector. You can use this to control how steep the angles in the normalmap are, when being converted from the heights in your heightmap. A low bumpiness value will mean that even sharp contrast in the heightmap will be translated to gentle angles and bumps. A high value will create exaggerated bumps and very high contrast lighting responses to the bumps.
![Low and High Bumpiness settings when importing a height map as a normal map, and the resulting effect on the model.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/BumpMapLowAndHighBumpiness.jpg) Low and High Bumpiness settings when importing a height map as a normal map, and the resulting effect on the model.
Once you have a normalmap in your assets, you can place it into the Normal Map slot of your Material in the inspector. The Standard **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) has a normal map slot, and many of the older legacy shaders also support normal maps.
If you imported a normalmap or heightmap, and did not mark it as a normal map (By selecting **Texture Type: Normal Map** as described above), the Material inspector will warn you about this and offer to fix it, as so:
![The Fix Now warning appears when trying to use a normalmap that has not been marked as such in the inspector.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/BumpMapPutIntoShaderFixNow.png) The “Fix Now” warning appears when trying to use a normalmap that has not been marked as such in the inspector.
Clicking “Fix Now” has the same effect as selecting **Texture Type: Normal Map** in the texture inspector settings. This will work if your texture really is a normal map. However if it is a greyscale heightmap, it will not automatically detect this - so for heightmaps you must always select the “Create from Greyscale” option in the texture’s inspector window.
## Use secondary normal maps
You may also notice that there is a second Normal Map slot further down in the Material inspector for the Standard Shader. This allows you to use an additional normal map for creating extra detail. You can add a normal map into this slot in the same way as the regular normal map slot, but the intention here is that you should use a different scale or frequency of tiling so that the two normal maps together produce a high **level of detail** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#levelofdetail) at different scales. For example, your regular normal map could define the details of panelling on a wall or vehicle, with groves for the panel edges. A secondary normal map could provide very fine bump detail for scratches and wear on the surface which may be tiled at 5 to 10 times the scale of the base normal map. These details could be so fine as to only be visible when examined closely. To have this amount of detail on the base normal map would require the base normal map to be incredibly large, however by combining two at different scales, a high overall level of detail can be achieved with two relatively small normal map textures.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)
Introduction to surface normals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterHeightMap.html)
Height maps
