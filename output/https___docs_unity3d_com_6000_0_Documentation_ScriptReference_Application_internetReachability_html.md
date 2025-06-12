* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-internetReachability.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).internetReachability
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
[NetworkReachability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NetworkReachability.html) internetReachability; 
### Description
Returns the type of internet reachability currently possible on the device.
This property is mostly useful on handhelds to distinguish fast and cheap WiFi connection from carrier networking.  
  
**Note** : Do not use this property to determine the actual connectivity. For example, the device can be connected to a hot spot, but not have the actual route to the network.   
  
Non-handhelds are considered to be always capable of [NetworkReachability.ReachableViaLocalAreaNetwork](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NetworkReachability.ReachableViaLocalAreaNetwork.html).
* * *
