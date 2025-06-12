* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
  * Create a Video Player component


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html)
Video Player component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-rendertexture.html)
Set up your Render Texture to display video
# Create a Video Player component
Create a Video Player component to play videos in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
There are a few ways to create a Video Player component in Unity. Choose from one of the following methods: 
  * [Create a Video Player from the menu or hierarchy](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html#menu)
  * [Add the component to an existing GameObject](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html#existing)
  * [Drag a video clip into the scene](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html#drag)
  * [Use C# scripting to add the component at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html#script)


After you set up your component, you can configure the settings to your liking. For information about the settings, refer to [Video Player component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html).
## Create a Video Player from the menu or hierarchy
To create the Video Player component from the menu, select **GameObject** > **Video** > **Video Player**. 
Alternatively, in the **Hierarchy** , select the **Add (+)** button and then select **Video** > **Video Player**.
Either method creates a new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with a Video Player component attached. 
## Add the component to an existing GameObject
You can also add a Video Player component to an existing GameObject. To do this, either drag a video file onto the GameObject, or:
  1. Click on the GameObject.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, select **Add Component**.
  3. Select **Video** > **Video Player**.


As a result, your GameObject contains a Video Player component. 
## Drag a video clip into the scene
The quickest way to create a Video Player component is to drag your [video clip](https://docs.unity3d.com/6000.0/Documentation/Manual/video-clips-use.html) into the scene: 
  1. Locate the video file in your `Asset` folder in Unity.
  2. Click and drag your file into an empty spot in the Scene Hierarchy, in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView), or in the Inspector.


As a result, Unity creates a GameObject that contains a Video Player component and automatically assigns your video clip to the component. 
## Use C# scripting to add the component at runtime
You can also use scripting to add a VideoPlayer component to a GameObject and configure its settings using C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). Here’s an example code snippet:
```
 // Add a Video Player component to the GameObject.
    VideoPlayer videoPlayer = gameObject.AddComponent<VideoPlayer>();

```

This code dynamically adds a Video Player component to the GameObject that contains this script at runtime.
You can then use the `videoPlayer` variable to access and modify the Video Player’s properties.
## Additional resources
  * [VideoPlayer API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)
  * [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
  * [Video Player component targets](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-intro.html)
  * [Video Player component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html)
  * [Set up your Render Texture to display video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-rendertexture.html)
  * [Create a Video Player component](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html)
  * [Video Clip Importer reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html)
Video Player component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-rendertexture.html)
Set up your Render Texture to display video
