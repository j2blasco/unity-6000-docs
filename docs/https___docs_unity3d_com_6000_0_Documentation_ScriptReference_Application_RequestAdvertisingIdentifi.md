* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestAdvertisingIdentifierAsync.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).RequestAdvertisingIdentifierAsync
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
public static bool RequestAdvertisingIdentifierAsync([Application.AdvertisingIdentifierCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.AdvertisingIdentifierCallback.html) delegateMethod); 
### Parameters
Parameter | Description  
---|---  
delegateMethod | Delegate method.  
### Returns
**bool** Returns true if successful, and false for platforms which do not support Advertising Identifiers. In this case, the delegate method is not invoked. 
### Description
Request an advertising ID for iOS and UWP.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;  
  
public class SampleBehaviour : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void Start()
    {
        Application.RequestAdvertisingIdentifierAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.RequestAdvertisingIdentifierAsync.html)(
            (string advertisingId, bool trackingEnabled, string error) =>
            { Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("advertisingId " + advertisingId + " " + trackingEnabled + " " + error); }
        );
    }
}

```

* * *
