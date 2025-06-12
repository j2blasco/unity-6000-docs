* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Light sources](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
  * [Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components.html)
  * Per-pixel and per-vertex lights


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lighting.html)
Types of Light component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingLights.html)
Place Light components
# Per-pixel and per-vertex lights
If you use the default [Forward rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-paths-introduction.html#forward), each realtime Light component can be one of the following types:
  * A per-pixel light, which lights each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) of an object accurately.
  * A per-vertex light, which lights each vertex of an object accurately. Unity interpolates lighting for the pixels between vertices.


Per-pixel lights give more accurate results but reduce performance.
The Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) also sets some lights as Spherical Harmonic (SH) per-vertex lights, which are the least accurate but render the fastest.
For more information, refer to the following:
  * [Light limits in the Universal Render Pipeline (URP)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/light-limits-in-urp.html)
  * [Per-pixel and per-vertex lights in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html)


## Additional resources
  * [Choose a lighting setup](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-a-lighting-setup.html)
  * [Introduction to rendering paths](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-paths-introduction.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lighting.html)
Types of Light component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingLights.html)
Place Light components
