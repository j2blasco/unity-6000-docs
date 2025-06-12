* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup-probePositions.html

#  [LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html).probePositions
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeGroup.html "Go to LightProbeGroup Component in the Manual")
probePositions; 
### Description
Editor only function to access and modify probe positions.
Probe positions are specified in local space relative to the parent object.  
  
At runtime this function will return an empty Vector3 array and setting it will have no effect.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class ExampleScript : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    private LightProbeGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) lightProbes = null;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Set Probe Positions")]
    static void Init()
    {
        var window = GetWindowWithRect<ExampleScript>(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 350, 50));
        window.Show();
    }  
  
    void OnGUI()
    {
        lightProbes = (LightProbeGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html))EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)(
            "Find Dependency",     // string
            lightProbes,       // Object
            typeof(LightProbeGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html)),     // Type
            true);  
  
        if (lightProbes)
        {
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Set Probe Positions"))
            {
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] positions = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[4];
                positions[0] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.0f, 0.0f);
                positions[1] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f, 0.0f, 0.0f);
                positions[2] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 1.0f, 0.0f);
                positions[3] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f, 1.0f, 1.0f);
                lightProbes.probePositions = positions;
            }
        }
        else
        {
            EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Missing:", "Please select an object first!");
        }
    }
}

```

* * *
