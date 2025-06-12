* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceID.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).graphicsDeviceID
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
graphicsDeviceID; 
### Description
The identifier code of the graphics device (Read Only).
This is the PCI device ID of the user's graphics card. Together with [SystemInfo.graphicsDeviceVendorID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVendorID.html), this number uniquely identifies a particular graphics card model. The number is the same across operating systems and driver versions.  
  
Note that device IDs are only implemented on PC (Windows/Mac/Linux) platforms and on Android when running Vulkan; on other platforms you'll have to do name-based detection if needed.  
  
See [pci-ids.ucw.cz](http://pci-ids.ucw.cz/read/PC/) for a list of device IDs.  
  
Additional resources: [SystemInfo.graphicsDeviceVendorID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceVendorID.html), [SystemInfo.graphicsDeviceName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsDeviceName.html).
* * *
