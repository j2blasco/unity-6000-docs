* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/multiple-cameras-birp.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Using multiple cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras-landing.html)
  * Set the order of multiple cameras


[](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras.html)
Configure multiple cameras
[](https://docs.unity3d.com/6000.0/Documentation/Manual/multidisplay.html)
Display camera views on multiple monitors
# Set the order of multiple cameras
You can create multiple Cameras and assign each one to a different depth. Use the following properties in the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window:
  * **Depth** if your project uses the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
  * **Priority** if your project uses the Universal Render Pipeline (URP).


Cameras are drawn from low depth to high depth. In other words, a Camera with a depth of 2 will be drawn on top of a Camera with a depth of 1. You can adjust the values of the **View Rect** property to resize and position the Camera’s view onscreen. This can create multiple mini-views like missile cams, map views, rear-view mirrors, etc.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MultipleCameras.html)
Configure multiple cameras
[](https://docs.unity3d.com/6000.0/Documentation/Manual/multidisplay.html)
Display camera views on multiple monitors
