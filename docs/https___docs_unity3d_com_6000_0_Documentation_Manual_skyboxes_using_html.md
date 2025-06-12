* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/skyboxes-using.html

  * [World building](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingEnvironments.html)
  * [Sky](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)
  * Create a skybox


[](https://docs.unity3d.com/6000.0/Documentation/Manual/sky.html)
Sky
[](https://docs.unity3d.com/6000.0/Documentation/Manual/skybox-shaders.html)
Configure a skybox with a Skybox Shader
# Create a skybox
To create a new **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) Material:
  1. From the menu bar, click **Assets > Create > Material**.
  2. In the ****Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader)** drop-down, click **Skybox** then the skybox Shader you want to use.
  3. You can now fill out the properties on the Material to set up the skybox. The properties available on the Material depend on the skybox Shader the Material uses.


**Note** : Each skybox Shader has its own set of prerequisite Textures that differ in number and **Texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat). For information on the Textures a particular skybox Shader requires, see the documentation for that skybox Shader. You can find the list of skybox Shaders and their documentation on the [skybox Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/skybox-shaders.html) page.
## Drawing a skybox in your Scene
After you create a skybox Material, you can render it in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). To do this:
  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. In the window that appears, click the **Environment** tab.
  3. Assign the skybox Material to the **Skybox Material** property.


This draws the skybox in the background of every **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) in your Scene. If you instead only want to draw the skybox for a particular Camera, see [Drawing a skybox for a particular Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/skyboxes-using.html#DrawingForCamera).
## Drawing a skybox for a particular Camera
If you only want to draw a skybox in the background of a particular Camera, use the [Skybox component](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html). When you attach this component to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with a Camera, it overrides the skybox that the Camera draws. To attach and set up the Skybox component:
  1. Select a Camera in your Scene and view it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window.
  2. Click **Add Component > Rendering > Skybox**.
  3. On the Skybox component, assign the skybox Material to the **Custom Skybox** property.


## Best Practices
If your Skybox includes a sun, moon, or other light in it, set up a Directional Light that points in the same direction as the light. This makes it appear as though the light in your skybox creates shadows in your Scene. If there are multiple Directional Lights in your Scene, you can choose which Directional Light the Skybox uses. To do this:
  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. Click the **Scene** tab.
  3. Assign the Directional Light you want to use to the **Sun Source** property.


If you want to have fog in your Scene, match the fog color to the color of the skybox. This makes the fog blend to the color of the Scene sky. To do this:
  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. Click the **Environment** tab.
  3. In the **Other Settings** section, enable the **Fog** checkbox.
  4. Set the **Color** property to a color that suits your skybox. For this, you can use the ink dropper tool to select a color from the Scene.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/sky.html)
Sky
[](https://docs.unity3d.com/6000.0/Documentation/Manual/skybox-shaders.html)
Configure a skybox with a Skybox Shader
