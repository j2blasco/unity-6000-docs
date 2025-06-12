* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysVertexStreams.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp.html)
  * [Particle shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShadersLanding.html)
  * [Custom data streams in Particle Systems in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-data-streams-particle-systems.html)
  * Particle System custom vertex streams in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-data-streams-particle-systems.html)
Custom data streams in Particle Systems in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
Example of Particle System Standard Shader custom vertex streams in the Built-In Render Pipeline
# Particle System custom vertex streams in the Built-In Render Pipeline
If you are comfortable writing your own **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), you can use the [Renderer Module](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)’s **Custom Vertex Streams** feature to configure your **Particle Systems** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) to pass a wider range of data into your custom Shaders.
There are a number of built-in [data streams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.html) to choose from, such as velocity, size and center position. Aside from the ability to create powerful custom Shaders, these streams allow a number of more general benefits:
  * Use the [Tangent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.Tangent.html) stream to support normal mapped particles.
  * You can remove Color and then add the Tangent [UV2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.UV2.html) and [AnimBlend](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStream.AnimBlend.html) streams to use the Standard Shader on particles.
  * To easily perform linear texture blending of flipbooks, add the UV2 and AnimBlend streams, and attach the Particles/Anim Alpha Blended Shader (see example screenshot below to see how to set this up).


There are also two completely custom per-particle data streams ([ParticleSystemVertexStreams.Custom1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStreams.Custom1.html) and [ParticleSystemVertexStreams.Custom2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemVertexStreams.Custom2.html)), which can be populated from script. Call [SetCustomParticleData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetCustomParticleData.html) and [GetCustomParticleData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetCustomParticleData.html) with your array of data to use them. There are two ways of using this:
  * To drive custom behavior in **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) by attaching your own data to particles; for example, attaching a “health” value to each particle.
  * To pass this data into a Shader by adding one of the two custom streams, in the same way you would send any other stream to your Shader (see [ParticleSystemRenderer.EnableVertexStreams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.EnableVertexStreams.html)). To elaborate on the first example, maybe your custom health attribute could now also drive some kind of visual effect, as well as driving script-based game logic.


When adding vertex streams, Unity will provide you with some information in brackets, next to each item, to help you read the correct data in your shader:
  * Position (POSITION.xyz)
  * Normal (NORMAL.xyz)
  * Color (COLOR.xyzw)
  * UV (TEXCOORD0.xy)
  * UV2 (TEXCOORD0.zw)
  * AnimBlend (TEXCOORD1.x)


Each item in brackets corresponds to a **Vertex Shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader) input, which you should specify in your Shader. Here is the correct input structure for this configuration.
```
            struct appdata_t {
                float4 vertex : POSITION;
                float3 normal : NORMAL;
                fixed4 color : COLOR;
                float4 texcoords : TEXCOORD0;
                float texcoordBlend : TEXCOORD1;
            };

```

Notice that both UV and UV2 are passed in different parts of TEXCOORD0, so we use a single declaration for both. To access each one in your shader, you would use the xy and zw swizzles. This allows you to pack your vertex data efficiently.
## Additional resources
  * [Example of Particle System Standard Shader custom vertex streams](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
  * [Example of Particle System Surface Shader custom vertex streams](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-data-streams-particle-systems.html)
Custom data streams in Particle Systems in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
Example of Particle System Standard Shader custom vertex streams in the Built-In Render Pipeline
