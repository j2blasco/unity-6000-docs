* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-macros.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-writing-shaders.html)
  * DOTS Instancing shader macros reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-unity-dots-instanced-prop.html)
Example of using UNITY_DOTS_INSTANCED_PROP macros in a DOTS Instancing shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-functions.html)
DOTS Instancing shader functions reference for URP
# DOTS Instancing shader macros reference for URP
Unity provides the following access macros:
**Access macro** | **Description**  
---|---  
`UNITY_ACCESS_DOTS_INSTANCED_PROP(PropertyType, PropertyName)` | Returns the value loaded from `unity_DOTSInstanceData`. Refer to [Declare DOTS Instancing properties in a custom shader](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-declare.html) for more information. **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that Unity provides use this version for DOTS Instanced built-in properties that don’t have a default value to fall back on.  
`UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_DEFAULT(PropertyType, PropertyName)` | Returns the same as `UNITY_ACCESS_DOTS_INSTANCED_PROP`, except if the most significant bit of the metadata value is zero, it returns a default value. The default value is the value of the regular material property with the same name as the DOTS Instanced property, which is why Shaders that Unity provides use the convention where DOTS Instanced properties have the same name as regular material properties. When using the default value, the access macro doesn’t access `unity_DOTSInstanceData` at all. Shaders that Unity provides use this access macro for DOTS Instanced material properties, so the loads fall back to the value set on the material.  
`UNITY_ACCESS_DOTS_INSTANCED_PROP_WITH_CUSTOM_DEFAULT(PropertyType, PropertyName, DefaultValue)` | Returns the same as `UNITY_ACCESS_DOTS_INSTANCED_PROP` unless the most significant bit of the metadata value is zero, in which case this macroreturns `DefaultValue` instead, and doesn’t access `unity_DOTSInstanceData`.  
`UNITY_DOTS_INSTANCED_METADATA_NAME(PropertyType, PropertyName)` | Returns the metadata value directly without accessing anything. This is useful for custom instance data loading schemes.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-unity-dots-instanced-prop.html)
Example of using UNITY_DOTS_INSTANCED_PROP macros in a DOTS Instancing shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-functions.html)
DOTS Instancing shader functions reference for URP
