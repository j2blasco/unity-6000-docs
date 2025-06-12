* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CreateGameObjectWithHideFlags.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).CreateGameObjectWithHideFlags
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
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) CreateGameObjectWithHideFlags(string name, [HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html) flags, params Type[] components); 
### Description
Creates a game object with [HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html) and specified components.
This is very similar to creating a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) the usual way, except it sets the specified [HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html) immediately.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorUtility%20CreateGameObjectWithHideFlags.png) _Editor Window that shows how does the example looks._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateGOHideFlagsExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string objName = "GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)";
    int instanceID = 0;
    bool create = true;
    GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = null;
    bool hideHierarchy = false;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)")]
    static void Init()
    {
        // Get existing open window or if none, make a new one:
        CreateGOHideFlagsExample window = (CreateGOHideFlagsExample)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(CreateGOHideFlagsExample));
        window.Show();
    }  
  
    void OnGUI()
    {
        create = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("Create a GO:", create);
        GUI.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-enabled.html) = create;  
  
        objName = EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Name:", objName);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Create"))
        {
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) created = EditorUtility.CreateGameObjectWithHideFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CreateGameObjectWithHideFlags.html)(objName,
                hideHierarchy ? HideFlags.HideInHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html) : 0);  
  
            instanceID = created.GetInstanceID();
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Created GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) ID: " + instanceID);
        }  
  
        GUI.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-enabled.html) = !create;  
  
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();  
  
        instanceID = EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Instance ID:", instanceID);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Search & Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) flags"))
        {
            go = null;
            go = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(instanceID) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
            if (go)
                go.hideFlags = hideHierarchy ? HideFlags.HideInHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html) : 0;
        }  
  
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();  
  
        if (!go)
            EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Object: ", (go == null) ? "No object was found" : go.name);  
  
        GUI.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-enabled.html) = true;
        hideHierarchy = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("HideInHierarchy", hideHierarchy);
    }  
  
    void OnInspectorUpdate()
    {
        Repaint();
    }
}

```

* * *
