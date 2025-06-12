* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/editor-CustomEditors.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [IMGUI (Immediate Mode GUI)](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html)
  * [Extending the Editor with IMGUI](https://docs.unity3d.com/6000.0/Documentation/Manual/ExtendingTheEditor.html)
  * Create custom Editors with IMGUI


[](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-PropertyDrawers.html)
Use Property Drawers with IMGUI to customize the Inspector
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TreeViewAPI.html)
Create TreeView with IMGUI
# Create custom Editors with IMGUI
**Note** : It’s strongly recommended to use the [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html) to extend the [Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-support-for-editor-ui.html), as it provides a more modern, flexible, and scalable solution than IMGUI.
To speed up application development, create custom editors for components you commonly use. This page shows you how to create a simple script to make **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) always look at a point.
  1. Create a C# script and name it “LookAtPoint”.
  2. Open the script and replace its contents with the code below.
  3. Attach the script to a GameObject in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).

```
using UnityEngine;
public class LookAtPoint : MonoBehaviour
{
    public Vector3 lookAtPoint = Vector3.zero;

    void Update()
    {
        transform.LookAt(lookAtPoint);
    }
}

```

When you enter Play mode, the GameObject that you attached the script to now orientates itself towards the coordinates you set to the “Look At Point” property. When writing Editor **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), it’s often useful to make certain scripts execute during **Edit mode** , while your application is not running. To do this, add the `ExecuteInEditMode` attribute to the class, like this:
```
using UnityEngine;
[ExecuteInEditMode]
public class LookAtPoint : MonoBehaviour
{
    public Vector3 lookAtPoint = Vector3.zero;

    void Update()
    {
        transform.LookAt(lookAtPoint);
    }
}

```

Now if you move the GameObject in the Editor, or change the values of “Look At Point” in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), the GameObject updates its rotation so that it looks at the target point in world space.
### Making a Custom Editor
The above demonstrates how you can get simple scripts running during edit-time, however this alone does not allow you to create your own Editor tools. The next step is to create a **Custom Editor** for the script you just created.
When you create a script in Unity, by default it inherits from MonoBehaviour, and therefore is a component that you can attach to a GameObject. When you place a component on a GameObject, the Inspector displays a default interface that you can use to view and edit every public variable, for example: an integer, a float, or a string.
This is how the Inspector for the LookAtPoint component looks by default:
![A default Inspector with a public Vector3 field](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/NoCustomInspector.png) A default Inspector with a public Vector3 field
**A custom editor is a separate script which _replaces_ this default layout with any editor controls that you choose.**
To create the custom editor for the LookAtPoint script:
  1. Create a new C# script and name it “LookAtPointEditor”.
  2. Open the script and replace its contents with the code below.

```
using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(LookAtPoint))]
[CanEditMultipleObjects]
public class LookAtPointEditor : Editor 
{
    SerializedProperty lookAtPoint;
    
    void OnEnable()
    {
        lookAtPoint = serializedObject.FindProperty("lookAtPoint");
    }

    public override void OnInspectorGUI()
    {
        serializedObject.Update();
        EditorGUILayout.PropertyField(lookAtPoint);
        serializedObject.ApplyModifiedProperties();
    }
}

```

This class must inherit from **Editor**. The **CustomEditor** attribute informs Unity which component it should act as an editor for. The **CanEditMultipleObjects** attribute tells Unity that you can select multiple objects with this editor and change them all at the same time.
Unity executes the code in OnInspectorGUI it displays the editor in the Inspector. You can put any GUI code in here and it works in the same way as OnGUI does, but runs inside the Inspector. Editor defines the target property that you can use to access the GameObject you are inspecting. 
This is how the Inspector for the LookAtPoint component looks with the new editor:
![The Look At Point component in the new editor](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CustomInspector.png) The Look At Point component in the new editor
This looks very similar (although the “Script” field is now not present, because the editor script does not add any Inspector code to show it).
However now that you have control over how the Inspector displays in an Editor script, you can use any code you like to lay out the Inspector fields, allow the user to adjust the values, and even display graphics or other **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement). In fact all of the Inspectors you see within the Unity Editor including the more complex Inspectors such as the **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) system and animation import settings, are all made using the same API that you have access to when creating your own custom Editors.
Here is a simple example which extends your editor script to display a message that indicates whether the target point is above or below the GameObject:
```
using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(LookAtPoint))]
[CanEditMultipleObjects]
public class LookAtPointEditor : Editor
{
    SerializedProperty lookAtPoint;

    void OnEnable()
    {
        lookAtPoint = serializedObject.FindProperty("lookAtPoint");
    }

    public override void OnInspectorGUI()
    {
        serializedObject.Update();
        EditorGUILayout.PropertyField(lookAtPoint);
        serializedObject.ApplyModifiedProperties();
        if (lookAtPoint.vector3Value.y > (target as LookAtPoint).transform.position.y)
        {
            EditorGUILayout.LabelField("(Above this object)");
        }
        if (lookAtPoint.vector3Value.y < (target as LookAtPoint).transform.position.y)
        {
            EditorGUILayout.LabelField("(Below this object)");
        }
    }
}

```

This is how the Inspector for the LookAtPoint component looks with the message showing if the target point is above or below the GameObject.
![The component in the Inspector now includes information about the targets location relative to the GameObject](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CustomInspector2.png) The component in the Inspector now includes information about the target’s location relative to the GameObject
You have full access to all the IMGUI commands to draw any type of interface, including rendering Scenes using a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) within Editor windows.
### Scene View Additions
You can add extra code to the **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView). To do this, implement OnSceneGUI in your custom editor. 
OnSceneGUI works just like OnInspectorGUI except it runs in the Scene view. To help you make your own editing controls, you can use the functions defined in the [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html) class. All functions in there are designed for working in 3D Scene views.
```
using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(LookAtPoint))]
[CanEditMultipleObjects]
public class LookAtPointEditor : Editor
{
    SerializedProperty lookAtPoint;

    void OnEnable()
    {
        lookAtPoint = serializedObject.FindProperty("lookAtPoint");
    }

    public override void OnInspectorGUI()
    {
        serializedObject.Update();
        EditorGUILayout.PropertyField(lookAtPoint);
        if (lookAtPoint.vector3Value.y > (target as LookAtPoint).transform.position.y)
        {
            EditorGUILayout.LabelField("(Above this object)");
        }
        if (lookAtPoint.vector3Value.y < (target as LookAtPoint).transform.position.y)
        {
            EditorGUILayout.LabelField("(Below this object)");
        }
        
            
        serializedObject.ApplyModifiedProperties();
    }

    public void OnSceneGUI()
    {
        var t = (target as LookAtPoint);

        EditorGUI.BeginChangeCheck();
        Vector3 pos = Handles.PositionHandle(t.lookAtPoint, Quaternion.identity);
        if (EditorGUI.EndChangeCheck())
        {
            Undo.RecordObject(target, "Move point");
            t.lookAtPoint = pos;
            t.Update();
        }
    }
}

```

If you want to add 2D GUI objects (for example: GUI or EditorGUI), you need to wrap them in calls to Handles.BeginGUI() and Handles.EndGUI().
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-PropertyDrawers.html)
Use Property Drawers with IMGUI to customize the Inspector
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TreeViewAPI.html)
Create TreeView with IMGUI
