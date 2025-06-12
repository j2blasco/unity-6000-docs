* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginToggleGroup.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).BeginToggleGroup
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
public static bool BeginToggleGroup(string label, bool toggle); 
## Declaration
public static bool BeginToggleGroup([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, bool toggle); 
### Parameters
Parameter | Description  
---|---  
label | Label to show above the toggled controls.  
toggle | Enabled state of the toggle group.  
### Returns
**bool** The enabled state selected by the user. 
### Description
Begin a vertical group with a toggle to enable or disable all the controls within at once.
Additional resources: [EndToggleGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndToggleGroup.html).  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Aligner.png)  
_Align position/rotation/scale of the selected GameObjects._
```
// Simple script that lets you align GameObjects
// position/rotation/scale wise with the selected active transform  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Aligner : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    bool[] pos = new bool[3] { true, true, true };
    bool[] rot = new bool[3] { true, true, true };
    bool[] scale = new bool[3] { true, true, true };  
  
    bool posGroupEnabled = true;
    bool rotGroupEnabled = true;
    bool scaleGroupEnabled = false;  
  
    void OnGUI()
    {
        posGroupEnabled = EditorGUILayout.BeginToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginToggleGroup.html)("Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html) position", posGroupEnabled);
        pos[0] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("x", pos[0]);
        pos[1] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("y", pos[1]);
        pos[2] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("z", pos[2]);
        EditorGUILayout.EndToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndToggleGroup.html)();  
  
        rotGroupEnabled = EditorGUILayout.BeginToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginToggleGroup.html)("Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html) rotation", rotGroupEnabled);
        rot[0] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("x", rot[0]);
        rot[1] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("y", rot[1]);
        rot[2] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("z", rot[2]);
        EditorGUILayout.EndToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndToggleGroup.html)();  
  
        scaleGroupEnabled = EditorGUILayout.BeginToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginToggleGroup.html)("Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html) scale", scaleGroupEnabled);
        scale[0] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("x", scale[0]);
        scale[1] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("y", scale[1]);
        scale[2] = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("z", scale[2]);
        EditorGUILayout.EndToggleGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndToggleGroup.html)();  
  
        GUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Space.html)(30);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html)!"))
            Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html)();
    }  
  
    void Align[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html)()
    {
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[] transforms = Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html);
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) activeTransform = Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html);
        if (transforms.Length < 2)
        {
            Debug.LogWarning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogWarning.html)("Aligner: select at least two objects.");
            return;
        }
        for (int i = 0; i < transforms.Length; i++)
        {
            if (posGroupEnabled)
            {
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) newPos;
                newPos.x = pos[0] ?
                    activeTransform.position.x : transforms[i].position.x;
                newPos.y = pos[1] ?
                    activeTransform.position.y : transforms[i].position.y;
                newPos.z = pos[2] ?
                    activeTransform.position.z : transforms[i].position.z;
                transforms[i].position = newPos;
            }
            if (rotGroupEnabled)
            {
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) newRot;
                newRot.x = rot[0] ?
                    activeTransform.rotation.eulerAngles.x : transforms[i].rotation.eulerAngles.x;
                newRot.y = rot[1] ?
                    activeTransform.rotation.eulerAngles.y : transforms[i].rotation.eulerAngles.y;
                newRot.z = rot[2] ?
                    activeTransform.rotation.eulerAngles.z : transforms[i].rotation.eulerAngles.z;
                transforms[i].rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(newRot);
            }
            if (scaleGroupEnabled)
            {
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) newScale;
                newScale.x = scale[0] ?
                    activeTransform.localScale.x : transforms[i].localScale.x;
                newScale.y = scale[1] ?
                    activeTransform.localScale.y : transforms[i].localScale.y;
                newScale.z = scale[2] ?
                    activeTransform.localScale.z : transforms[i].localScale.z;
                transforms[i].localScale = newScale;
            }
        }
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html)-Rotation-Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) Aligner")]
    static void Init()
    {
        Aligner window = (Aligner)EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(Aligner));
        window.Show();
    }
}

```

* * *
