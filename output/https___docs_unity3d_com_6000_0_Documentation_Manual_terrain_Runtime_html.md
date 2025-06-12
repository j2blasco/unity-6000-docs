* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-Runtime.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Terrain](https://docs.unity3d.com/6000.0/Documentation/Manual/script-Terrain.html)
  * Using Terrain at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)
Terrain Settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TerrainTools.html)
Terrain Tools package
# Using Terrain at runtime
The **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) system uses dedicated Unity engine resources to function correctly. Unity includes these resources in your application at build time when you have at least one Terrain instance in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that’s part of your [build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.md)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile).
If your application only creates Terrain instances at runtime, make sure you include at least one Terrain component as a placeholder in a scene listed by your build profile. Unity detects the placeholder and includes the required resources at build time.
> **Tip:** If you’re not using the placeholder in your application, you can hide it. Either [deactivate](https://docs.unity3d.com/6000.0/Documentation/Manual/DeactivatingGameObjects.md) the GameObject that contains the Terrain component or put this GameObject in a scene that your application doesn’t load.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-OtherSettings.html)
Terrain Settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TerrainTools.html)
Terrain Tools package
