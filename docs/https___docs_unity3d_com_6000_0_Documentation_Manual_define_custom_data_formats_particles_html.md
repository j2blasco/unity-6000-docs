* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/define-custom-data-formats-particles.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp.html)
  * [Particle shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShadersLanding.html)
  * [Custom data streams in Particle Systems in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-data-streams-particle-systems.html)
  * Define custom data formats for particles in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)
Example of Particle System Surface Shader custom vertex streams in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-optimization.html)
Particle System optimization in the Built-In Render Pipeline
# Define custom data formats for particles in the Built-In Render Pipeline
The [Custom Data](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysCustomDataModule.html) module allows you to define custom data formats in the Editor to be attached to particles. You can also set this in a script. See documentation on [Particle System vertex streams](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysVertexStreams.html) for more information on how to set custom data from a script and feed that data into your **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). 
Data can be in the form of a **Vector** , with up to 4 [MinMaxCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html) components, or a **Color** , which is an HDR-enabled [MinMaxGradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html). Use this data to drive custom logic in your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) and Shaders.
The default labels for each curve/gradient can be customized by clicking on them and typing in a contextual name. When passing custom data to shaders, it is useful to know how that data is used inside the shader. For example, a curve may be used for custom alpha testing, or a gradient may be used to add a secondary color to particles. By editing the labels, it is simple to keep a record in the UI of the purpose of each custom data entry.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)
Example of Particle System Surface Shader custom vertex streams in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-optimization.html)
Particle System optimization in the Built-In Render Pipeline
