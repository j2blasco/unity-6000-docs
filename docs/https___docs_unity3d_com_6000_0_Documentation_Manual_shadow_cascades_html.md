* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)
  * [Real-time shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-realtime.html)
  * [Shadow cascades](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-landing.html)
  * Introduction to shadow cascades


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-landing.html)
Shadow cascades
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-use.html)
Configure shadow cascades
# Introduction to shadow cascades
Shadow cascades let you improve the visual fidelity of shadows without increasing the shadow map resolution.
For example, the following illustration shows shadow rendering with different numbers of shadow cascades. The shadow resolution is 2048 in all cases.
![Shadow rendering with different cascade numbers. A: 1 cascade, B: 2 cascades, C: 3 cascades, D: 4 cascades](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shadows/shadow-cascades-comparison.png)  
Shadow rendering with different cascade numbers. A: 1 (no cascades), B: 2 cascades, C: 3 cascades, D: 4 cascades.
Shadow cascades only work with directional lights.
From a technical perspective, shadow cascades mitigate a problem called [perspective aliasing](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-implementation-details.html#perspective-aliasing), where real-time shadows from [directional lights](https://docs.unity3d.com/6000.0/Documentation/Manual/Lighting.html) appear pixelated when they are near the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera).
## Additional resources
  * [Configure shadow cascades](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-use.html)
  * [Performance impact of shadow cascades](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades.html)
  * [Technical implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-implementation-details.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-landing.html)
Shadow cascades
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-use.html)
Configure shadow cascades
