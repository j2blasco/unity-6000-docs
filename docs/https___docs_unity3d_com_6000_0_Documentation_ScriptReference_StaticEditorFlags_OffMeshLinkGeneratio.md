* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.OffMeshLinkGeneration.html

**Method group is Obsolete**   

#  [StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html).OffMeshLinkGeneration
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
**Obsolete** Enum member StaticEditorFlags.OffMeshLinkGeneration has been deprecated. You can now use NavMeshBuilder.CollectSources() and NavMeshBuildMarkup to nominate the objects that will generate Off-Mesh Links.
### Description
Attempt to generate an Off-Mesh Link that starts from this GameObject when precomputing navigation data.
For more information, see the documentation on [[wiki:nav-BuildingOffMeshLinksAutomatically|automatically building Off-Mesh Links].
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
public class StaticEditorFlagsExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Create GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and set Static Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)")]
    static void CreateGameObjectAndSetStaticEditorFlags()
    {
        // Create a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        var go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Example");
        // Set the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s StaticEditorFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html)
        var flags = StaticEditorFlags.OffMeshLinkGeneration;
        GameObjectUtility.SetStaticEditorFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html)(go, flags);
    }
}

```

Additional resources: [GameObjectUtility.SetStaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html), [GameObject.isStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-isStatic.html)
* * *
