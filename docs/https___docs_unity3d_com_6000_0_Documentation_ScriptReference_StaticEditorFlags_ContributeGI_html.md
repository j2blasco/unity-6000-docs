* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.ContributeGI.html

#  [StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html).ContributeGI
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
### Description
Include the target [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html) in global illumination calculations.
These calculations take place while precomputing lighting data at bake time. The ContributeGI property exposes the [ReceiveGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.html) property. The ContributeGI property only takes effect if you enable a global illumination setting such as [Baked Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#MixedLighting.html) or [Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#RealtimeLighting.html) for the target Scene. For additional context, see [this tutorial for setting up the Built-in Render Pipeline and lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/BestPracticeLightingPipelines.html) in Unity.
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
        var flags = StaticEditorFlags.ContributeGI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.ContributeGI.html);
        GameObjectUtility.SetStaticEditorFlags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html)(go, flags);
    }
}

```

Additional resources: [GameObjectUtility.SetStaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.SetStaticEditorFlags.html), [GameObject.isStatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-isStatic.html).
* * *
