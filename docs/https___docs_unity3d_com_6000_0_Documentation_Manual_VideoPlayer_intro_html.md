* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-intro.html

  * [Video and cutscenes](https://docs.unity3d.com/6000.0/Documentation/Manual/Video.html)
  * [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
  * Video Player component targets


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
Video Player
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html)
Video Player component reference
# Video Player component targets
Use the Video Player component to play videos (from a URL or [video clips](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoClip.html)) on various surfaces in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
The Video Player component lets you play video content on different targets, which changes where the video content displays in your scene. To change the video’s target, open the Video Player component and set the **Render Mode** property to your preferred target. 
This page provides details about some of the video targets available:
  * [Camera planes](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-intro.html#camera-planes)
  * [Materials and Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-intro.html#material-texture)
  * [Render Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-intro.html#render-texture)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture)
  * [API Only](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-intro.html#api-only)


For more details of the **Render Mode** property and its options, refer to the [Render mode dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html#render-mode-dropdown). 
For information about all of the Video Player component’s settings, refer to [Video Player component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html). For instructions on how to create the component, refer to [Create a Video Player component](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html).
## The default target of the Video Player
Unity determines the default target when you create the component. If you drop a Video Clip or Video Player component onto a GameObject, the texture of the GameObject’s Renderer becomes the target.
If you drag the Video Clip into the scene, the target is set to the far plane of the scene’s main camera. Otherwise, the VideoPlayer uses the **Render Texture** render mode. 
## Display your video content on a Camera plane
You can choose to project the video onto the near plane or far plane of the [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). To enable this setting, set **Render Mode** to **Camera Near Plane** or **Camera Far Plane**. 
The near plane shows the video in front of any objects in the scene. Displaying the video on this plane is useful for video cutscenes or UI elements that need to overlay the scene. 
The far plane shows the video in the background of the scene, which is ideal for animated backgrounds. 
## Display your video content on a GameObject’s Material and Texture
You can use the Video Player component to attach video files to [GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), and play the video’s content on the GameObject’s [Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html)An image used when rendering a GameObject, Sprite, or UI element. Textures are often applied to the surface of a mesh to give it visual detail. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#texture) at runtime.
When you attach a Video Player component to a GameObject that contains a Renderer component, Unity automatically sets the **Material Property** of the component to the GameObject’s main Texture.
The following screenshot shows a Video Player component attached to a spherical GameObject. The GameObject has a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer component, so the Video Player automatically assigns it to the **Renderer** field, which means the video clip plays on the **Mesh Renderer** A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer)’s Texture.
![A Video Player component attached to a spherical GameObject. The Video Player plays the video clip on the GameObject’s main Texture \(in this case, the Texture of the Mesh Renderer component\).](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Video-1.png) A Video Player component attached to a spherical GameObject. The Video Player plays the video clip on the GameObject’s main Texture (in this case, the Texture of the Mesh Renderer component).
## Display your content on a Render Texture
You can use the Video Player to display video content on a Render Texture. This is useful if you want to project your video onto multiple GameObjects or to apply **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects to the content. For instructions on how to set up and optimize a Render Texture for video, refer to [Set up your Render Texture to display video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-rendertexture.html). 
## Use scripting to set a target (API Only)
When you set **Render Mode** to **API Only** , the Video Player component doesn’t automatically assign a target or draw the video content anywhere. Instead, this mode expects you to handle video rendering manually through C# code. Use scripting to access the video frames via the `VideoPlayer.texture` property. 
This render mode provides the video as a [Render Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html) or [Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html) object, which you can dynamically assign to texture fields in your scene through code. This approach is useful because it eliminates the need to create and manage an intermediate Render Texture manually.
With API Only, you can use video content anywhere the Unity API allows you to assign a texture, such as on Raw Image UI elements, or GameObject materials.
## Additional resources
  * [VideoPlayer API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html)
  * [Video Player](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
  * [Video Player component targets](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-intro.html)
  * [Video Player component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html)
  * [Create a Video Player component](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-instructions.html)
  * [Set up your Render Texture to display video](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer-rendertexture.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VideoPlayer.html)
Video Player
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-VideoPlayer.html)
Video Player component reference
