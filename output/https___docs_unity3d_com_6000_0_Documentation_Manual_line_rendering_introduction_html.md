* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/line-rendering-introduction.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lines and trails](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lines-trails-billboards.html)
  * [Rendering lines](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-lines.html)
  * Rendering lines


[](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-lines.html)
Rendering lines
[](https://docs.unity3d.com/6000.0/Documentation/Manual/draw-configure-line-3d-space.html)
Draw and configure a line in 3D space
# Rendering lines
The ****Line Renderer** A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LineRenderer)** component takes an array of two or more points in 3D space, and draws a straight line between each one. You can use a Line Renderer to draw anything from a simple straight line to a complex spiral.
The line is always continuous; if you need to draw two or more completely separate lines, you should use multiple **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), each with its own Line Renderer.
The Line Renderer does not render lines that have a width in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel). It renders polygons that have a width in world units. The Line Renderer uses the same algorithm for line rendering as the [Trail Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)A visual effect that lets you to make trails behind GameObjects in the Scene as they move. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TrailRenderer).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-lines.html)
Rendering lines
[](https://docs.unity3d.com/6000.0/Documentation/Manual/draw-configure-line-3d-space.html)
Draw and configure a line in 3D space
