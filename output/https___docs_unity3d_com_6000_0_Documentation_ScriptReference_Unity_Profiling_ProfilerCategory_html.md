* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.html

# ProfilerCategory
struct in Unity.Profiling
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Use to specify category for instrumentation Profiler markers.
```
using Unity.Profiling;  
  
public class MySystemClass
{
    static readonly ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) s_SimulatePerfMarker = new ProfilerMarker[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html)(ProfilerCategory.Ai[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Ai.html), "MySystem.Simulate");  
  
    public void UpdateLogic()
    {
        using (s_SimulatePerfMarker.Auto())
        {
            // ...
        }
    }
}

```

Additional resources: [ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html).
### Static Properties
Property | Description  
---|---  
[Ai](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Ai.html) | AI and NavMesh Profiler category.  
[Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Animation.html) | Animation Profiler category.  
[Audio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Audio.html) | Audio system Profiler category.  
[FileIO](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.FileIO.html) | File IO Profiler category.  
[Gui](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Gui.html) | UI Profiler category.  
[Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Input.html) | Input system Profiler category.  
[Internal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Internal.html) | Internal Unity systems Profiler category.  
[Lighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Lighting.html) | Global Illumination Profiler category.  
[Loading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Loading.html) | Loading system Profiler category.  
[Memory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Memory.html) | Memory allocation Profiler category.  
[Network](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Network.html) | Networking system Profiler category.  
[Particles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Particles.html) | Particle system Profiler category.  
[Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Physics.html) | Physics system Profiler category.  
[Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Physics2D.html) | The Physics 2D system category for the Profiler.  
[Render](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Render.html) | Rendering system Profiler category.  
[Scripts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Scripts.html) | Generic C# code Profiler category.  
[Video](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Video.html) | Video system Profiler category.  
[VirtualTexturing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.VirtualTexturing.html) | Virtual Texturing system Profiler category.  
[Vr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Vr.html) | VR systen Profiler category.  
### Properties
Property | Description  
---|---  
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Color.html) | Gets Profiler category color.  
[Name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.Name.html) | Gets Profiler category name.  
### Constructors
Constructor | Description  
---|---  
[ProfilerCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory-ctor.html) | Use to construct ProfilerCategory by category name.  
* * *
