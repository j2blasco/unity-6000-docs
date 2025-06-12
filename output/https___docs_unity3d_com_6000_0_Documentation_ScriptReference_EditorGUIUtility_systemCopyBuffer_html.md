* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-systemCopyBuffer.html

#  [EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html).systemCopyBuffer
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
systemCopyBuffer; 
### Description
The system copy buffer.
Use this to make Copy and Paste work for your own application. The [systemCopyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-systemCopyBuffer.html) captures any text that is selected on the machine. This does not specifically have to be text that is selected in Unity. Reading and writing [systemCopyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-systemCopyBuffer.html) is possible. ![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIUtilitySystemCopyBuffer.png)  
_Have more than 1 saved "copy" command._
```
// Example that shows up to 5 strings.  These strings are captured from Copy
// commands on the machine.  The Current buffer at the bottom of the window shows whatever string
// is copied.  The string can be copied to one of the five Save rows when the Load toggle is
// five Save rows when the Load toggle is off and one of the horizontal buttons is pressed.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SystemCopyBufferExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    string[] savedCopies = new string[5];
    bool load = false;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Example showing systemCopyBuffer")]
    static void systemCopyBufferExample()
    {
        SystemCopyBufferExample window =
            EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<SystemCopyBufferExample>();
        window.Show();
    }  
  
    void OnGUI()
    {
        load = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("Load:", load);  
  
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        for (int i = 0; i < savedCopies.Length; i++)
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)(i.ToString()))
                if (load)
                    EditorGUIUtility.systemCopyBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-systemCopyBuffer.html) = savedCopies[i];
                else
                    savedCopies[i] = EditorGUIUtility.systemCopyBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-systemCopyBuffer.html);
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();  
  
        for (int j = 0; j < savedCopies.Length; j++)
            EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Saved " + j, savedCopies[j]);  
  
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Current buffer:", EditorGUIUtility.systemCopyBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-systemCopyBuffer.html));
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Clear all saves"))
            for (int s = 0; s < savedCopies.Length; s++)
                savedCopies[s] = "";
    }  
  
    void OnInspectorUpdate()
    {
        this.Repaint();
    }
}

```

**Note:** iOS and Android do not support this feature.
* * *
