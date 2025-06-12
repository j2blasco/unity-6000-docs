* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysLightsModule.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Particle System module component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
  * Lights module reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTexSheetAnimModule.html)
Texture Sheet Animation module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTrailsModule.html)
Trails module reference
# Lights module reference
Add real-time lights to a percentage of your particles using this module.
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html).
Property | Function  
---|---  
**Light** | Assign a [Light](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingInUnity.html) **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) describing how your particle lights should look.  
**Ratio** | A value between 0 and 1 describing the proportion of particles that will receive a light.  
**Random Distribution** | Choose whether lights are assigned randomly or periodically. When set to true, every particle has a random chance of receiving a light based on the Ratio. Higher values increase the probability of a particle having a light. When set to false, the Ratio controls how often a newly created particle receives a light (for example, every Nth particle will receive a light).  
**Use Particle Color** | When set to True, the final color of the Light will be modulated by the color of the particle it is attached to. If set to False, the Light color is used without any modification.  
**Size Affects Range** | When enabled, the **Range** specified in the Light will be multiplied by the size of the particle.  
**Alpha Affects Intensity** | When enabled, the **Intensity** of the light is multiplied by the particle alpha value.  
**Range Multiplier** | Apply a custom multiplier to the Range of the light over the lifetime of the particle using this curve.  
**Intensity Multiplier** | Apply a custom multiplier to the Intensity of the light over the lifetime of the particle using this curve.  
**Maximum Lights** | Use this setting to avoid accidentally creating an enormous number of lights, which could make the Editor unresponsive or make your application run very slowly.  
## Additional resources
  * [Particle lights and trails](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-lights-trails.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTexSheetAnimModule.html)
Texture Sheet Animation module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysTrailsModule.html)
Trails module reference
