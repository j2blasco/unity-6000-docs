* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.SelectionGrid.html

#  [GUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.html).SelectionGrid
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
public static int SelectionGrid(int selected, string[] texts, int xCount, params GUILayoutOption[] options); 
## Declaration
public static int SelectionGrid(int selected, Texture[] images, int xCount, params GUILayoutOption[] options); 
## Declaration
public static int SelectionGrid(int selected, GUIContent[] content, int xCount, params GUILayoutOption[] options); 
## Declaration
public static int SelectionGrid(int selected, string[] texts, int xCount, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int SelectionGrid(int selected, Texture[] images, int xCount, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int SelectionGrid(int selected, GUIContent[] contents, int xCount, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
selected | The index of the selected button.  
texts | An array of strings to show on the buttons.  
images | An array of textures on the buttons.  
contents | An array of text, image and tooltips for the button.  
xCount | How many elements to fit in the horizontal direction. The elements will be scaled to fit unless the style defines a fixedWidth to use. The height of the control will be determined from the number of elements.  
style | The style to use. If left out, the `button` style from the current [GUISkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**int** The index of the selected button. 
### Description
Make a Selection Grid.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/GUILayoutSelectionGrid.png)   
_Selection grid in the Game View._
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    int selGridInt = 0;
    string[] selStrings = {"radio1", "radio2", "radio3"};  
  
    void OnGUI()
    {
        GUILayout.BeginVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginVertical.html)("Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html)");
        selGridInt = GUILayout.SelectionGrid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.SelectionGrid.html)(selGridInt, selStrings, 1);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Start"))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("You chose " + selStrings[selGridInt]);
        }
        GUILayout.EndVertical[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndVertical.html)();
    }
}

```

* * *
