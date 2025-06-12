* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-skybox.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
  * [Panoramic video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic.html)
  * Set up a panoramic video as a skybox


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-setup.html)
Set up a panoramic video
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-3D.html)
Set up your 3D panoramic video
# Set up a panoramic video as a skybox
Use your panoramic video as the backdrop of your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
This information covers how to create a **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) material and assign it to your default skybox. For more information about how to work with skyboxes, refer to [Create a skybox](https://docs.unity3d.com/6000.0/Documentation/Manual/skyboxes-using.html). 
You can use a panoramic video as a skybox to enhance immersion in various ways. You can use it to create dynamic backgrounds, such as weather systems, day-night cycles, or other visual changes that add depth and realism to the experience.
In **virtual reality** Virtual Reality (VR) immerses users in an artificial 3D world of realistic images and sounds, using a headset and motion tracking. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VirtualReality) (VR), panoramic video skyboxes provide a fully dynamic, 360° environment that users can explore. As the user moves their head, their view of the video’s content shifts, which can make their surroundings feel more realistic.
To use a panoramic video as a skybox, complete the following tasks:
  1. Check the [prerequisites before you continue](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-skybox.html#prerequisites).
  2. [Identify your video content type](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-skybox.html#identify-your-video-content-type).
  3. If your video has a equirectangular layout, [Create a panoramic skybox material for your video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-skybox.html#create-a-panoramic-skybox-material-for-your-video).
  4. If your video has a **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) layout, you have 2 options: 
     * [Create a panoramic skybox material for your video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-skybox.html#create-a-panoramic-skybox-material-for-your-video).
     * [Create a cubemap skybox material for your cubemap video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-skybox.html#create-a-cubemap-skybox-material-for-your-video).
  5. [Assign your skybox material to your skybox](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-skybox.html#assign-your-skybox-material-to-your-skybox).


For more information about how to create a skybox, refer to [Create a skybox](https://docs.unity3d.com/6000.0/Documentation/Manual/skyboxes-using.html).
## Prerequisites
Before you continue to set up a panoramic video as a skybox, you need to set up a panoramic video. For more information, refer to [Set up a panoramic video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-setup.html). 
## Identify your video content type
You need to correctly identify the type of content in the video (cubemap or equirectangular) for the panoramic video to display correctly. To check the type, you can either check the video’s resolution or view the video itself. 
### Check the video’s resolution
You can check the video resolution to confirm what content type the video has using the following steps:
  1. Click on the video.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), click on the video’s name.
  3. Select **Source Info**.
  4. Check the ****Pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel)** value. 
     * Equirectangular videos have 2:1 or 1:1 ratios.
     * Cubemap videos have 1:6, 3:4, 4:3, or 6:1 ratios.


### View the video content
Click on the video to bring up a preview in the Inspector window. If the video looks like a flattened cube, it’s a cubemap. If the video looks more like a flattened sphere, it’s likely equirectangular. 
## Create a panoramic skybox material for your video
If you want your panoramic video with an equirectangular layout to be the backdrop of your Scene, you need to replace the default skybox with your video content. To do this: 
  1. Create a new Material (menu: **Assets** > **Create** > **Material**).
  2. Select the new Material. This opens the Inspector window for the Material.
  3. Set **Shader** to **Skybox** > **Panoramic**.
  4. In the **Texture** slot, assign your **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture).
  5. Set **Mapping** to: 
     * **Latitude Longitude Layout** for equirectangular videos.
     * **6 Frames Layout** for cubemap videos.
  6. For **Image Type** : 
     * Choose **360 Degrees** if the video covers a full 360° view.
     * Choose **180 Degrees** if the video only faces one way.


To check your content looks correct, view the **Preview** at the bottom of the **Material** Inspector.
For more information about the panoramic skybox **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), refer to [Panoramic skybox](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-skybox-panoramic.html).
## Create a cubemap skybox material for your video
The cubemap layout (such as a cross and strip layout) is common for static skybox textures. To set up a skybox material for a cubemap video:
  1. Create a new Material (menu: **Assets** > **Create** > **Material**).
  2. Select the new Material. This opens the Inspector window for the Material.
  3. Set **Shader** to **Skybox** > **Cubemap**.
  4. In the **Texture** slot, assign your render texture.


For more information about the cubemap skybox shader, refer to [Cubemap Skybox Shader Material Inspector Window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-skybox-cubemap.html).
## Assign your skybox material to your skybox
After you create your skybox panoramic or cubemap material, you can assign it to your skybox. 
  1. From the main menu, select **Window** > **Rendering** > **Lighting**.
  2. In the **Lighting** window, select the **Environment** tab.
  3. Drag your skybox material to the **Skybox Material** property.


For more information about how to create a skybox, refer to [Create a skybox](https://docs.unity3d.com/6000.0/Documentation/Manual/skyboxes-using.html). 
## Additional resources
  * [Panoramic Skybox Shader Material Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-skybox-panoramic.html)
  * [Panoramic video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic.html)
  * [Introduction to panoramic videos](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-introduction.html)
  * [Set up a panoramic video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-setup.html)
  * [Set up your 3D panoramic video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-3D.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-setup.html)
Set up a panoramic video
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPanoramic-3D.html)
Set up your 3D panoramic video
