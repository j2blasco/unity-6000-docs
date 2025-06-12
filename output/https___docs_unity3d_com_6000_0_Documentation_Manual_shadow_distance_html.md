* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-distance.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html)
  * [Real-time shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-realtime.html)
  * Set shadow distance in a scene


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-mapping.html)
Shadow mapping
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-landing.html)
Shadow cascades
# Set shadow distance in a scene
Use the **Shadow Distance** property to determine the distance from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) up to which Unity renders real-time shadows.
Shadows from **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) become less noticeable the farther the GameObjects are from the Camera. This is both because the shadows appear smaller on the screen, and because distant GameObjects are usually not the focus of attention. You can take advantage of this effect by disabling real-time shadow rendering for distant GameObjects. This saves on wasted rendering operations, and can improve runtime performance. Additionally, the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) often looks better without distant shadows.
If the current Camera Far Plane is closer than the Shadow Distance, Unity uses the Camera Far Plane instead of the Shadow Distance.
To disguise missing shadows beyond the Shadow Distance, you can use visual effects such as fog.
## Setting the Shadow Distance
In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), set the Shadow Distance property in your Project’s [Quality Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html).
In the Universal Render Pipeline (URP), set the Shadow Distance property in the [Universal Render Pipeline Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html).
In the High Definition Render Pipeline (HDRP), set the Shadow Distance property for each [Volume](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest/index.html?subfolder=/manual/Volumes.html).
## Shadow Distance and Shadowmask Lighting Mode
If your Scene uses the [Shadowmask Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#baked-indirect), Unity renders shadows from [Mixed Lights](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-landing.html)Light components whose Mode property is set to Mixed. Some calculations for Mixed Lights are performed in advance, and some calculations for Mixed Lights are performed at runtime. The behavior of all Mixed Lights in a Scene is determined by the Scene’s Lighting Mode. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MixedLights) beyond the Shadow Distance, using either [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) or a shadow mask Texture. You can configure how Unity renders shadows beyond the Shadow Distance.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-mapping.html)
Shadow mapping
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades-landing.html)
Shadow cascades
