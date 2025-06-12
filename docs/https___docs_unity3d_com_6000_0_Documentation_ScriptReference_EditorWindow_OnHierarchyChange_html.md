* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnHierarchyChange.html

#  [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).OnHierarchyChange()
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
Handler for message that is sent when an object or group of objects in the hierarchy changes.
Actions that trigger this message include creating, renaming, reparenting, or destroying objects in the current hierarchy, as well as loading, unloading, renaming, or reordering loaded Scenes. Note that the message is not sent immediately in response to these actions, but rather during the next update of the editor application.  
  
Actions taken with objects that have [HideFlags.HideInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html) set will not cause this message to be sent, but changing [Object.hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) will.  
  
The [OnHierarchyChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnHierarchyChange.html)() is added to the Unity editor. Adding a new GameObject into the Scene, or changing the position of a GameObject in the Inspector will be observed by [OnHierarchyChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnHierarchyChange.html)(). Similarly, changes to the rotation and scale will be seen.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorWindowOnHierarchyChange.gif)  
_An animation showing how the OnHierarchyChange can be used._  
  
Additional resources: EditorApplication.hierarchyChange  
  
The following example script created an [EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) that monitors the number of objects and updates whenever the hierarchy changes. Copy it into a file called HierarchyMonitorWindow.cs and put it in a folder called Editor.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;

class HierarchyMonitorWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.html) Monitor")]
    static void CreateWindow()
    {
        EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<HierarchyMonitorWindow>();
    }

    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    int m_NumberVisible;

    void OnEnable()
    {
        titleContent.text = "Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.html) Monitor";
        // Manually call the event handler when the window is first loaded so its contents are up-to-date.
        OnHierarchyChange();
    }

    void OnHierarchyChange()
    {
        var all = Resources.FindObjectsOfTypeAll[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.FindObjectsOfTypeAll.html)(typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)));
        m_NumberVisible = CountVisibleObjects(all);
        var label = rootVisualElement.Q<Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)>();
        if (label != null)
            label.text = $"There are currently {m_NumberVisible} GameObjects visible in the hierarchy.";
    }

    int CountVisibleObjects(Object[] objects)
    {
        int count = 0;
        foreach (var obj in objects)
        {
            var gameObject = obj as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
            if (gameObject != null && (gameObject.hideFlags & HideFlags.HideInHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html)) != HideFlags.HideInHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html))
            {
                count++;
            }
        }
        return count;
    }

    void CreateGUI()
    {
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)($"There are currently {m_NumberVisible} GameObjects visible in the hierarchy.");
        rootVisualElement.Add(label);
    }
}

```

Another simple example. 
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UIElements;

public class OnHierarchyChangeExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static int count = 0;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/OnHierarchyChange Example")]
    static void Init()
    {
        OnHierarchyChangeExample window = (OnHierarchyChangeExample)GetWindow(typeof(OnHierarchyChangeExample));
        window.Show();
    }

    void OnHierarchyChange()
    {
        count += 1;
    }

    void CreateGUI()
    {
        var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)();
        rootVisualElement.Add(label);

        label.schedule.Execute(() =>
        {
            label.text = $"OnHierarchyChange: {count}";
        }).Every(10);
    }
}

```

* * *
