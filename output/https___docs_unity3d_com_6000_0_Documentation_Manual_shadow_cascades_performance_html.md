* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-performance.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)
  * [Real-time shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-realtime.html)
  * [Shadow cascades](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-landing.html)
  * Performance impact of shadow cascades


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-use.html)
Configure shadow cascades
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-implementation-details.html)
Implementation details of shadow cascades
# Performance impact of shadow cascades
Increasing the number of shadow cascades increases the number of draw calls in the shadow rendering pass, which has a negative impact on rendering performance.
Reducing the number of shadow cascades lets you significantly reduce the number of shadow rendering draw calls.
A lower number of shadow cascades might reduce the visual quality of shadows in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Choose the number of cascades based on the performance and visual quality requirements of your project on a scene-by-scene basis.
You can configure different shadow cascade settings and shadow resolution settings for different quality levels using multiple URP Assets.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-use.html)
Configure shadow cascades
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-implementation-details.html)
Implementation details of shadow cascades
