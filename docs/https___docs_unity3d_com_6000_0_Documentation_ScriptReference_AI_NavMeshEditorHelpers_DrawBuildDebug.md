* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshEditorHelpers.DrawBuildDebug.html

#  [NavMeshEditorHelpers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshEditorHelpers.html).DrawBuildDebug
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
public static void DrawBuildDebug([AI.NavMeshData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html) navMeshData, [AI.NavMeshBuildDebugFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildDebugFlags.html) flags = NavMeshBuildDebugFlags.All); 
### Parameters
Parameter | Description  
---|---  
navMeshData | NavMesh object for which debug data has been deliberately collected during the build process.  
flags | Bitmask that designates the types of data to show at one time.  
### Description
Displays in the Editor the precise intermediate data used during the build process of the specified NavMesh.
Additional resources: [NavMeshBuildSettings.debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSettings-debug.html).
```
using System.Collections.Generic;
using UnityEditor.AI;
using UnityEngine;
using UnityEngine.AI;  
  
public class NavMeshBuildDebugDraw : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    NavMeshData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html) m_NavMeshData;  
  
    void Start()
    {
        var bounds = new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)(transform.position, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(100.0f, 100.0f, 100.0f));
        var markups = new List<NavMeshBuildMarkup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildMarkup.html)>();
        var sources = new List<NavMeshBuildSource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildSource.html)>();
        NavMeshEditorHelpers.CollectSourcesInStage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshEditorHelpers.CollectSourcesInStage.html)(
            bounds, ~0, NavMeshCollectGeometry.RenderMeshes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshCollectGeometry.RenderMeshes.html), 0, markups, gameObject.scene, sources);  
  
        var settings = NavMesh.GetSettingsByID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMesh.GetSettingsByID.html)(0);
        var debug = new NavMeshBuildDebugSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildDebugSettings.html)();
        debug.flags = NavMeshBuildDebugFlags.All[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildDebugFlags.All.html);
        settings.debug = debug;  
  
        m_NavMeshData = new NavMeshData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshData.html)();
        UnityEngine.AI.NavMeshBuilder.UpdateNavMeshDataAsync(m_NavMeshData, settings, sources, bounds);
    }  
  
    void OnDrawGizmos()
    {
        NavMeshEditorHelpers.DrawBuildDebug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshEditorHelpers.DrawBuildDebug.html)(
            m_NavMeshData, NavMeshBuildDebugFlags.Regions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildDebugFlags.Regions.html) | NavMeshBuildDebugFlags.SimplifiedContours[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuildDebugFlags.SimplifiedContours.html));
    }
}

```

* * *
