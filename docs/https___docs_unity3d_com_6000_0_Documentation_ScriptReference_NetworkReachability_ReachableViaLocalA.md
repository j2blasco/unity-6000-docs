* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NetworkReachability.ReachableViaLocalAreaNetwork.html

#  [NetworkReachability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NetworkReachability.html).ReachableViaLocalAreaNetwork
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
Network is reachable via WiFi or cable.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//This script checks the device’s ability to reach the internet and outputs it to the console window  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string m_ReachabilityText;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
//Output the network reachability to the console window
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Internet : " + m_ReachabilityText);
        //Check if the device cannot reach the internet
        if (Application.internetReachability[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-internetReachability.html) == NetworkReachability.NotReachable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NetworkReachability.NotReachable.html))
        {
            //Change the Text
            m_ReachabilityText = "Not Reachable.";
        }
        //Check if the device can reach the internet via a carrier data network
        else if (Application.internetReachability[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-internetReachability.html) == NetworkReachability.ReachableViaCarrierDataNetwork[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NetworkReachability.ReachableViaCarrierDataNetwork.html))
        {
            m_ReachabilityText = "Reachable via carrier data network.";
        }
        //Check if the device can reach the internet via a LAN
        else if (Application.internetReachability[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-internetReachability.html) == NetworkReachability.ReachableViaLocalAreaNetwork[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NetworkReachability.ReachableViaLocalAreaNetwork.html))
        {
            m_ReachabilityText = "Reachable via Local Area Network.";
        }
    }
}

```

* * *
