* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysExtForceModule.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)
  * [Particle System module component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystemModules.html)
  * External Forces module reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRotBySpeedModule.html)
Rotation by Speed module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysCollisionModule.html)
Collision module reference
# External Forces module reference
This property modifies the effect of **wind zones** A GameObject that adds the effect of wind to your terrain. For instance, Trees within a wind zone will bend in a realistic animated fashion and the wind itself will move in pulses to create natural patterns of movement among the tree. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WindZone.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#windzone) and [Particle System Force Fields](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystemForceField.html) on particles emitted by the system.
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PartSysExtForcesInsp.png) ![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PartSysExtForcesInspList.png)
## Properties
For some properties in this section, you can use different modes to set their value. For information on the modes you can use, refer to [Vary Particle System properties over time](https://docs.unity3d.com/6000.0/Documentation/Manual/varying-particle-system-properties-over-time.html).
**_Property_** | **_Function_**  
---|---  
**Multiplier** | Scale value applied to wind zone forces.  
**Influence Filter** | Choose whether to include Force Fields based on a **Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask), or via an explicit **List**.  
**List** | Define an explicit list of Force Fields that can affect this **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem). This appears when the **Influence Filter** is set to **List**.  
**Influence Mask** | Use a Layer Mask to determine which Force Fields affect this Particle System. This appears when the **Influence Filter** is set to **Layer Mask**.   
This is set to **Everything** by default, but you can enable or disable the following options individually:  
- **Nothing** (automatically unticks all other options, turning them off)  
- **Everything** (automatically ticks all other options, turning them on)  
- **Default**   
- **TransparentFX**   
- **Ignore[Raycast](https://docs.unity3d.com/Packages/com.unity.ugui@latest?subfolder=/manual/Raycasters.html)**  
- **Water**   
- **UI**   
- **[PostProcessing](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)**  
## Additional resources
  * [Particle physics forces](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-physics-forces.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRotBySpeedModule.html)
Rotation by Speed module reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysCollisionModule.html)
Collision module reference
