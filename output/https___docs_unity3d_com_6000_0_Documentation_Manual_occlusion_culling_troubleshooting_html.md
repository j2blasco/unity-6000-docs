* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-troubleshooting.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Excluding hidden objects with occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling-landing.html)
  * Troubleshooting occlusion culling


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CullingGroupAPI-get-culling-results.html)
Get culling results
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicalCameras.html)
Simulating real-world cameras with Physical Cameras
# Troubleshooting occlusion culling
Solve common problems when using occlusion culling, such as incorrect culling and slow processing.
## Hidden objects aren’t being culled
### Symptom
Objects are reported as visible in the occlusion data but are visibly occluded.
### Cause
Culling in Unity operates conservatively. This means that unless the object is explicitly set as invisible, Unity will assume objects are visible.
Occlusion data represents a conservatively simplified version of the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)’s occluders, meaning some of the occlusion erodes and loses detail.
### Resolution
Decrease the value of the **Smallest Occluder** parameter. This will produce higher-resolution data that is less conservative. However, culling will decrease in speed and occlusion data will increase in size.
## Visible objects are being culled
### Symptom
Objects are occluded incorrectly.
### Resolution
  * Decrease the value of the **Smallest Hole** parameter.
  * Set the **Backface Threshold** to 100.
  * Remove the **Static Occluder** flag from **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that you don’t want occluded.


## Slow culling
### Symptom
The culling process is too slow.
### Resolution
Increase the value of the **Smallest Occluder** parameter.
## Slow baking
### Symptom
The baking process is too slow.
### Resolution
Increase the value of the **Smallest Hole** parameter.
## Large occlusion data
### Symptom
The size of the occlusion data is too large.
### Resolution
  * Decrease the value of the **Backface Threshold**.
  * Increase the value of the **Smallest Occluder** parameter.


## Baking fails
### Symptom
Baking fails with the `Failure in split phase` error.
### Cause
The initial step of the bake tries to subdivide the scene into computation tiles. The subdivision is based on the **Smallest Occluder** parameter and when the scene is large in size, too many computation tiles can be created, resulting in an out of memory error.
### Resolution
Increase the value of the **Smallest Occluder** parameter and split up the scene into smaller chunks.
## Additional resources
  * [Occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling)
  * [Occlusion culling window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/occlusion-culling-window.html)
  * [Troubleshooting cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/CameraTroubleshooting.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CullingGroupAPI-get-culling-results.html)
Get culling results
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicalCameras.html)
Simulating real-world cameras with Physical Cameras
