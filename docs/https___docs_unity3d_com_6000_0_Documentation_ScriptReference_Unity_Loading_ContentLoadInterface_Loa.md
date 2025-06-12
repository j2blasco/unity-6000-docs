* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentLoadInterface.LoadContentFileAsync.html

#  [ContentLoadInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentLoadInterface.html).LoadContentFileAsync
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
public static [Unity.Loading.ContentFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html) LoadContentFileAsync([Unity.Content.ContentNamespace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.html) nameSpace, string filename, NativeArray<ContentFile> dependencies, [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) dependentFence); 
### Parameters
Parameter | Description  
---|---  
nameSpace | The [ContentNamespace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.html) used to filter the results.  
filename | Path of the file on disk.  
dependencies | List of the [ContentFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html)s that will be referenced by the file being loaded. The ordering must match the ordering returned from the build process. [ContentFile.GlobalTableDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.GlobalTableDependency.html) can be used to indicate that the PersistentManager should be used to resolve references. This allows references to files such as "unity default resources".  
dependentFence | The load will not begin until this [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) completes. A default [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) can be used if there is no dependency.  
### Returns
**ContentFile** Handle to access the results of the load process. 
### Description
Loads a serialized file asynchronously from disk.
The status of the load operation can be accessed using the returned [ContentFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html). Objects loaded with this function will not be garbage collected; the user is responsible for calling [ContentFile.UnloadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.UnloadAsync.html) to free resources when they are no longer required. The user must call [ContentFile.UnloadAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.UnloadAsync.html) even if the load fails.
```
using System.Collections;
using Unity.Collections;
using Unity.Content;
using Unity.Loading;
using UnityEngine;  
  
public class SampleBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public IEnumerator Start()
    {
        NativeArray<ContentFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html)> empty = new NativeArray<ContentFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html)>();
        ContentFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html) depFileHandle = ContentLoadInterface.LoadContentFileAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentLoadInterface.LoadContentFileAsync.html)(ContentNamespace.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.Default.html), "path/to/depfile", empty);  
  
        NativeArray<ContentFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html)> depFiles = new NativeArray<ContentFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html)>(1, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
        depFiles[0] = depFileHandle;
        ContentFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFile.html) rootFileHandle = ContentLoadInterface.LoadContentFileAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentLoadInterface.LoadContentFileAsync.html)(ContentNamespace.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.Default.html), "path/to/rootfile", depFiles);
        depFiles.Dispose();  
  
        // yield coroutine until loading is complete
        while (rootFileHandle.LoadingStatus == LoadingStatus.InProgress[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.LoadingStatus.InProgress.html))
            yield return null;  
  
        ulong localFileIdentifierOfObjectIWant = 25;
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) obj = (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))rootFileHandle.GetObject(localFileIdentifierOfObjectIWant);  
  
        // When done using obj. unload both files.
        ContentFileUnloadHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFileUnloadHandle.html) unloadHandleRoot = rootFileHandle.UnloadAsync();
        ContentFileUnloadHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Loading.ContentFileUnloadHandle.html) unloadHandleDep = depFileHandle.UnloadAsync();  
  
        // yield coroutine until loading is complete
        while (!unloadHandleRoot.IsCompleted || !unloadHandleRoot.IsCompleted)
            yield return null;  
  
        // file is now completly unloaded. obj has been deleted
    }
}

```

* * *
