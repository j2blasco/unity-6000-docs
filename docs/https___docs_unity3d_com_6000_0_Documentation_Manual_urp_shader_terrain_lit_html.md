* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shader-terrain-lit.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Shader Material Inspector window reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-reference.html)
  * Terrain Lit Shader Material Inspector window reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/unlit-shader.html)
Unlit Shader Material Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/particles-lit-shader.html)
Particles Lit Shader Material Inspector window reference for URP
# Terrain Lit Shader Material Inspector window reference for URP
URP uses the **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) Lit **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) for Unity Terrain. This shader is a simpler version of the [Lit shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lit-shader.html). A Terrain can use a Terrain Lit Material with up to eight [Terrain Layers](https://docs.unity3d.com/Manual/class-TerrainLayer.html).
![A Terrain GameObject rendered with the Terrain Lit shader.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/terrain/terrain-rendered-with-terrain-lit.png)  
_A Terrain GameObject rendered with the Terrain Lit shader._
## Properties
**Property** | **Description**  
---|---  
**Enable Height-based Blend** | Enable to have Unity take the height values from the blue channel of the **Mask Map** Texture.  
  
If you do not enable this property, Unity blends the Terrain Layers based on the weights painted in the splatmap Textures. When you disable this property and the Terrain Lit Shader Material is assigned to a Terrain, URP adds an additional option **Opacity as Density Blend** for each Terrain Layer that is added to that Terrain in the Paint Texture Tool Inspector.  
  
**Note** : Unity ignores this option when more than four Terrain Layers are on the Terrain.  
 _Height Transition_ | Select the size in world units of the smooth transition area between Terrain Layers.  
**Enable Per-pixel Normal** | Enable to have Unity sample the normal map Texture on a per-pixel level, preserving more geometry details for distant terrain parts. Unity generates a geometry normal map at runtime from the heightmap, rather than the Mesh geometry. This means you can have high-resolution Mesh normals, even if your Mesh is low resolution.  
  
**Note** : This option only works if you enable **Draw Instanced** on the Terrain.  
## Using the Paint Holes Tool
To use the **Paint Holes** tool on a Terrain, ensure that the **Terrain Holes** check box in your project’s URP Asset is checked. Otherwise, the Terrain holes are absent when you build the application.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/unlit-shader.html)
Unlit Shader Material Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/particles-lit-shader.html)
Particles Lit Shader Material Inspector window reference for URP
