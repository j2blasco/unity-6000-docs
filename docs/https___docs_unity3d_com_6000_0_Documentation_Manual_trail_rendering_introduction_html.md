* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/trail-rendering-introduction.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lines and trails](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lines-trails-billboards.html)
  * [Rendering trails](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-trails.html)
  * Rendering trails for moving GameObjects


[](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-trails.html)
Rendering trails
[](https://docs.unity3d.com/6000.0/Documentation/Manual/draw-configure-trail-behind-moving-gameobject.html)
Draw and configure a trail behind a moving GameObject
# Rendering trails for moving GameObjects
The **Trail Renderer** A visual effect that lets you to make trails behind GameObjects in the Scene as they move. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TrailRenderer) component renders a trail of polygons behind a moving **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), over time. This can be used to give an emphasized feeling of motion to a moving object, or to highlight the path or position of moving objects.
The Trail Renderer uses the same algorithm for trail rendering as the [Line Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LineRenderer).
## Distance between trail points
The **Min Vertex Distance** value determines how far in world units the GameObject to which the trail applies must travel before a new segment is added to the trail. Low values like 0.1 create trail segments more often, creating smoother trails. Higher values like 1.5 create segments that are more jagged in appearance. Additionally, wide trails may exhibit visual artifacts when the vertices are very close together and the trail changes direction significantly over a short distance.
For performance reasons, it is best to use the largest possible value that achieves the effect you are trying to create.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-trails.html)
Rendering trails
[](https://docs.unity3d.com/6000.0/Documentation/Manual/draw-configure-trail-behind-moving-gameobject.html)
Draw and configure a trail behind a moving GameObject
