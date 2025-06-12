* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/troubleshoot-mismatched-cell-layouts.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [Tilemaps in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tilemaps-landing.html)
  * [Work with tilemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/work-with-tilemaps-landing.html)
  * Troubleshoot mismatched Cell Layouts


[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
Tilemap Collider 2D component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/tiles-landing.html)
Tiles for tilemaps
# Troubleshoot mismatched Cell Layouts
When you create a **tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Tilemap) in an existing Grid **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), it is possible to try to create a tilemap that uses a different **Cell Layout** to the Grid. If this happens, Unity detects the mismatch in the **Cell Layouts** and a dialog appears. The dialog prompts you to decide if you want to continue creating the child tilemap or stop the action.
Select **Continue** to continue creating the child tilemap, and Unity changes the parent Grid’s **Cell Layout** to match the child’s. Alternately you can select **Cancel** to stop creating the new child tilemap.
**Note:** If you are running the Unity Editor in [headless mode](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorCommandLineArguments.html), this dialog won’t appear and the Editor creates the tilemaps automatically as if you have selected **Continue**.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/work-with-tilemaps/tilemap-collider-2d-reference.html)
Tilemap Collider 2D component reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/tilemaps/tiles-for-tilemaps/tiles-landing.html)
Tiles for tilemaps
