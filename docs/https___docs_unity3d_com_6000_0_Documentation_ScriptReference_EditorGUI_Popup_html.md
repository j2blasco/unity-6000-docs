* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Popup.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).Popup
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
public static int Popup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selectedIndex, string[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int Popup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selectedIndex, GUIContent[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int Popup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, int selectedIndex, string[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int Popup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int selectedIndex, GUIContent[] displayedOptions, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label in front of the field.  
selectedIndex | The index of the option the field shows.  
displayedOptions | An array with the options shown in the popup.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**int** The index of the option that has been selected by the user. 
### Description
Makes a generic popup selection field.
Takes the currently selected index as a parameter and returns the index selected by the user.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIPopup.png)  
_Popup in and Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

// Adds a component to the selected GameObjects  
  
class EditorGUIPopup : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string[] options = { "Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)", "Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html) Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)", "Sphere Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)" };
    int index = 0;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Popup usage")]
    static void Init()
    {
        var window = GetWindow<EditorGUIPopup>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 180, 80);
        window.Show();
    }  
  
    void OnGUI()
    {
        index = EditorGUI.Popup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Popup.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, position.width, 20),
            "Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html):",
            index,
            options);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 25, position.width, position.height - 26), "Add Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)"))
            AddComponentToObjects();
    }  
  
    void AddComponentToObjects()
    {
        if (!Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Please select at least one GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) first");
            return;
        }  
  
        foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) obj in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
        {
            switch (index)
            {
                case 0:
                    obj.AddComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
                    break;  
  
                case 1:
                    obj.AddComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>();
                    break;  
  
                case 2:
                    obj.AddComponent<SphereCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SphereCollider.html)>();
                    break;
            }
        }
    }
}

```

**Note:** The `displayedOptions` lists an array of options. When these elements contain "/" (slash characters) the elements are use for sub-menus. The text to the left of the slashes determines the structure.
* * *
