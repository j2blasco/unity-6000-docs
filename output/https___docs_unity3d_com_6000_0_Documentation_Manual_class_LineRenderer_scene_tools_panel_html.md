* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer-scene-tools-panel.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lines and trails](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lines-trails-billboards.html)
  * [Rendering lines](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-lines.html)
  * [Line Renderer component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)
  * Line Renderer Scene Tools panel reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)
Line Renderer component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer-line-renderer-properties.html)
Line Renderer properties reference
# Line Renderer Scene Tools panel reference
The properties in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) Tools panel change depending on whether the ****Line Renderer** A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LineRenderer) Scene Editing Mode** is set to **None** , **Edit Points** , or **Create Points**.
To set the current Scene Editing Mode, use the **Edit Points** and **Create Points** buttons.
## Scene Editing Mode: None
By default, there is no Scene Editing Mode set.
**Control** | **Description**  
---|---  
**Simplify Preview** | Enable **Simplify Preview** to see a preview of the results of the simplification operation.  
**Tolerance** | Set the amount by which the simplified line can deviate from the original line.  
  
A value of 0 results in no deviation, and therefore little or no simplification. Higher positive values result in more deviation from the original line, and therefore more simplification.  
  
The default value is 1.  
**Simplify** | Click **Simplify** to reduce the number of elements in the Line Renderer’s **Positions** array.  
  
The simplification operation uses the [Ramer-Douglas-Peucker algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm) to reduce the number of points, based on the **Tolerance** value.  
## Scene Editing Mode: Edit Points
To set the Scene Editing Mode to **Edit Points** , select the **Edit Points** button. Select it again to set the Scene Editing Mode to **None**.
**Control** | **Description**  
---|---  
**Show Wireframe** | When enabled, Unity draws a wireframe in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) that visualizes the line.  
**Subdivide Selected** | This button is enabled when you select two or more adjacent points. Pressing this button inserts a new point between the selected adjacent points.  
## Scene Editing Mode: Create Points
To set the Scene Editing Mode to **Create Points** , select the **Create Points** button. Select it again to set the Scene Editing Mode to **None**.
**Control** | **Description**  
---|---  
**Input** | Set the input method you want to use to create points. The options are: 
  * **Mouse position** : Create points based on the mouse position in the Scene view.
  * **Physics Raycast** : Create points based on a [raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html) into the Scene. Unity creates the point at the position where the raycast hits.

  
****Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask)** | The layer mask to use when performing a raycast. This property is visible only when **Input** is set to **Physics Raycast**.  
**Min Vertex Distance** | When you drag the mouse to create points in the Scene view, the Line Renderer creates a new point when this distance from the last point is exceeded.  
**Offset** | The offset applied to created points. When **Input** is set to **Mouse Position** , Line Renderer applies the offset from the Scene **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). When Input is set to **Physics Raycast** , Line Renderer applies the offset from the raycast normal.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)
Line Renderer component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer-line-renderer-properties.html)
Line Renderer properties reference
