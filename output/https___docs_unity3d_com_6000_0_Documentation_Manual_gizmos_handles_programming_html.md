* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-handles-programming.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * [The Scene view](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)
  * [Gizmos and handles](https://docs.unity3d.com/6000.0/Documentation/Manual/gizmos-and-handles.html)
  * Programming with gizmos and handles


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html)
Gizmos menu
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewContextMenu.html)
Scene view context menu
# Programming with gizmos and handles
The [`Gizmos`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) and [`Handles`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html) classes allow you to draw lines and shapes in the ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)** view and **Game** view, as well as interactive handles and controls. These two classes together provide a way for you to extend what is shown in these views and build interactive tools to edit your project in any way you like.
For example, rather than entering numbers in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), you could create a draggable circle radius **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) around a non-player character in a game, which represents the area within which they can hear or see the player.
## Gizmos
The `Gizmos` class allows you to draw lines, spheres, cubes, icons, textures and meshes into the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) to use as debugging, set-up aids, or tools while developing your project.
The following example draws a 10 unit yellow wire cube around a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject):
```
using UnityEngine;
public class GizmosExample : MonoBehaviour
{
    void OnDrawGizmosSelected()
    {
        // Draw a yellow cube at the transform position
        Gizmos.color = Color.yellow;
        Gizmos.DrawWireCube(transform.position, new Vector3(10, 10, 10));
    }
}

```

The following image shows how this cube looks when placed on a Directional Light GameObject:
![A light GameObject with an extra script applied which draws a cube gizmo around its position](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ScriptingGizmoExample.png) A light GameObject with an extra script applied which draws a cube gizmo around its position
For a full API reference including usage examples, refer to the API reference page for [`Gizmos`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).
## Handles
Handles are similar to gizmos, but provide more interactivity and manipulation. The default 3D controls that Unity provides to manipulate items in the Scene view are a combination of gizmos and handles. There are a number of built-in handle GUIs, such as the familiar tools to position, scale and rotate an object via the [Transform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html) component.
You can define your own handle GUIs to use with custom component editors. Such GUIs can be a very useful way to edit procedurally-generated Scene content, “invisible” items and groups of related objects, such as waypoints and location markers.
The following example creates an arc area with an arrowhead handle, allowing you to modify a “shield area” in the Scene view:
```
using UnityEditor;
using UnityEngine;
using System.Collections;

//this class should exist somewhere in your project
public class WireArcExample : MonoBehaviour
{
    public float shieldArea;
}

// Create a 180 degrees wire arc with a ScaleValueHandle attached to the disc
// that lets you modify the "shieldArea" value in the WireArcExample
[CustomEditor(typeof(WireArcExample))]
public class DrawWireArc : Editor
{
    void OnSceneGUI()
    {
        Handles.color = Color.red;
        WireArcExample myObj = (WireArcExample)target;
        Handles.DrawWireArc(myObj.transform.position, myObj.transform.up, -myObj.transform.right, 180, myObj.shieldArea);
        myObj.shieldArea = (float)Handles.ScaleValueHandle(myObj.shieldArea, myObj.transform.position + myObj.transform.forward * myObj.shieldArea, myObj.transform.rotation, 1, Handles.ConeHandleCap, 1);
    }
}

```
![An example of an Arc handle and an Scale handle](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ScriptingHandlesExample.png) An example of an Arc handle and an Scale handle
For a full API reference including usage examples, refer to the API reference page for [`Gizmos`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).
## Additional resources
  * [Gizmos Menu](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html)
  * [Programming in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html)
Gizmos menu
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SceneViewContextMenu.html)
Scene view context menu
