* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-access.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-writing-shaders.html)
  * Access DOTS Instancing properties in a custom shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-declare.html)
Declare DOTS Instancing properties in a custom shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-best-practice.html)
Best practice for DOTS Instancing shaders in URP
# Access DOTS Instancing properties in a custom shader
To access DOTS Instanced properties, your **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) can use one of the access macros that Unity provides. The access macros assume that instance data in `unity_DOTSInstanceData` uses the following layout:
  * The 31 least significant bits of the metadata value contain the byte address of the first instance in the batch within the `unity_DOTSInstanceData` buffer.
  * If the most significant bit of the metadata value is `0`, every instance uses the value from instance index zero. This means each instance loads directly from the byte address in the metadata value. In this case, the buffer only needs to store a single value, instead of one value per instance.
  * If the most significant bit of the metadata value is `1`, the address should contain an array where you can find the value for instance index `instanceID` using `AddressOfInstance0 + sizeof(PropertyType) * instanceID`. In this case, you should ensure that every rendered instance index has valid data in buffer. Otherwise, out-of-bounds access and undefined behavior can occur.


You can also set the the metadata value directly which is useful if you want to use a custom data source that doesn’t use the above layout, such as a texture.
For an example of how to use these macros, see [Access macro example](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-per-instance.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-declare.html)
Declare DOTS Instancing properties in a custom shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dots-instancing-shaders-best-practice.html)
Best practice for DOTS Instancing shaders in URP
