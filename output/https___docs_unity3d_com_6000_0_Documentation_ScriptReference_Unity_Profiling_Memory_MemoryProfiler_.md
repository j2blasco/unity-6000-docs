* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html

#  [MemoryProfiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.html).TakeSnapshot
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
public static void TakeSnapshot(string path, Action<string,bool> finishCallback, [Unity.Profiling.Memory.CaptureFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.html) captureFlags); 
## Declaration
public static void TakeSnapshot(string path, Action<string,bool> finishCallback, Action<string,bool,DebugScreenCapture> screenshotCallback, [Unity.Profiling.Memory.CaptureFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.html) captureFlags); 
### Parameters
Parameter | Description  
---|---  
path | Destination path for the memory snapshot file.  
finishCallback | Event that is fired once the memory snapshot has finished the process of capturing data. The first parameter denotes if a snapshot file was successfully created on the calling device, the second one contains the resulting snapshot path.  
screenshotCallback | Event that you can specify to retrieve a screenshot after the snapshot has finished. The first parameter denotes if a screenshot file was successfully created on the calling device, the second one contains the resulting screenshot path and the third one the data of the snapshot as [DebugScreenCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.DebugScreenCapture.html).  
captureFlags | Flag mask defining the content of the memory snapshot.  
### Description
Triggers a memory snapshot capture to generate a capture of the memory state that the Memory Profiler can open and analyze.
Request a memory snapshot capture with the provided arguments. Not all fields corresponding to the capture flags are collected. This depends on the target build used to capture the snapshot. Specifically [CaptureFlags.NativeAllocationSites](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocationSites.html) and [CaptureFlags.NativeStackTraces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeStackTraces.html) relate to data that can only be collected from a build that supports the collection of native call stack information. Collecting native call stack information currently requires source code access. When providing these flags to capture from builds that do not support them they are ignored.  
  
The `path` parameter relates to the device that the call is made on, but the connection state of the Editor or Player this method is called from determines what process is captured and where the snapshot file will be created: In the system, there are two different behaviors of data collection:  
  
* When you call this from a Player that is connected to an Editor via [PlayerConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnection.html), the file is not stored locally but streamed out to the connected Editor. The provided path should be empty, or [MemoryProfiler.TakeTempSnapshot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.TakeTempSnapshot.html) could be called instead. The bool value of the `finishCallback` will be false, even if the snapshot was succesfully saved in the Editor.  
  
* When you call this from a Player that is **not** connected to an Editor via [PlayerConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnection.html), the file is created on the host device of the Player.  
  
* When you call this from an Editor, the file is created on the host device of the Editor. If the Editor is not connected to a Player via [EditorConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.EditorConnection.html), it will capture the Player, otherwise it will capture the Editor.  
  
Metadata collection happens just before the snapshot is taken, if at least one listener was registered to the [MemoryProfiler.CreatingMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html) event. At the end of the process, the `finishCallback` is triggered. If a screenshot callback was provided to the call, this is called at the end of the current frame.  
  
Note: * If an absolute path is provided, make sure the application can write to that path. If only a file name or a relative path are provided, the snapshot will be stored at a path relative to [Application.dataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html) and API like File.Open can be used with the same relative path information. * Listeners of the [MemoryProfiler.CreatingMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html) event are notified in the Player or Editor that is being captured, which might not be the Editor that called this method but a connected Player instead. * Screenshot callbacks are only called in standalone players or in Play mode. If no callbacks are supplied for `screenshotCallback`, no screenshot is taken. * It's recommended to call this API from within a [Coroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html), yielding until both callbacks have been called, because the capture process locks code execution on the host device while it is taken and takes time to execute. Calling the API from a coroutine prevents the capturing Editor from locking up in the meantime. * There is no way to capture Play mode in isolation, only the entire Editor. Memory usage in the Editor can differ drastically from that in a built Player. Always make sure to analyze memory usage in development Players running on your target devices. * You can only take the next snapshot after the `finishCallback` is triggered. * Use the [Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/) to open and analyze the resulting files.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;
using System.IO;
using Unity.Collections.LowLevel.Unsafe;
using Unity.Collections;
using Unity.Profiling;
using Unity.Profiling.Memory;
using UnityEngine;  
  
#if UNITY_EDITOR
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Networking.PlayerConnection;
using UnityEngine.Networking.PlayerConnection;
// Reguires com.unity.editorcoroutines package to be installed and its assembly referenced
using Unity.EditorCoroutines.Editor;
#endif  
  
#if UNITY_EDITOR
public class MemoryProfilerExampleWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    IConnectionState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.IConnectionState.html) m_PlayerConnectionState;
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Windows/Analysis/MemoryProfilerAPIExample")]
    static void InitializeOnLoad()
    {
        var window = EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)<MemoryProfilerExampleWindow>();
        window.m_PlayerConnectionState = PlayerConnectionGUIUtility.GetConnectionState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUIUtility.GetConnectionState.html)(window);
        window.Show();
    }  
  
    void TakeSnapshot()
    {
        // In the Unity Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html), the screenshot function only gets called when the not profiling Playmode or if Playmode is active.
        // In otherwords, capturing an Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) outside of Playmode does not create a screenshot and waiting for the callback would create and endless loop.
        var takeScreenshot = m_PlayerConnectionState.connectedToTarget == ConnectionTarget.Player[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.ConnectionTarget.Player.html) || Application.isPlaying[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isPlaying.html);
        EditorCoroutineUtility.StartCoroutine(MemoryProfilerExample.TakeSnapshot(takeScreenshot), this);
    }
}
#endif  
  
public static class MemoryProfilerExample
{
    public static IEnumerator TakeSnapshot(bool takeScreenshot)
    {
        var snapshotFileName = "SnapshotName.tmpsnap";
        // Make sure the file does not exist, e.g. as a left over of a failed previous attempt to take a snapshot.
        if (File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(snapshotFileName))
            File.Delete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Delete.html)(snapshotFileName);  
  
        var snapshotFinished = false;
        var screenshoFinished = false;
        string resultingSnapshotPath = null;
        string resultingScreenshotPath = null;
        var captureFlags = CaptureFlags.ManagedObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.ManagedObjects.html) | CaptureFlags.NativeObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeObjects.html) | CaptureFlags.NativeAllocations[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.NativeAllocations.html);
        Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<string, bool> snapshotCaptureFunction = (snapshotFilePath, success) =>
        {
            snapshotFinished = true;
            if (success)
            {
                resultingSnapshotPath = Path.GetFullPath(snapshotFilePath);
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Snapshot captured and stored at {resultingSnapshotPath}.");
            }
            else
            {
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Failed to take a snapshot.");
            }
        };
        Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html)<string, bool, DebugScreenCapture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.DebugScreenCapture.html)> screenshotCaptureFunction = (screenshotFilePath, success, screenshotData) =>
        {
            screenshoFinished = true;
            if (!success || screenshotData.RawImageDataReference.Length == 0)
                return;  
  
            // Note: for the Memory Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) to be able to pick up the screenshot, the name and path needs to match that of the snapshot file, safe for the extension.
            // The path provided by the callback is based on the path provided to TakeSnapshot.
            if (Path.HasExtension(screenshotFilePath))
            {
                screenshotFilePath = Path.ChangeExtension(screenshotFilePath, ".tmppng");
            }  
  
            var texture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(screenshotData.Width, screenshotData.Height, screenshotData.ImageFormat, false, false);
            CopyDataToTexture(texture, screenshotData.RawImageDataReference);
            File.WriteAllBytes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.WriteAllBytes.html)(screenshotFilePath, texture.EncodeToPNG());
            if (Application.isPlaying[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isPlaying.html))
                UnityEngine.Object.Destroy(texture);
            else
                UnityEngine.Object.DestroyImmediate(texture);
            resultingScreenshotPath = screenshotFilePath;
        };  
  
        if (takeScreenshot)
            MemoryProfiler.TakeSnapshot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html)(snapshotFileName, snapshotCaptureFunction, screenshotCaptureFunction, captureFlags);
        else
            MemoryProfiler.TakeSnapshot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.TakeSnapshot.html)(snapshotFileName, snapshotCaptureFunction, captureFlags);  
  
        // The finishCallback is called first.
        while (!snapshotFinished)
        {
            yield return null;
        }
        // The screenshotCallback is called second and can take a moment longer,
        // but don't wait for it if it is not being taken.
        while (takeScreenshot && !screenshoFinished)
        {
            yield return null;
        }  
  
        if (resultingSnapshotPath != null && File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(resultingSnapshotPath))
        {
            var finalSnapshotPath = Path.ChangeExtension(resultingSnapshotPath, ".snap");
            var finalScreenshotPath = resultingScreenshotPath != null ? Path.ChangeExtension(resultingScreenshotPath, ".png") : null;  
  
            // Remove any pre-existing files first.
            if (File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(finalSnapshotPath))
                File.Delete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Delete.html)(finalSnapshotPath);
            if (finalScreenshotPath != null && File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(finalScreenshotPath))
                File.Delete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Delete.html)(finalScreenshotPath);  
  
            // Now that writing to the file has succesfully completed, rename the file to the .snap extension to denote that the Memory Profiler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) can open it.
            File.Move(resultingSnapshotPath, finalSnapshotPath);
            if (finalScreenshotPath != null)
                File.Move(resultingScreenshotPath, finalScreenshotPath);  
  
            // If you don't have access to the Player's file system you could also upload the file to an end-point that is accessible to you here.
        }
    }  
  
    static void CopyDataToTexture(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex, NativeArray<byte> byteArray)
    {
        unsafe
        {
            void* srcPtr = NativeArrayUnsafeUtility.GetUnsafeBufferPointerWithoutChecks[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeArrayUnsafeUtility.GetUnsafeBufferPointerWithoutChecks.html)(byteArray);
            void* dstPtr = tex.GetRawTextureData<byte>().GetUnsafeReadOnlyPtr();
            UnsafeUtility.MemCpy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.MemCpy.html)(dstPtr, srcPtr, byteArray.Length * sizeof(byte));
        }
    }
}

```

Additional resources: [Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/), [Application.dataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html), [DebugScreenCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.DebugScreenCapture.html), [MemoryProfiler.CreatingMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.CreatingMetadata.html), [PlayerConnectionGUIUtility.GetConnectionState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUIUtility.GetConnectionState.html), [EditorCoroutineUtility](https://docs.unity3d.com/Packages/com.unity.editorcoroutines@latest/index.html?subfolder=/api/Unity.EditorCoroutines.Editor.EditorCoroutineUtility.html).
* * *
