* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html)
  * Set up a camera stack in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/camera-stacking-concepts.html)
Camera stacking in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html)
Add and remove cameras in a camera stack in URP
# Set up a camera stack in URP
This page describes how to use a **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) stack to layer outputs from multiple cameras to the same render target. For more information on camera stacking, refer to [Understand camera stacking](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/camera-stacking-concepts.html).
![A red capsule with a post-processing effect, and a blue capsule with no post-processing](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/camera-stacking-blur-background.png) A red capsule with a post-processing effect, and a blue capsule with no post-processing
Follow these steps to set up a camera stack:
  1. [Create a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html#create-a-camera-stack).
  2. [Set up layers and culling masks](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html#set-up-layers-and-culling-masks).


## Create a camera stack
Create a camera stack with a Base Camera and one or more Overlay Cameras.
For more information on how to do this, refer to [Add a camera to a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html).
## Set up layers and culling masks
Once you create your camera stack, you must assign any **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) the Overlay Cameras need to render to a [layer](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Layer), then set the ****Culling Mask** Allows you to include or omit objects to be rendered by a Camera, by Layer.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#CullingMask)** of each camera to match the layer.
To do this use the following steps:
  1. Add as many layers as your project requires. For information on how to do this, refer to [Add a new layer](https://docs.unity3d.com/6000.0/Documentation/Manual/create-layers.html).
  2. For each GameObject you want an Overlay Camera to render, assign the GameObject to the appropriate layer.
  3. Select the Base Camera of your camera stack and navigate to **Rendering** > **Culling Mask** in the Inspector Window.
  4. Remove any layers you don’t want the Base Camera to render, such as layers that contain objects only an Overlay Camera should render.
  5. Select the first Overlay Camera in the camera stack and navigate to **Rendering** > **Culling Mask** in the Inspector window.
  6. Remove all layers except for the layers that contain GameObjects you want this camera to render.
  7. Repeat Step 5 and Step 6 for each Overlay Camera in the camera stack.


**Note:** You don’t need to configure the **Culling Mask** property of the cameras. However, cameras in URP render all layers by default, so rendering is faster if you remove layers that contain unneeded GameObjects.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/camera-stacking-concepts.html)
Camera stacking in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html)
Add and remove cameras in a camera stack in URP
