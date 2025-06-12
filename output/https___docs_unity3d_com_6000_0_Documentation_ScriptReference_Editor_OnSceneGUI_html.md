* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).OnSceneGUI()
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Enables the Editor to handle an event in the Scene view.
In the [OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html) you can, for example, edit meshes, paint terrain, or have advanced gizmos. Refer to the [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html) class for methods related to drawing interactable visuals in the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).  
  
If you want to draw elements in the Scene view, for instance by using `Graphics.DrawMeshNow`, only do so during [EventType.Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.Repaint.html).   
  
In the following two scripts, [OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html) is used to draw lines between GameObjects. The first script shows how [OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html) is used. In this script, a GameObject is used as a parent. The script obtains the position of the parent and then draws lines from that position to GameObjects stored in an array. The script uses [Handles.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html) to draw lines. The documentation for [Handles.DrawLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html) has a very similar example.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)( typeof( DrawLine ) )]
public class DrawLineEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    // Draw lines between a chosen GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    // and a selection of added GameObjects  
  
    void OnSceneGUI()
    {
        // Get the chosen GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        DrawLine t = target as DrawLine;  
  
        if( t == null || t.GameObjects == null )
            return;  
  
        // Grab the center of the parent
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center = t.transform.position;  
  
        // Iterate over GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) added to the array...
        for( int i = 0; i < t.GameObjects.Length; i++ )
        {
            // ... and draw a line between them
            if( t.GameObjects[i] != null )
                Handles.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawLine.html)( center, t.GameObjects[i].transform.position );
        }
    }
}

```

This script stores the array of GameObjects which have a line drawn to them. This regular script is attached to a GameObject which is considered to be the starting point for all lines.
```
using UnityEngine;  
  
[ExecuteInEditMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html)]
public class DrawLine : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // an array of game objects which will have a
    // line drawn to in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) editor
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] GameObjects;
}

```

* * *
