* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-initializing.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html)
  * [Creating a renderer with the BatchRendererGroup API in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-creating-a-renderer.html)
  * Initialize a BatchRendererGroup object in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-creating-a-renderer.html)
Creating a renderer with the BatchRendererGroup API in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-registering-meshes-and-materials.html)
Register meshes and materials with the BatchRendererGroup API in URP
# Initialize a BatchRendererGroup object in URP
The first step to render using BRG is to create an instance of [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) and initialize it with an implementation of [OnPerformCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.OnPerformCulling.html).
The OnPerformCulling callback is the main entry point of BRG and Unity calls it whenever it culls visible objects. For information on the parameters it receives, see [OnPerformCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.OnPerformCulling.html). Typically, there are two tasks that the OnPerformCulling callback needs to perform:
  * Visibility culling to determine which of its instances are visible based on the [BatchCullingContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext.html) parameter.
  * Output the actual draw commands to render those instances. To do this you write to the [BatchCullingOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingOutput.html) parameter.


In simple implementations, you can do these tasks directly in the OnPerformCulling callback, but for high-performance implementations, it’s best practice to do most of this work in [Burst](https://docs.unity3d.com/Packages/com.unity.burst@latest) jobs. The OnPerformCulling callback should return a [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) that completes after the jobs write the output into the [BatchCullingOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingOutput.html) parameter. If your implementation doesn’t use jobs, you can return an empty JobHandle.
See the following code sample for an example of how to create a BatchRendererGroup object and initialize it with the most minimum OnPerformCulling callback that compiles.
```
using System;
using Unity.Collections;
using Unity.Collections.LowLevel.Unsafe;
using Unity.Jobs;
using UnityEngine;
using UnityEngine.Rendering;

public class SimpleBRGExample : MonoBehaviour
{
    private BatchRendererGroup m_BRG;

    private void Start()
    {
        m_BRG = new BatchRendererGroup(this.OnPerformCulling, IntPtr.Zero);
    }

    private void OnDisable()
    {
        m_BRG.Dispose();
    }

    public unsafe JobHandle OnPerformCulling(
        BatchRendererGroup rendererGroup,
        BatchCullingContext cullingContext,
        BatchCullingOutput cullingOutput,
        IntPtr userContext)
    {
        // This example doesn't use jobs, so it can return an empty JobHandle.
        // Performance-sensitive applications should use Burst jobs to implement
        // culling and draw command output. In this case, this function would return a
        // handle here that completes when the Burst jobs finish.
        return new JobHandle();
    }
}

```

Before you use OnPerformCulling to create draw commands, you need to provide your BatchRendererGroup object any meshes you want it to draw, and any materials you want it to use. For more information, see the next topic, [Registering meshes and materials](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-registering-meshes-and-materials.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-creating-a-renderer.html)
Creating a renderer with the BatchRendererGroup API in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group-registering-meshes-and-materials.html)
Register meshes and materials with the BatchRendererGroup API in URP
