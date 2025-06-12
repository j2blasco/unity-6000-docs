* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-a-render-texture.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html)
  * Render a camera's output to a Render Texture in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
Apply different post processing effects to separate cameras in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/User-Render-Requests.html)
Create a render request in URP
# Render a camera’s output to a Render Texture in URP
In the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) can render to the screen or to a [Render Texture](https://docs.unity3d.com/Manual/class-RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture). Rendering to a screen is the default and is the most common use case, but rendering to a Render Texture allows you to create effects such as CCTV camera monitors.
If you have a Camera that is rendering to a Render Texture, you must have a second Camera that then renders that Render Texture to the screen. In URP, all Cameras that render to Render Textures perform their render loops before all Cameras that render to the screen. This ensures that the Render Textures are ready to render to the screen. For more information on Camera rendering order in URP, refer to [Rendering order and overdraw](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-advanced.html).
## Render to a Render Texture that renders to the screen
  1. Create a Render Texture Asset in your project. To do this select **Assets** > **Create** > **Rendering** > **Render Texture**.
  2. Create a **Quad** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad) game object in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  3. Create a material in your Project.
  4. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), drag the Render Texture to the material’s **Base Map** field.
  5. In the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView), drag the material on to the quad.
  6. Create a camera in your scene.
  7. Select the Base Camera and in the Inspector, drag the Render Texture on to the **Output Texture** property.
  8. Create another camera in your scene.
  9. Place the quad within the view of the new Base Camera.


The first Camera now renders its view to the Render Texture. The second Camera renders the scene including the Render Texture to the screen.
You can set the output target for a camera in a script by setting the `targetTexture` property of the camera:
```
myCamera.targetTexture = myRenderTexture;

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
Apply different post processing effects to separate cameras in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/User-Render-Requests.html)
Create a render request in URP
