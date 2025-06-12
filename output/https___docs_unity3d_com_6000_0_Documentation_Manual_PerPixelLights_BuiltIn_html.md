* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * Per-pixel and per-vertex lights in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
Lighting in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-emissive-materials.html)
Emit light from a GameObject in the Built-In Render Pipeline
# Per-pixel and per-vertex lights in the Built-In Render Pipeline
If you use the default [Forward rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-paths-introduction.html), Unity sets each realtime Light component as one of the following types:
  * Per-pixel light
  * Per-vertex light
  * Spherical harmonics (SH) per-vertex light


For more information, refer to [Per-pixel and per-vertex lights](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights.html).
The Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) renders each **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) once for each per-pixel light that affects it.
SH lights are fast, and have little or no performance impact. However, SH lights don’t support cookies, **normal maps** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap), or specular highlights. They also have sharp lighting transitions, and might look incorrect.
## How Unity classifies lights
By default, Unity groups lights using the following criteria:
  * The brightest light is always a per-pixel light. This is usually the main Directional Light.
  * The 4 next most important lights are per-vertex lights.
  * The remaining lights are SH lights.


During rendering, Unity finds all lights surrounding a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) and calculates which of those lights affect it most.
For example, in the following image where a sphere GameObject is lit by 8 lights with the same color and intensity, Unity sets the four closest lights (A to D) as per-pixel lights, lights D to G to per-vertex lights, and lights G and H as SH lights. Each per-pixel light creates a separate render pass.
![A sphere GameObject lit by 8 lights](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ForwardLightsExample.png) A sphere GameObject lit by 8 lights ![How Unity classifies the lights](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ForwardLightsClassify.png) How Unity classifies the lights
To help avoid visible light transitions when GameObjects and lights move, Unity blends lights from one mode to another. In the preceding example, Unity blends light D from a per-pixel light to a per-vertex light.
For information about optimizing how Unity classifies lights, refer to [Optimize lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-optimize-builtin.html).
## Additional resources
  * [Per-pixel and per-vertex lights](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
Lighting in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-emissive-materials.html)
Emit light from a GameObject in the Built-In Render Pipeline
