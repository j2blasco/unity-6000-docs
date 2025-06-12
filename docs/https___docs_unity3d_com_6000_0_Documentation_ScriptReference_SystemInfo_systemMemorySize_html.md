* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-systemMemorySize.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).systemMemorySize
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
systemMemorySize; 
### Description
Amount of system memory present (Read Only).
This is the approximate amount of system memory in megabytes.  
  
**WebGL** : This function will return the current size of the asm.js/WebAssembly heap. Note that when using WebAssembly, the heap size can increase at run-time if the Unity content memory-usage exceeds the [initial memory size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.WebGL-memorySize.html). **Windows Store Apps** : This function is not supported on Windows Store Apps and will always return 0.  
  
Additional resources: [SystemInfo.graphicsMemorySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-graphicsMemorySize.html).
* * *
