* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/set-up-a-volume.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](https://docs.unity3d.com/6000.0/Documentation/Manual/post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-in-urp.html)
  * [Volumes in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/volumes-landing-page.html)
  * Set up a volume in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volumes.html)
Understand volumes in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html)
Create a Volume Profile in URP
# Set up a volume in URP
To set up a volume in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), you can configure the project’s default volume settings, or add a new custom volume. For details, refer to the following sections:
  * [Configure the default volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/set-up-a-volume.html#configure-the-default-volumes)
  * [Add a volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/set-up-a-volume.html#add-a-volume).


## Configure the default volumes
You can configure the default global volumes that all URP scenes use.
### Configure the Default Volume
To configure the Default Volume, go to **Project Settings** > **Graphics** > **URP** > **Default Volume Profile**. 
By default, the Default Volume references a Volume Profile called `DefaultVolumeProfile`. `DefaultVolumeProfile` lists all possible Volume Overrides. You can change the properties, but you can’t disable or remove Volume Overrides. Refer to [Volume Overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html) for more information about changing the properties.
You can assign your own Volume Profile.
If you delete the Volume Profile, URP automatically reassigns `DefaultVolumeProfile`.
### Configure the global volume for a quality level
To configure the global volume for a quality level, follow these steps:
  1. Go to **Project Settings** > **Quality** and select the quality level.
  2. Go to **Rendering** > **Render Pipeline Asset** and open the URP Asset.
  3. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window for the URP Asset, go to **Volumes**.


You can add or remove Volume Overrides and edit their properties. Refer to [Volume Overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html) for more information about changing the Volume Overrides and properties.
## Add a volume
To add a volume to your scene and edit its Volume Profile, follow these steps:
  1. Go to **GameObject** > **Volume** and select a GameObject.
  2. In the **Scene** or **Hierarchy** view, select the new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to view it in the Inspector.
  3. In the **Volume** component, assign a Volume Profile asset. To create a new Volume Profile, select **New**.


The list of Volume Overrides that the Volume Profile contains appears below the Volume Profile asset. You can add or remove Volume Overrides and edit their properties. Refer to [Volume Overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html) for more information about changing the Volume Overrides and properties.
### Example: Create a local post-processing effect
The following example shows how to use a local Box Volume to implement a location-based **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effect.
  1. In a scene, create a new Box Volume using **GameObject** > **Volume** > **Box Volume**.
  2. Select the Box Volume. In the Inspector, in the **Volume** component, select **New**.
Unity creates the new Volume Profile.
  3. Select **Add Override** , then select a post-processing effect.
  4. In the **Box**Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collider)** component, adjust the **Size** and **Center** properties so the collider occupies the volume where you want the local post-processing effect to be.
  5. Ensure **Is Trigger** is enabled in the ****Box Collider** A cube-shaped collider component that handles collisions for GameObjects like dice and ice cubes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BoxCollider.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#boxcollider)** component.
  6. If you have other Volume components in the scene, change the value of the **Priority** property to ensure that the Volume Overrides from this volume have higher priority than those of other volumes.


Now, when the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is within the bounds of the GameObject’s collider, URP uses the Volume Overrides from the **Volume** component.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volumes.html)
Understand volumes in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html)
Create a Volume Profile in URP
