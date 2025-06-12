* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.html

# OnDemandResourcesRequest
class in UnityEngine.iOS
/
Inherits from:[AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html)
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
Represents a request for On Demand Resources (ODR). It's an [AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) and can be yielded in a coroutine.
**NOTE:** only available on iOS.  
  
Creating an [OnDemandResourcesRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.html) is equivalent to calling [ NSBundleResourceRequest.beginAccessingResourcesWithCompletionHandler ](https://developer.apple.com/reference/foundation/nsbundleresourcerequest/1614840-beginaccessingresources). The request will keep the on demand resource alive until either [Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.Dispose.html)() is called or the request object is collected by a garbage collector, which is the equivalent of calling [NSBundleResourceRequest.endAccessingResources ](https://developer.apple.com/reference/foundation/nsbundleresourcerequest/1614843-endaccessingresources).
```
using UnityEngine;
using UnityEngine.iOS;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;  
  
public static class Loader
{
    public static IEnumerator LoadAsset(string resourceName)
    {
        // Create the request
        var request = OnDemandResources.PreloadAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResources.PreloadAsync.html)(new string[] { "Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)'s ODR tag" });  
  
        // Wait until request is completed
        yield return request;  
  
        // Check for errors
        if (request.error != null)
            throw new Exception("ODR request failed: " + request.error);  
  
        // Get path to the resource and use it
        var path = request.GetResourcePath(resourceName);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(path);  
  
        // Call Dispose() when resource is no longer needed.
        request.Dispose();
    }
}

```

### Properties
Property | Description  
---|---  
[error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest-error.html) | Returns an error after operation is complete.  
[loadingPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest-loadingPriority.html) | Sets the priority for request.  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.Dispose.html) | Release all resources kept alive by On Demand Resources (ODR) request.  
[GetResourcePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.GetResourcePath.html) | Gets file system's path to the resource available in On Demand Resources (ODR) request.  
### Inherited Members
### Properties
Property | Description  
---|---  
[allowSceneActivation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-allowSceneActivation.html) | Allow Scenes to be activated as soon as it is ready.  
[isDone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-isDone.html) | Has the operation finished? (Read Only)  
[priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-priority.html) | Priority lets you tweak in which order async operation calls will be performed.  
[progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-progress.html) | What's the operation's progress. (Read Only)  
### Events
Event | Description  
---|---  
[completed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation-completed.html) | Event that is invoked upon operation completion. An event handler that is registered in the same frame as the call that creates it will be invoked next frame, even if the operation is able to complete synchronously. If a handler is registered after the operation has completed and has already invoked the complete event, the handler will be called synchronously.  
* * *
