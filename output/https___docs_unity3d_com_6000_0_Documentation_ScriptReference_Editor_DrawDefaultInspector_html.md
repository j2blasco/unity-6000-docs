* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawDefaultInspector.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).DrawDefaultInspector
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
public bool DrawDefaultInspector(); 
### Returns
**bool** Returns true if any GUI controls in the default Inspector changed the value of the input data, otherwise returns false. 
### Description
Draws the built-in Inspector.
Call this method, within the OnInspectorGUI method, to automatically draw the Inspector. This is useful if you want to add a few buttons without having to redo the entire Inspector. Additional resources: [OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html).
```
// This example shows a custom inspector for an
// object "MyPlayer", which has a variable speed.
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyPlayer : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Hide this field so that it is not shown twice when drawing the default Inspector.
    [HideInInspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html)]
    public float speed;  
  
    public int gear;
}  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyPlayer))]
public class Example : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public override void OnInspectorGUI()
    {
        MyPlayer targetPlayer = (MyPlayer)target;
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html) ("Some help", "Some other text");  
  
        targetPlayer.speed = EditorGUILayout.Slider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Slider.html) ("Speed", targetPlayer.speed, 0, 100);  
  
        // Show default inspector property editor
        if(DrawDefaultInspector())
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Gear was changed!");
    }
}

```

* * *
