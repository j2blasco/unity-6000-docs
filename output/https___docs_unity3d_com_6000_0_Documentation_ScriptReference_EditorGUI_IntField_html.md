* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).IntField
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
public static int IntField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static int IntField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, int value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
## Declaration
public static int IntField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int value, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.numberField); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the int field.  
label | Optional label to display in front of the int field.  
value | The value to edit.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**int** The value entered by the user. 
### Description
Makes a text field for entering integers.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIIntField.png)   
_Int Field in an Editor Window._
```
//Create a folder and name it "Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)" (Right click in your Project Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) folder and go to Create>Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html)) if you don't already have one
//Place this script in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) folder
//This script creates a new menu at the top of the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) named "Examples" with one item "Clone Object".  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    int clones = 1;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Clone Object")]
    static void Init()
    {
        //Create the new Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) window and show it
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(Example));
        window.Show();
    }  
  
    void OnGUI()
    {
        //The field which allows you to input the amount of clones of a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you want
        clones = EditorGUI.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 35, position.width, 15), "Number of clones:", clones);  
  
        //If there isn't a currently selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), this message appears
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) == null)
            EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width, 20), "Please click on a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in your Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)!");  
  
        //Press the clone Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 55, position.width, 20), "Clone!"))
        {
            //Check that you have a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) selected
            if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null)
            {
                //Loop until the number of clones is reached
                for (int i = 0; i < clones; i++)
                {
                    //Spawn each of the clones
                    Instantiate(Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html), Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
                }
            }
        }
    }
}

```

* * *
