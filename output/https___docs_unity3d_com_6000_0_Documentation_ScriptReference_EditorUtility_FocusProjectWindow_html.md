* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.FocusProjectWindow.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).FocusProjectWindow
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
public static void FocusProjectWindow(); 
### Description
Brings the project window to the front and focuses it.
This is commonly called after a menu item that creates and selects an asset is invoked.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorUtilityFocusProjectWindow.png)  
_Changes the color of the selected GameObjects._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class FocusProjectWindowExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    static Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)    matColor = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);  
  

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Change")]
    static void Init()
    {
        // Get existing open window or if none, make a new one:
        FocusProjectWindowExample window = (FocusProjectWindowExample)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(FocusProjectWindowExample));
        window.Show();
    }  
  
    void OnGUI()
    {
        matColor = EditorGUI.ColorField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ColorField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 15), "New Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html):", matColor);
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25, position.width - 6, 30), "Change"))
            ChangeColors();
    }  
  
    void ChangeColors()
    {
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) t in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
            {
                Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = t.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
                if (rend)
                    rend.sharedMaterial.color = matColor;
            }
        }  
  
        EditorUtility.FocusProjectWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.FocusProjectWindow.html)();
    }  
  
    void OnInspectorUpdate()
    {
        Repaint();
    }
}

```

* * *
