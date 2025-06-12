* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightingInUnity.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * Introduction to lighting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
Lighting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-configuration-workflow.html)
Lighting configuration workflow
# Introduction to lighting
Lighting in Unity works by approximating how light behaves in the real world. Unity uses detailed models of how light works for a more realistic result, or simplified models for a more stylized result. To set up lighting, choose a **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), configure global lighting, and add elements like lights, emissive surfaces, probes, and volumes.
## Lights
**Lights** are an essential part of every **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). While meshes and textures define the shape and look of a scene, lights define the color and mood of your 3D environment. You’ll likely work with more than one light in each scene. Making them work together requires a little practice but the results can be quite amazing.
![A shader changing the skybox rendering.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StandardShaderChangingSkyboxesEffect.gif) A shader changing the skybox rendering.
Lights can be added to your scene from the **GameObject-andgt;Light** menu. You will choose the light format that you want from the sub-menu that appears. Once a light has been added, you can manipulate it like any other **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject). Additionally, you can add a Light Component to any selected GameObject by using **Component-andgt;Rendering-andgt;Light**.
There are many different options within the Light Component in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
By simply changing the **Color** of a light, you can give a whole different mood to the scene.
![Bright, sunny lights](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightMood1.jpg) Bright, sunny lights ![Dark, medieval lights](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightMood2.jpg) Dark, medieval lights ![Spooky night lights](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LightMood3.jpg) Spooky night lights
## Direct and indirect lighting
Direct light is light that is emitted, hits a surface once, and is then reflected directly into a sensor (for example, the eye’s retina or a camera). Indirect light is all other light that is ultimately reflected into a sensor, including light that hits surfaces several times, and sky light. To achieve realistic lighting results, you need to simulate both direct and indirect light.
Unity can calculate direct lighting, indirect lighting, or both direct and indirect lighting. The lighting techniques that Unity uses depends on how you configure your Project.
## Real-time and baked lighting
Real-time lighting is when Unity calculates lighting at runtime. Baked lighting is when Unity performs lighting calculations in advance and saves the results as lighting data, which is then applied at runtime. In Unity, your Project can use real-time lighting, baked lighting, or a mix of the two (called mixed lighting).
For information on configuring Light components to contribute real-time, baked, or mixed lighting, see [Light Modes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes.html)A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightMode).
## Global illumination
Global illumination is a group of techniques that model both direct and indirect lighting to provide realistic lighting results. Unity has two global illumination systems, which combine direct and indirect lighting.
For more information, refer to [Global illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-a-lighting-setup.html)A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination).
## Rendering paths
Unity supports different **Rendering Paths** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath). These paths affect mainly Lights and Shadows, so choosing the correct rendering path depending on your game requirements can improve your project’s performance. For more info about rendering paths you can visit the [Rendering paths section](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
Lighting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-configuration-workflow.html)
Lighting configuration workflow
