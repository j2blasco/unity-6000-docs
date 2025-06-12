* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-optional-directives.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * [Surface Shader language reference for the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference.html)
  * Surface Shader optional directives reference for the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-required-directives.html)
Surface Shader required directives reference for the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-input-structure.html)
Surface Shader input structure reference for the Built-In Render Pipeline
# Surface Shader optional directives reference for the Built-In Render Pipeline
**Transparency and alpha testing** is controlled by `alpha` and `alphatest` directives. Transparency can typically be of two kinds: traditional alpha blending (used for fading objects out) or more physically plausible “premultiplied blending” (which allows semitransparent surfaces to retain proper specular reflections). Enabling semitransparency makes the generated surface **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code contain [blending](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Blend.html) commands; whereas enabling alpha cutout will do a fragment discard in the generated **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) shader, based on the given variable.
  * `alpha` or `alpha:auto` - Will pick fade-transparency (same as `alpha:fade`) for simple lighting functions, and premultiplied transparency (same as `alpha:premul`) for physically based lighting functions.
  * `alpha:blend` - Enable alpha blending.
  * `alpha:fade` - Enable traditional fade-transparency.
  * `alpha:premul` - Enable premultiplied alpha transparency.
  * `alphatest:VariableName` - Enable alpha cutout transparency. Cutoff value is in a float variable with VariableName. You’ll likely also want to use `addshadow` directive to generate proper shadow caster pass.
  * `keepalpha` - By default opaque **surface shaders** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) write 1.0 (white) into alpha channel, no matter what’s output in the Alpha of output struct or what’s returned by the lighting function. Using this option allows keeping lighting function’s alpha value even for opaque surface shaders.
  * `decal:add` - Additive decal shader (e.g. terrain AddPass). This is meant for objects that lie atop of other surfaces, and use additive blending. See [Surface Shader Examples](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html)
  * `decal:blend` - Semitransparent decal shader. This is meant for objects that lie atop of other surfaces, and use alpha blending. See [Surface Shader Examples](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html)


**Custom modifier functions** can be used to alter or compute incoming vertex data, or to alter final computed fragment color.
  * `vertex:VertexFunction` - Custom vertex modification function. This function is invoked at start of generated **vertex shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader), and can modify or compute per-vertex data. See [Surface Shader Examples](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html).
  * `finalcolor:ColorFunction` - Custom final color modification function. See [Surface Shader Examples](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html).
  * `finalgbuffer:ColorFunction` - Custom deferred path for altering G-buffer content.


**Shadows and Tessellation** - additional directives can be given to control how shadows and tessellation is handled.
  * `addshadow` - Generate a shadow caster pass. Commonly used with custom vertex modification, so that shadow casting also gets any procedural vertex animation. Often shaders don’t need any special shadows handling, as they can just use shadow caster pass from their fallback.
  * `fullforwardshadows` - Support all light shadow types in [Forward](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html) **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath). By default shaders only support shadows from one directional light in **forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) (to save on internal shader variant count). If you need point or Spot Light shadows in forward rendering, use this directive.
  * `tessellate:TessFunction` - use DX11 GPU tessellation; the function computes tessellation factors. See [Surface Shader Tessellation](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderTessellation.html) for details.


**Code generation options** - by default generated surface shader code tries to handle all possible lighting/shadowing/**lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) scenarios. However in some cases you know you won’t need some of them, and it is possible to adjust generated code to skip them. This can result in smaller shaders that are faster to load.
  * `exclude_path:deferred`, `exclude_path:forward` - Do not generate passes for given rendering path ([Deferred Shading](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading), [Forward](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html) respectively).
  * `noshadow` - Disables all shadow receiving support in this shader.
  * `noambient` - Do not apply any ambient lighting or **light probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe).
  * `novertexlights` - Do not apply any light probes or per-vertex lights in Forward rendering.
  * `nolightmap` - Disables all lightmapping support in this shader.
  * `nodynlightmap` - Disables runtime dynamic **global illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) support in this shader.
  * `nodirlightmap` - Disables directional lightmaps support in this shader.
  * `nofog` - Disables all built-in Fog support.
  * `nometa` - Does not generate a “meta” pass (that’s used by lightmapping & dynamic global illumination to extract surface information).
  * `noforwardadd` - Disables [Forward](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html) rendering additive pass. This makes the shader support one full directional light, with all other lights computed per-vertex/SH. Makes shaders smaller as well.
  * `nolppv` - Disables **Light Probe Proxy Volume** A component that allows you to use more lighting information for large dynamic GameObjects that cannot use baked lightmaps (for example, large Particle Systems or skinned Meshes). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeProxyVolume) support in this shader.
  * `noshadowmask` - Disables Shadowmask support for this shader (both [Shadowmask](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadowmask) and Distance Shadowmask).


**Miscellaneous options**
  * `softvegetation` - Makes the surface shader only be rendered when Soft Vegetation is on.
  * `interpolateview` - Compute view direction in the vertex shader and interpolate it; instead of computing it in the pixel shader. This can make the pixel shader faster, but uses up one more texture interpolator.
  * `halfasview` - Pass half-direction vector into the lighting function instead of view-direction. Half-direction will be computed and normalized per vertex. This is faster, but not entirely correct.
  * `approxview` - Removed in Unity 5.0. Use `interpolateview` instead.
  * `dualforward` - Use dual lightmaps in [forward](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html) rendering path.
  * `dithercrossfade` - Makes the surface shader support dithering effects. You can then apply this shader to **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that use an [LOD Group](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup) component configured for cross-fade transition mode.


To see what exactly is different from using different options above, it can be helpful to use “Show Generated Code” button in the [Shader Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-required-directives.html)
Surface Shader required directives reference for the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-input-structure.html)
Surface Shader input structure reference for the Built-In Render Pipeline
