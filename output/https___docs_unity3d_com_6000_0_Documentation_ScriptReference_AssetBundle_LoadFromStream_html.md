* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromStream.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).LoadFromStream
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
public static [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) LoadFromStream(Stream stream); 
## Declaration
public static [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) LoadFromStream(Stream stream, uint crc); 
## Declaration
public static [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) LoadFromStream(Stream stream, uint crc, uint managedReadBufferSize); 
### Parameters
Parameter | Description  
---|---  
stream | The managed Stream object. Unity calls Read(), Seek() and the Length property on this object to load the AssetBundle data.  
crc | An optional CRC-32 checksum of the uncompressed content.  
managedReadBufferSize | You can use this to override the size of the read buffer Unity uses while loading data. The default size is 32KB.  
### Returns
**AssetBundle** The loaded AssetBundle object or null when the object fails to load. 
### Description
Synchronously loads an AssetBundle from a managed Stream.
The function supports bundles of any compression type. **lzma** compressed data is decompressed to memory, while uncompressed and chunk-compressed bundles are read directly from the Stream.  
  
The content is compared against the checksum before it is loaded when the checksum is a non-zero value. An error is thrown if it does not match.  
  
Unlike [LoadFromStreamAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromStreamAsync.html), this function is synchronous and only returns when it has loaded the AssetBundle object.  
  
Unlike [LoadFromFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html), the data for the AssetBundle is supplied by a managed Stream object.  
  
The following are restrictions on a Stream object to optimize AssetBundle data loading: 
  1. The AssetBundle data must start at stream position zero.
  2. Unity sets the seek position to zero before it loads the AssetBundle data.
  3. Unity assumes the read position in the stream is not altered by any other process. This allows the Unity process to read from the stream without having to call Seek() before every read.
  4. stream.CanRead must return true.
  5. stream.CanSeek must return true.
  6. It must be accessible from threads different to the main thread. Seek() and Read() can be called from any Unity native thread.
  7. In certain circumstances, Unity tries to read past the size of the AssetBundle data. The Stream implementation must gracefully handle this without throwing exceptions. The Stream implementation must also return the actual number of bytes read (not including any bytes past the end of the AssetBundle data).
  8. When starting at the end of the AssetBundle data and trying to read data the Stream implementation must return 0 bytes read and not throw exceptions.


To reduce the number of calls from native to managed code the data is read from the Stream using a buffered reader with a buffer size of **managedReadBufferSize**.
  * Changing **managedReadBufferSize** may change the loading performance, especially on mobile devices.
  * The optimal value for **managedReadBufferSize** varies from project to project and potentially from Asset Bundle to Asset Bundle.
  * A good range of values to experiment with is: 8KB, 16KB, 32KB, 64KB, 128KB.
  * Larger values might be better for compressed Asset Bundles or if the Asset Bundle contains large sized assets or if the Asset Bundle does not contain many assets and they are loaded sequentially from the Asset Bundle.
  * Smaller values might be better for uncompressed Asset Bundles and reading lots of small assets or if the Asset Bundles has lots of assets in it and the asset are loaded in a random order.


Do not dispose the Stream object while loading the AssetBundle or any assets from the bundle. Its lifetime should be longer than the AssetBundle. This means you dispose the Stream object after calling [AssetBundle.Unload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.Unload.html).
```
using UnityEngine;
using System.Collections;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.IO;  
  
public class LoadFromStreamExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var fileStream = new FileStream(Application.streamingAssetsPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-streamingAssetsPath.html), FileMode.Open, FileAccess.Read);
        var myLoadedAssetBundle = AssetBundle.LoadFromStream[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromStream.html)(fileStream);
        if (myLoadedAssetBundle == null)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Failed to load AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)!");
            return;
        }  
  
        var prefab = myLoadedAssetBundle.LoadAsset<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>("MyObject");
        Instantiate(prefab);  
  
        myLoadedAssetBundle.Unload(false);
        fileStream.Dispose();
    }
}

```

Additional resources: [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html), [LoadFromStreamAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromStreamAsync.html) [LoadFromFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html).
* * *
