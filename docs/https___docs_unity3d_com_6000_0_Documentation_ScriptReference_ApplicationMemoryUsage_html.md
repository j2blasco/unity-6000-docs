* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.html

# ApplicationMemoryUsage
enumeration
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
Describes the application memory usage level.
### Properties
Property | Description  
---|---  
[Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Unknown.html) | The memory usage level of the application is not known.  
[Low](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Low.html) | Application can safely allocate significant amounts of memory.  
[Medium](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Medium.html) | Application is at safe memory usage level and has some margin to allocate more.  
[High](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.High.html) | Application is at risk of getting low on memory. To prevent this, avoid allocating significant amounts of memory, and release some resources.  
[Critical](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.Critical.html) | Application is dangerously low on memory and is at risk of being closed by the Operating System. To prevent this, release some resources immediately.  
* * *
