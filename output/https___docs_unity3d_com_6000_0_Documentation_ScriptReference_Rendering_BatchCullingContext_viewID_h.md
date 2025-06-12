* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext-viewID.html

#  [BatchCullingContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext.html).viewID
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
[Rendering.BatchPackedCullingViewID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.html) viewID; 
### Description
The ID of the object from which the culling is invoked. Usage example: store culling-related data for each object.
```
// Example of per-view data, indexed by view ID  
  
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;  
  
public class CullingExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private BatchRendererGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) batchRendererGroup;
    private Dictionary<BatchPackedCullingViewID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.html), MyViewData> myPerViewData = new Dictionary<BatchPackedCullingViewID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.html), MyViewData>();  
  
    void Start()
    {
        batchRendererGroup = new BatchRendererGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html)(this.OnPerformCulling, IntPtr.Zero);
    }  
  
    public JobHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) OnPerformCulling[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.OnPerformCulling.html)(
        BatchRendererGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) rendererGroup,
        BatchCullingContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext.html) cullingContext,
        BatchCullingOutput[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingOutput.html) cullingOutput,
        IntPtr userContext)
    {
        if (!myPerViewData.ContainsKey(cullingContext.viewID))
        {
            // If the data doesn't exist for the current view, create it.
            myPerViewData[cullingContext.viewID] = new MyViewData();
        }
        MyViewData currentViewData = myPerViewData[cullingContext.viewID];  
  
        // Do stuff with the current view's data.  
  
        /* You can also get the instance ID of the current view's gameObject
           (for example, Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html), Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html), etc.) as follows: */
        int instanceID = cullingContext.viewID.GetInstanceID();  
  
        /* The slice index depends on the view type.
           For example, for Cameras, the slice index is always zero.
           For cascaded shadow maps, it equals the index of the cascade. */
        int sliceIndex = cullingContext.viewID.GetSliceIndex();
    }
}

```

* * *
