* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-hierarchy.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Profile rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
  * [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-landing.html)
  * Check or find a rendering event


[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-debug.html)
Debug a frame
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-attach.html)
Attach the Frame Debugger to a built project
# Check or find a rendering event
The Event Hierarchy panel in the [Frame Debugger window](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window.html) displays the sequence of rendering events that constitute the frame. The panel organizes the events into a hierarchy so you can see where each event originates from.
![The Event Hierarchy for the URP template scene.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/frame-debugger-event-hierarchy.png) The Event Hierarchy for the URP template scene.
To view information about an event, select the event in the Event Hierarchy. When you select an event:
  * The Frame Debugger displays information about the event in the [event information](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-debugger-window-event-information.html) panel.
  * Unity processes events up to and including the selected event and displays the result in the Game view.
  * If there is a single **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) associated with the event, you can double click or CTRL + click the event to highlight the GameObject in the [Hierarchy](https://docs.unity3d.com/6000.0/Documentation/Manual/Hierarchy.html). If the event represents a batch that contains multiple GameObjects, Unity doesn’t highlight the GameObjects.


For more information, see [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger.html).
## Hierarchy search bar
The search bar at the top of the Event Hierarchy can filter events by name. Use it to quickly find specific events by name.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-debug.html)
Debug a frame
[](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger-attach.html)
Attach the Frame Debugger to a built project
