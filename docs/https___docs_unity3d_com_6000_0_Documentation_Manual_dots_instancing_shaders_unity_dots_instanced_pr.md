* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-unity-dots-instanced-prop.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-writing-shaders.html)
  * [DOTS Instancing shader examples in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-samples.html)
  * Example of using UNITY_DOTS_INSTANCED_PROP macros in a DOTS Instancing shader in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-constant.html)
Example of a DOTS Instancing shader that accesses constant data in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-macros.html)
DOTS Instancing shader macros reference for URP
# Example of using UNITY_DOTS_INSTANCED_PROP macros in a DOTS Instancing shader in URP
The `UNITY_DOTS_INSTANCED_PROP` macro has 3 variants: 
  * `UNITY_DOTS_INSTANCED_PROP_OVERRIDE_DISABLED(PropertyType, PropertyName)`
  * `UNITY_DOTS_INSTANCED_PROP_OVERRIDE_SUPPORTED(PropertyType, PropertyName)`
  * `UNITY_DOTS_INSTANCED_PROP_OVERRIDE_REQUIRED(PropertyType, PropertyName)`


These macros allow you to specify if a property can be instanced or not at compile-time. It allows the access macros such as `UNITY_ACCESS_DOTS_INSTANCED_PROP` to expand to more optimal code and can have significant impact on low-end platforms. 
Here is an example of a DOTS Instanced property block using all the macro variants above:
```
UNITY_DOTS_INSTANCING_START(MaterialPropertyMetadata)
    UNITY_DOTS_INSTANCED_PROP_OVERRIDE_SUPPORTED(float4, Color)
    UNITY_DOTS_INSTANCED_PROP_OVERRIDE_DISABLED(float4, SpecColor)
    UNITY_DOTS_INSTANCED_PROP_OVERRIDE_REQUIRED(float4, EmissionColor)
UNITY_DOTS_INSTANCING_END(MaterialPropertyMetadata)

```

  * The `Color` property can either be instanced or not. The correct loading path is selected dynamically depending on the property metadata high-bit.
  * The `SpecColor` property is not instantiable. This declaration won’t add an uint32 field in the constant buffer. It is equivalent to not declaring anything at all. It can be useful to quickly disable instancing on a property without the need to modify other parts of the code.
  * The `EmissionColor` property must be instanced. The property is always loaded from the `unity_DOTSInstanceData` buffer, and no dynamic branch is ever emitted when accessing the property.


By default, `UNITY_DOTS_INSTANCED_PROP` is the same as `UNITY_DOTS_INSTANCED_PROP_OVERRIDE_SUPPORTED`. This default behavior can be changed by uncommenting the define `UNITY_DOTS_INSTANCED_PROP_OVERRIDE_DISABLED_BY_DEFAULT` in “com.unity.render-pipelines.core\ShaderLibrary\UnityDOTSInstancing.hlsl”. When you do this, the define is enabled, and `UNITY_DOTS_INSTANCED_PROP` becomes the same as `UNITY_DOTS_INSTANCED_PROP_OVERRIDE_DISABLED`.
**Note** : When uncommenting the define `UNITY_DOTS_INSTANCED_PROP_OVERRIDE_DISABLED_BY_DEFAULT`, you might need to clear the Library folder to make sure the **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) are correctly recompiled.
On low-end devices, instanced properties can have a significant performance cost. Loading from an SSBO for example, can be a lot slower than a normal constant buffer load. This is because on many low-end devices, this type of buffer load goes through texture samplers, whereas constant buffer loads uses faster hardware unless a dynamic index is used to access the buffer. Instanced properties are always loaded with dynamic indexing since it depends on the property metadata, this means they always go through the texture samplers on low-end devices. To better optimize your project for low-end devices, you can disable property instancing by default. To do this, enable the define `UNITY_DOTS_INSTANCED_PROP_OVERRIDE_DISABLED_BY_DEFAULT`, this sets property instancing to be disabled as default. Once this is done, you can then enable property instancing manually only for the properties that require it.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-constant.html)
Example of a DOTS Instancing shader that accesses constant data in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-macros.html)
DOTS Instancing shader macros reference for URP
