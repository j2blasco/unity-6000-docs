* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords-default.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Reducing the size or number of shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reducing.html)
  * [Reducing shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-landing.html)
  * Default shader keywords


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html)
Strip shader variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/avoid-shader-duplication.html)
Troubleshooting shader duplication from AssetBundles
# Default shader keywords
Unity uses predefined sets of **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) keywords to generate shader variants that enable common functionality.
Unity adds the following sets of shader variant keywords at compile time:
  * By default, Unity adds this set of keywords to all graphics shader programs: STEREO_INSTANCING_ON, STEREO_MULTIVIEW_ON, STEREO_CUBEMAP_RENDER_ON, UNITY_SINGLE_PASS_STEREO. You can strip these keywords using an Editor script. For more information, see [Shader variant stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html).
  * By default, Unity adds this set of keywords to the Standard Shader: LIGHTMAP_ON, DIRLIGHTMAP_COMBINED, DYNAMICLIGHTMAP_ON, LIGHTMAP_SHADOW_MIXING, SHADOWS_SHADOWMASK. You can strip these keywords using the [Graphics settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html) window.
  * In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), if your project uses [tier settings](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers-customize.html) that differ from each other, Unity adds this set of keywords to all graphics shaders: UNITY_HARDWARE_TIER1, UNITY_HARDWARE_TIER2, UNITY_HARDWARE_TIER3. For more information, see [Graphics tiers: Graphics tiers and shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html#shader-variants).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html)
Strip shader variants
[](https://docs.unity3d.com/6000.0/Documentation/Manual/avoid-shader-duplication.html)
Troubleshooting shader duplication from AssetBundles
