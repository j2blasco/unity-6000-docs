* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-ready.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).ready
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
ready; 
### Description
Returns true if Caching system is ready for use.
```
using System.Collections;
using UnityEngine;
using UnityEngine.Networking;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator IsCachingReadyExample(string uri)
    {
        //Using this conditional says we want to wait for our Caching[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html) system to be ready before trying to download bundles
        while (!Caching.ready[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-ready.html))
        {
            yield return null;
        }
        //Download the bundle
        UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) request = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)(uri);
        yield return request.SendWebRequest();
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(request);  
  
        //Do something with the AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)...  
  
        //Unload the AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)
        bundle.Unload(true);
    }
}

```

* * *
