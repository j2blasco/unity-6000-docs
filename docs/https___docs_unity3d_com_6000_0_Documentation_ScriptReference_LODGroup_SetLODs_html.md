* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODGroup.SetLODs.html

#  [LODGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODGroup.html).SetLODs
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html "Go to LODGroup Component in the Manual")
## Declaration
public void SetLODs(LOD[] lods); 
### Parameters
Parameter | Description  
---|---  
lods | The LODs to use for this group.  
### Description
Set the LODs for the LOD group. This will remove any existing LODs configured on the LODGroup.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public LODGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODGroup.html) group;  
  
    void Start()
    {
        // Programmatically create a LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html) group and add LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html) levels.
        // Create a GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) that allows for forcing a specific LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html) level.
        group = gameObject.AddComponent<LODGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODGroup.html)>();  
  
        // Add 4 LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html) levels
        LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html)[] lods = new LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html)[4];
        for (int i = 0; i < 4; i++)
        {
            PrimitiveType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.html) primType = PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html);
            switch (i)
            {
                case 1:
                    primType = PrimitiveType.Capsule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Capsule.html);
                    break;
                case 2:
                    primType = PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html);
                    break;
                case 3:
                    primType = PrimitiveType.Cylinder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cylinder.html);
                    break;
            }
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(primType);
            go.transform.parent = gameObject.transform;
            Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)[] renderers = new Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)[1];
            renderers[0] = go.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
            lods[i] = new LOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html)(1.0F / (i + 2), renderers);
        }
        group.SetLODs(lods);
        group.RecalculateBounds();
    }  
  
    void OnGUI()
    {
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Enable / Disable"))
            group.enabled = !group.enabled;  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Default"))
            group.ForceLOD(-1);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Force 0"))
            group.ForceLOD(0);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Force 1"))
            group.ForceLOD(1);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Force 2"))
            group.ForceLOD(2);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Force 3"))
            group.ForceLOD(3);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Force 4"))
            group.ForceLOD(4);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Force 5"))
            group.ForceLOD(5);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Force 6"))
            group.ForceLOD(6);
    }
}

```

* * *
